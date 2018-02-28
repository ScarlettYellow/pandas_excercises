import pandas as pd 
import numpy as np 

drinks = pd.read_csv('/Users/scarlett/repository/pandas/ex3.1_drinks/ex3_dataset.csv')

print drinks

print drinks.info()

print drinks.groupby('continent').beer_servings.mean() #  Which continent drinks more beer on average?

print drinks.groupby('continent').wine_servings.describe() # For each continent print the statistics for wine consumption

print drinks.groupby('continent').mean() #  Print the mean alcoohol consumption per continent for every column

print drinks.groupby('continent').median() # Print the median alcoohol consumption per continent for every column

print drinks.groupby('continent').spirit_servings.agg(['mean','min','max']) # Print the mean, min and max values for spirit consumption
