import pandas as pd 
import numpy as np 

iris = pd.read_csv("/Users/scarlett/repository/pandas/ex10.1_Iris/ex10_dataset.csv")

print iris.head()

iris.columns = ['sepal_length','sepal_width','petal_length','petal_width','class']
print iris.head()

print pd.isnull(iris).sum()

# Lets set the values of the rows 10 to 29 of the column 'petal_length' to NaN
iris.iloc[10:30,2:3]= np.nan
print iris.head(20)

# substitute the NaN values to 1.0
iris .petal_length.fillna(1,inplace = True)
print iris

# delete the column class
del iris['class']
print iris.head()

iris.iloc[0:3,:] = np.nan 
print iris.head()

# Delete the rows that have NaN
iris = iris.dropna(how='any')
iris.head()

# Reset the index so it begins with 0 again
iris = iris.resnet_index(drop = True)
print iris.head()

