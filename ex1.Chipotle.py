import pandas as pd 
import numpy as np 

path1 = "/Users/scarlett/repository/pandas/ex1_Chipotle/ex1_dataset.tsv" #import the dataset 

chipo = pd.read_csv(path1,sep='\t') #Assign it to a variable called chipo

print chipo.head(3) #See the first 10 entries

print chipo.info() #What is the number of observations in the dataset?

print chipo.shape #What is the number of columns in the dataset?

print chipo.columns #Print the name of all the columns.

print chipo.index #How is the dataset indexed?

print chipo.item_name.nunique() #How many items were ordered?

print chipo.choice_description.value_counts(dropna=False).head() #hat was the most ordered item in the choice_description column?

print chipo.quantity.sum() #How many items were orderd in total?

dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer) #Turn the item price into a float
print chipo.item_price 

print chipo.item_price.sum() #How much was the revenue for the period in the dataset?

print chipo.order_id.value_counts().count()#How many orders were made in the period?

order_grouped = chipo.groupby(by=['order_id']).sum() 
print order_grouped.mean()['item_price'] #What is the average amount per order?
 
print chipo.item_name.nunique() #How many different items are sold?
print chipo.item_name.value_counts(dropna=False).count() #How many different items are sold?
