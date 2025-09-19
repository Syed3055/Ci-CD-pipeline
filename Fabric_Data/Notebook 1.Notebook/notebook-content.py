# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "3ec3dccc-2800-44a7-8964-25722f4b4c86",
# META       "default_lakehouse_name": "LH_55oo",
# META       "default_lakehouse_workspace_id": "010417d3-a626-4bd8-b75b-b5841fec3ed9",
# META       "known_lakehouses": [
# META         {
# META           "id": "3ec3dccc-2800-44a7-8964-25722f4b4c86"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql.functions import *
from pyspark.sql.types import *


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("abfss://full_end_to_end_project@onelake.dfs.fabric.microsoft.com/LH_55oo.Lakehouse/Files/bronze_github/refs/heads/main/sales.csv")
# df now is a Spark DataFrame containing CSV data from "abfss://full_end_to_end_project@onelake.dfs.fabric.microsoft.com/LH_55oo.Lakehouse/Files/bronze_github/refs/heads/main/sales.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = df.withColumn("First_name", split(col("CustomerName")," ").getItem(0))\
    .withColumn("Last_name",split(col("CustomerName")," ").getItem(1))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = df.withColumn("Item2",split(col("Item")," ").getItem(1))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df=df.withColumn("OrderDate",to_date(col("OrderDate")))\
    .withColumn("Quantity", col("Quantity").cast(IntegerType()))\
    .withColumn("UnitPrice", col("UnitPrice").cast(DoubleType()))\
    .withColumn("TaxAmount", col("TaxAmount").cast(DoubleType()))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.mode("overwrite").parquet("abfss://full_end_to_end_project@onelake.dfs.fabric.microsoft.com/LH_55oo.Lakehouse/Files/bronze_github/sales_filter.csv")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
