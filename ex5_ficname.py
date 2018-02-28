import pandas as pd 
import numpy as np 

# Create the 3 DataFrames based on the followin raw data
raw_data_1 = {
	'subject_id':['1','2','3','4','5'],
	'first_name':['Alex','Amy','Allen','Alcie','Ayoung'],
	'last_name':['Anderson','Ackerman','Ali','Aoni','Atiches']
}

raw_data_2 = {
	'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']
}

raw_data_3 = {
	'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]
}

# Assign each to a variable called data1, data2, data3
data1 = pd.DataFrame(raw_data_1, columns = ['subject_id','first_name','last_name'])
data2 = pd.DataFrame(raw_data_2, columns = ['subject_id','first_name','last_name'])
data3 = pd.DataFrame(raw_data_3, columns = ['subject_id','test_id'])

print data3

# Join the two dataframes along rows and assign all_data
all_data0 = pd.concat([data1,data2])
print all_data0

all_data = pd.concat([data1,data2],axis=1) #Join the two dataframes along columns and assing to all_data_col
print all_data

# print pd.merge(all_data,data3,on = 'subject_id')

print pd.merge(data1,data2,on='subject_id',how='inner') # Merge only the data that has the same 'subject_id' on both data1 and data2

print pd.merge(data1, data2, on='subject_id', how='outer') # Merge all values in data1 and data2, with matching records from both sides where available
