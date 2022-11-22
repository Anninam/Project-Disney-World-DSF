import pandas as pd 
import numpy as np 

metadata = pd.read_csv("../Data_DSF_Project/metadata.csv")

print(metadata)

#### The column names are: 
#Index(['DATE', 'WDW_TICKET_SEASON', 'DAYOFWEEK', 'DAYOFYEAR', 'WEEKOFYEAR',
#       'MONTHOFYEAR', 'YEAR', 'SEASON', 'HOLIDAYPX', 'HOLIDAYM',
#       ...
#       'HSFIREWKS', 'AKPRDDAY', 'AKPRDDT1', 'AKPRDDT2', 'AKPRDDN', 'AKFIREN',
#       'AKSHWNGT', 'AKSHWNT1', 'AKSHWNT2', 'AKSHWNN'],
#      dtype='object', length=181)
#print(metadata.columns)

### Summary of data:
#print(metadata.describe())

### Shape of data:
#print(metadata.shape) #(2079, 181)

### Looking at subsets:
#print(metadata[["SEASON"]])
#print(metadata.dropna(subset =["WDW_TICKET_SEASON"]))
#print(metadata[["HOLIDAYM"]])
#X = metadata.dropna(subset =["HOLIDAYN"])
#print(X[["HOLIDAYN"]])

#print("Hello World")

### Looking at data only for 2021
#metadata_21 = metadata.loc[(metadata["YEAR"] == 2021)]
#print(metadata_21)
# shape: [104 rows x 181 columns]
#metadata_21_dropna = metadata_21.dropna() 
# print(metadata_21_dropna) # [0 rows x 181 columns] -> every row has NaN values

pirates = pd.read_csv("../Data_DSF_Project/pirates_of_caribbean.csv")
#print(pirates) #[301946 rows x 4 columns] -> data from every 30min ish

# SACTMIN = Actual Wait Time (in minutes)
# SPOSTMIN = Standby Posted Wait Time (in minutes)
print(pirates)
