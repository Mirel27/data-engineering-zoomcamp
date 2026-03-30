import sys
import pandas as pd


print("arguments", sys.argv) # to pass arguments
month = sys.argv[1] # get the first argument
print("month", month) # print the month argument

df=pd.DataFrame({"A":[1,2],"B":[3,4]})
print(df.head()) # print the first 5 rows of the dataframe
df.to_parquet(f"output_{month}.parquet") # save the dataframe as a parquet file in the output directory with the name of the month