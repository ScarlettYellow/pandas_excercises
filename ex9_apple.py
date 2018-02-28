import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

apple = pd.read_csv("/Users/scarlett/repository/pandas/ex9.1_apple/ex8_dataset.csv")

print apple.dtypes
print apple.head(3)

apple.Date = pd.to_datetime(apple.Date)
print apple['Date'].head()

apple = apple.set_index('Date')
print apple.head(3)

print apple.sort_index(ascending=True).head()

apple_month = apple.resample('BM').mean()
print apple_month.head()

print (apple.index.max() - apple.index.min()).days

apple_months = apple.resample('BM').mean()
print len(apple_months.index)

appl_open = apple['Adj Close'].plot(title = "Apple Stock")
fig = appl_open.get_figure()
print fig.set_size_inches(13.5,9)
plt.show()

