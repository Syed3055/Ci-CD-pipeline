CREATE TABLE [saless].[Dim_Customer] (

	[CustomerID] varchar(255) NOT NULL, 
	[CustomerName] varchar(255) NOT NULL, 
	[FirstName] varchar(255) NOT NULL, 
	[LastName] varchar(255) NOT NULL, 
	[EmailAddress] varchar(255) NOT NULL
);


GO
ALTER TABLE [saless].[Dim_Customer] ADD CONSTRAINT PK_Dim_Customer primary key NONCLUSTERED ([CustomerID]);