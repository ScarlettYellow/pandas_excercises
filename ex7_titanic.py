import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

titanic = pd.read_csv("/Users/scarlett/repository/pandas/ex7.1_titanic/ex7_dataset.csv")

print titanic.info()

# Set PassengerId as the index
print titanic.set_index('PassengerId').head()

# Create a pie chart presenting the male/female proportion

# males = (titanic['Sex'] == 'male').sum()
# females = (titanic['Sex'] == 'female').sum() # # sum the instances of males and females
# proportions = [males, females] # # put them into a list called proportions
# plt.pie(
# 	proportions,
# 	labels = ['Males','females'],
# 	shadow = True,
# 	colors = ['blue','yellow'],
# 	explode = (0.15,0),
# 	startangle = 90,
# 	autopct = '%1.1f%%'
# 	)
# plt.axis('equal')
# plt.title("Sex Proportion")
# plt.tight_layout()
# plt.show()

# Create a scatterplot with the Fare payed and the Age, differ the plot color by gender
lm = sns.lmplot(x = 'Age',y = 'Fare',data = titanic, hue = 'Sex',fit_reg=False) # # creates the plot using
lm.set(title = 'Fare x Age') #set a title
axes = lm.axes # # get the axes object and tweak it
axes[0,0].set_ylim(-5,)
axes[0,0].set_xlim(-5,85)

# How many people survived?
print titanic.Survived.sum()

# create a histogram with the Fare payed
df = titanic.Fare.sort_values(ascending=False)
binval = np.arange(0,600,10)
binval
plt.hist(df,bins=binval)
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.title('Fare Payed Histrogram')
plt.show()

