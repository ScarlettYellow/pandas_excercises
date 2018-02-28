import pandas as pd 
import numpy as np

euro12 = pd.read_csv('/Users/scarlett/repository/pandas/ex2.1_euro12/ex2.1_dataset.csv')

euro12

print euro12.info()

print euro12.index

print euro12.head(3)

print euro12['Goals']

print euro12.shape[0]

descipline = euro12[['Team','Yellow Cards','Red Cards']] # View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
print descipline

print euro12.sort_values(['Red Cards','Yellow Cards']) # Sort the teams by Red Cards, then to Yellow Cards

print euro12.mean()['Yellow Cards'] # Calculate the mean Yellow Cards given per Team

print euro12[euro12['Goals'] > 6] # Filter teams that scored more than 6 goals

print euro12[euro12.Team.str.startswith('G')]

print euro12.iloc[:,0:7] # Select the first 7 columns

print euro12.iloc[0,:] # Select the first column

print euro12.iloc[1,1] 

print euro12.iloc[:, :-3] # Select all columns except the last 3

# .loc is another way to slice, using the labels of the columns and indexes
print euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']] # Present only the Shooting Accuracy from England, Italy and Russia
