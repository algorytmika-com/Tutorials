# invoke a database query
Invoke-Sqlcmd -Query "SELECT * FROM dbo.Products"

# connect to a database
Invoke-Sqlcmd -ConnectionString "Data Source=ComputerName, 12345; Initial Catalog=AdventureWorks; Integrated Sceurity=true"

# disconnect from a remote computer
Exit-PSSession

# connect to a remote computer
Enter-PSSession -ComputerName $ComputerName