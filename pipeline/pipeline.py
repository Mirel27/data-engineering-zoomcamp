import sys
import pandas as pd

month = sys.argv[1] # get the first argument

df=pd.DataFrame({"A":[1,2],"B":[3,4]})
# print the first 5 rows of the dataframe
df.to_parquet(f"output_{month}.parquet") # save the dataframe as a parquet file in the output directory with the name of the month