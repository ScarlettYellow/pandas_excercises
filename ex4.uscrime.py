import pandas as pd 
import numpy as np 

crime = pd.read_csv('/Users/scarlett/repository/pandas/ex4.1_uscrime/ex4_dataset.csv')

print crime.dtypes

# crime.Year = pd.to_datetime(crime.Year. format = '%Y')
# print crime.info()

crime = crime.set_index('Year',drop=True) # Set the Year column as the index of the dataframe
print crime.head()

del crime['Total'] # Delete the Total column
print crime.head()

crimes = crime.resample('10AS').sum()
population = crime['Population'].resample('10AS').max()
crimes['Population'] = population # Group the year by decades and sum the values
print crimes 

print crime.idxmax(0) # What is the mos dangerous decade to live in the US?
