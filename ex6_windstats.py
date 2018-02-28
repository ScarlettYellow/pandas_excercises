import pandas as pd 
import numpy as np

data = pd.read_table("/Users/scarlett/repository/pandas/ex6.1_windstats/ex6_dataset.csv")
print data.head()

print data.info()

#  Year 2061? Do we really have data from this year? Create a function to fix it and apply it.
# def fix_century(x):
# 	year = x.year - 100 if x.year > 1989 else x.year
# 	return datetime.date(year,x.month,x.day)
# data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)
# data.head()

# Compute how many values are missing for each location over the entire record
print data.isnull().sum()

# Compute how many non-missing values there are in total
print data.shape[1] - data.isnull().sum()

# Calculate the mean windspeeds of the windspeeds over all the locations and all the times
print data.mean().mean()

# Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
loc_stats = pd.DataFrame()

loc_stats['min'] = data.min() # min
loc_stats['max'] = data.max() # max 
loc_stats['mean'] = data.mean() # mean
loc_stats['std'] = data.std() # standard deviations

print loc_stats

# Create a DataFrame called day_stats and calculate the min, max and mean windspeed and standard deviations of the windspeeds across all the locations at each day.
day_stats = pd.DataFrame()
day_stats['min'] = data.min(axis=1)
day_stats['max'] = data.max(axis=1)
day_stats['mean'] = data.mean(axis=1)
day_stats['std'] = data.std(axis=1)
print day_stats.head()

# Find the average windspeed in January for each location.
data['date'] = data.index
data['month'] = data['date'].apply(lambda date:date.month)
data['year'] = data['date'].apply(lambda date:date.year)
data['day'] = data['date'].apply(lambda date: date.day)
january_winds = data.query('month == 1')
january_winds.loc[:,'RPT':"MAL"].mean()


# Downsample the record to a yearly/monthly/weekly frequency for each location
data.query('month == 1 and day == 1')
data.query('day==1')
data[::7].head()

# Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 52 week
weekly = data.resample('W').agg(['min','max','mean','std']) 
weekly.ix[1:53,"RPT":"MAL"].head()




















