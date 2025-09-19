CREATE TABLE [saless].[Dim_Item] (

	[ItemID] varchar(255) NOT NULL, 
	[ItemName] varchar(255) NOT NULL
);


GO
ALTER TABLE [saless].[Dim_Item] ADD CONSTRAINT pk_dim_item primary key NONCLUSTERED ([ItemID]);