import pandas as pd 
import numpy as np 

path2 = "/Users/scarlett/repository/pandas/ex1.2_Occupation/ex2_dataset.tsv"

users = pd.read_csv(path2,sep='\t')

print users.head(3)

print users.shape

print users.tail(10)

print users.info()

print users.describe()

print users.columns

print users.index

print users.dtypes # What is the data type of each column?

print users.describe() # Summarize the DataFrame.

print users.describe(include='all')

