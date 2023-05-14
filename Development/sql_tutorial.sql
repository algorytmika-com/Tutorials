--find missing indexes
SELECT
CONVERT (varchar, getdate(), 126) AS runtime
, mig.index_group_handle
, mid.index_handle
, CONVERT (decimal (28,1), migs.avg_total_user_cost * migs.avg_user_impact *
(migs.user_seeks + migs.user_scans)) AS improvement_measure, 'CREATE INDEX missing_index_' + CONVERT (varchar, mig.index_group_handle) + '_' +
CONVERT (varchar, mid.index_handle) + ' ON ' + mid.statement + '
(' + ISNULL (mid.equality_columns,'')
+ CASE WHEN mid.equality_columns IS NOT NULL
AND mid.inequality_columns IS NOT NULL
THEN ',' ELSE '' END + ISNULL (mid.inequality_columns, '') + ')'
+ ISNULL (' INCLUDE (' + mid.included_columns + ')', '') AS
create_index_statement
, migs.*
, mid.database_id
, mid.[object_id]
FROM sys.dm_db_missing_index_groups AS mig
INNER JOIN sys.dm_db_missing_index_group_stats AS migs
ON migs.group_handle = mig.index_group_handle
INNER JOIN sys.dm_db_missing_index_details AS mid
ON mig.index_handle = mid.index_handle
WHERE mid.database_id = DB_ID()
ORDER BY migs.avg_total_user_cost * migs.avg_user_impact * (migs.user_seeks +
migs.user_scans) DESC


--shrink database
SELECT log_reuse_wait_desc
FROM sys.databases
WHERE name = 'dbtesting';
GO

SELECT DB_NAME() AS DbName,
	name AS FileName,
	type_desc,
	size/128.0 AS CurrentSizeMB,
	size/128.0 - CAST(FILEPROPERTY(name, 'SpaceUsed') AS INT)/128.0 AS FreeSpaceMB
FROM sys.database_files
WHERE type IN (0,1)
GO

ALTER DATABASE dbtesting SET RECOVERY SIMPLE WITH NO_WAIT;
GO

CHECKPOINT;
GO

DBCC SHRINKDATABASE (dbtesting);
GO

ALTER DATABASE dbtesting SET RECOVERY FULL WITH NO_WAIT;
GO

SELECT DB_NAME() AS DbName,
	name AS FileName,
	type_desc,
	size/128.0 AS CurrentSizeMB,
	size/128.0 - CAST(FILEPROPERTY(name, 'SpaceUsed') AS INT)/128.0 AS FreeSpaceMB
FROM sys.database_files
WHERE type IN (0,1)
GO

ALTER DATABASE dbtesting SET RECOVERY SIMPLE WITH NO_WAIT;
GO

--disk space monitoring
SELECT DISTINCT
volume_mount_point [Disk Mount Point],
file_system_type [File System Type],
logical_volume_name as [Logical Drive Name],
CONVERT(DECIMAL(18,2),total_bytes/1073741824.0) AS [Total Size in GB], ---1GB= 1073741824 bytes
CONVERT(DECIMAL(18,2),available_bytes/1073741824.0) AS [Available Size in GB],
CAST(CAST(available_bytes AS FLOAT)/ CAST(total_bytes AS FLOAT) AS
DECIMAL(18,2)) * 100 AS [Space Free %]
FROM sys.master_files
CROSS APPLY sys.dm_os_volume_stats(database_id, file_id)

-- create server login and database user
USE [master]
GO

CREATE LOGIN [LoginName] FROM WINDOWS WITH DEFAULT_DATABASE=[master], DEFAULT_LANGUAGE=[us_english]
GO

USE [CurrentDatabase]
GO

CREATE USER [DatabaseUser] FROM LOGIN [LoginName] 
GO

--add roles to a database user
ALTER ROLE db_datareader
ADD MEMBER [DatabaseUser]
GO

ALTER ROLE db_datawriter
ADD MEMBER [DatabaseUser]
GO