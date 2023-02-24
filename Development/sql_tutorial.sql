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