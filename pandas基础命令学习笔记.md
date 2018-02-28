# 1.简介

pandas和numpy是用Python做数据分析最基础且最核心的库

# 2.缩写解释 & 库的导入

df --- 任意的pandas DataFrame(数据框)对象
s --- 任意的pandas Series(数组)对象

```
import pandas as pd # 导入pandas库并简写为pd
import numpy as np # 导入numpy库并简写为np
```

# 3.数据的导入

```python
pd.read_csv(filename) # 导入csv格式文件中的数据
pd.read_table(filename) # 导入有分隔符的文本 (如TSV) 中的数据
pd.read_excel(filename) # 导入Excel格式文件中的数据
pd.read_sql(query, connection_object) # 导入SQL数据表/数据库中的数据
pd.read_json(json_string) # 导入JSON格式的字符，URL地址或者文件中的数据
pd.read_html(url) # 导入经过解析的URL地址中包含的数据框 (DataFrame) 数据
pd.read_clipboard() # 导入系统粘贴板里面的数据
pd.DataFrame(dict)  # 导入Python字典 (dict) 里面的数据，其中key是数据框的表头，value是数据框的内容。
```

# 4.数据的导出

```python
df.to_csv(filename) # 将数据框 (DataFrame)中的数据导入csv格式的文件中
df.to_excel(filename) # 将数据框 (DataFrame)中的数据导入Excel格式的文件中
df.to_sql(table_name,connection_object) # 将数据框 (DataFrame)中的数据导入SQL数据表/数据库中
df.to_json(filename) # 将数据框 (DataFrame)中的数据导入JSON格式的文件中
```

# 5.创建测试对象

```python
pd.DataFrame(np.random.rand(10,5)) # 创建一个5列10行的由随机浮点数组成的数据框 DataFrame
```

```
//# 从一个可迭代的对象 my_list 中创建一个数据组

my_list = ['Kesci',100,'欢迎来到科赛网']
pd.Series(my_list) 

df.index = pd.date_range('2017/1/1', period = df.shape[0]) # 添加一个日期索引 index

```

```
import pandas as pd
import numpy as np
df= DataFrame(np.random.rand(10,10))
df.index = pd.date_range('2018/1/1',period=df.shape[0])
df
```

# 6.数据的查看与检查

```python
df.head(n)  # 查看数据框的前n行
df.shape #查看数据框的行数与列数
df.tail(3) #查看数据框的最后n行
df.info() #查看数据框的索引、数据类型和内存信息
df.describe() # 对于数据类型为数值型的列，查询其描述性统计的内容
s.value_counts(dropna=False) #查询每个独特数据值出现次数统计
df.dtypes #查看每列的数据类型

//示例
df = pd.DataFrame(np.random.rand(10,5))
df.head(3) # 查看数据框的前3行
df.apply(pd.Series.value_counts) #查询数据框中每个列的独特数据值出现次数统计

df = pd.DataFrame(np.random.rand(10,5))
df.tail(4) #查看数据框的最后4行
df.shape #查看数据框的行数与列数

s = pd.Series([1,2,3,4,np.nan,5,5,6,7,8])
s.value_counts(dropna=False)
```

```python
# 将字符型转为浮点数
dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer) # change item_price into float
print chipo.item_price
```

# 7.数据的选取

```
df[col] #以数组series形式返回选取的列

df = pd.DataFrame(np.random.rand(5,5),columns=list('ABCDE'))
df['C']
```

```
df[[col1,col2]]  # 以新的数据框(DataFrame)的形式返回选取的列

df = pd.DataFrame(np.random.rand(5,5),columns=list('ABCDE'))
df[['B','E']]
```

```
s.iloc[0] #按照位置选取

s = pd.Series(np.array(['I','Love','Data']))
s.iloc[0]
```

```
s.loc['index_one'] # 按照索引选取

s = pd.Series(np.array(['I','Love','Data']))
s.loc[1]
```

```
df.iloc[0,:] # 选取第一行

df = pd.DataFrame(np.random.rand(5,5),columns=list('ABCDE'))
df.iloc[0,:]
```

```
df.iloc[0,0] # 选取第一行的第一个元素

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.iloc[0,0]
```

```python
euro.iloc[: , :-3] # Select all columns except the last 3
```

```python
# .loc is another way to slice, using the labels of the columns and indexes
print euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']] # Present only the Shooting Accuracy from England, Italy and Russia
```

# 8.数据的清洗

```python
del crime['Total']
```

```
df.columns = ['a','b'] # 重命名数据框的列名称

df = pd.DataFrame({'A':np.array([1,np.nan,2,3,6,np.nan]),
                 'B':np.array([np.nan,4,np.nan,5,9,np.nan]),
                  'C':'foo'})
df.columns = ['a','b','c']
df
```

```
pd.isnull() # 检查数据中空值出现的情况，并返回一个由布尔值(True,Fale)组成的列

df = pd.DataFrame({'A':np.array([1,np.nan,2,3,6,np.nan]),
                 'B':np.array([np.nan,4,np.nan,5,9,np.nan]),
                  'C':'foo'})
pd.isnull(df)
```

```python
pd.notnull() # 检查数据中非空值出现的情况，并返回一个由布尔值(True,False)组成的列

df = pd.DataFrame({'A':np.array([1,np.nan,2,3,6,np.nan]),
                 'B':np.array([np.nan,4,np.nan,5,9,np.nan]),
                  'C':'foo'})
pd.notnull(df)
```

```python
df.dropna() # 移除数据框 DataFrame 中包含空值的行

df = pd.DataFrame({'A':np.array([1,np.nan,2,3,6,np.nan]),
                 'B':np.array([np.nan,4,np.nan,5,9,np.nan]),
                  'C':'foo'})
df.dropna()
```

```python
df.dropna(axis=1) # 移除数据框 DataFrame 中包含空值的列

df = pd.DataFrame({'A':np.array([1,np.nan,2,3,6,np.nan]),
                 'B':np.array([np.nan,4,np.nan,5,9,np.nan]),
                  'C':'foo'})
df.dropna(axis=1)
```

```python
df.dropna(axis=1,thresh=n) # 移除数据框df中空值个数不超过n的行

df = pd.DataFrame({'A':np.array([1,np.nan,2,3,6,np.nan]),
                 'B':np.array([np.nan,4,np.nan,5,9,np.nan]),
                  'C':'foo'})
test = df.dropna(axis=1,thresh=1)
test
```

```python
df.fillna(x) # 将数据框 DataFrame 中的所有空值替换为 x

df = pd.DataFrame({'A':np.array([1,np.nan,2,3,6,np.nan]),
                 'B':np.array([np.nan,4,np.nan,5,9,np.nan]),
                  'C':'foo'})
df.fillna('Test')
```

```python
s.fillna(s.mean()) #将所有空值替换为平均值

s = pd.Series([1,3,5,np.nan,7,9,9])
s.fillna(s.mean())
```

```python 
s.astype(float) # 将数组(Series)的格式转化为浮点数

s = pd.Series([1,2,np.nan,2,3])
s.astype(float)
```

```python
s = pd.Series([1,3,5,np.nan,7,9,9]) #将数组(Series)中的所有1替换为'one'
s.replace(1,'one')
```

```python
s = pd.Series([1,3,5,np.nan,7,9,9])
s.replace([1,3],['one','three']) # 将数组(Series)中所有的1替换为'one', 所有的3替换为'three'
```

```python
df.rename(columns=lambda x: x + 2) # 将全体列重命名

df = pd.DataFrame(np.random.rand(4,4))
df.rename(columns=lambda x: x+ 2)
```

```python
df.rename(columns={'old_name': 'new_ name'}) # 将选择的列重命名

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.rename(columns={'A':'newA','C':'newC'})
```

```python
df.set_index('column_one') # 改变索引

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.set_index('B')
```

```python
df.rename(index = lambda x: x+ 1) # 改变全体索引

df = pd.DataFrame(np.random.rand(10,5))
df.rename(index = lambda x: x+ 1)
```

# 9.数据的过滤(filter),排序(sort)和分组(groupby)

```python
# Reset the index so it begins with 0 again
iris = iris.resnet_index(drop = True)
print iris.head()
```

```python 
apple.sort_index(ascending = True).head()
```

```python
euro12[euro12.Team.str.startswith('G')] #Select the teams that start with G

```

```python
df[df[col] > 0.5] # 选取数据框df中对应行的数值大于0.5的全部列

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df[df['A'] > 0.5]
```

```python
df[(df[col] > 0.5) & (df[col] < 0.7)] # 选取数据框df中对应行的数值大于0.5，并且小于0.7的全部列

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df[(df['C'] > 0.5) & (df['D'] < 0.7)]
```

```python
df.sort_values(col1) # 按照数据框的列col1升序(ascending)的方式对数据框df做排序

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.sort_values('E')
```

```python
df.sort_values(col2,ascending=False) # 按照数据框的列col2降序(descending)的方式对数据框df做排序

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.sort_values('A',ascending=False)
```

```python
df.sort_values([col1,col2],ascending=[True,False]) # 按照数据框的列col1升序，col2降序的方式对数据框df做排序

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.sort_values(['A','E'],ascending=[True,False])
```

```python
df.groupby(col) # 按照某列对数据框df做分组

df = pd.DataFrame({'A':np.array(['foo','foo','foo','foo','bar','bar']),
      'B':np.array(['one','one','two','two','three','three']),
     'C':np.array(['small','medium','large','large','small','small']),
     'D':np.array([1,2,2,3,3,5])})

df.groupby('A').count()
```

```python 
df.groupby([col1,col2]) # 按照列col1和col2对数据框df做分组

df = pd.DataFrame({'A':np.array(['foo','foo','foo','foo','bar','bar']),
      'B':np.array(['one','one','two','two','three','three']),
     'C':np.array(['small','medium','large','large','small','small']),
     'D':np.array([1,2,2,3,3,5])})

df.groupby(['B','C']).sum()
```

```python
df.groupby(col1)[col2].mean() # 按照列col1对数据框df做分组处理后，返回对应的col2的平均值

df = pd.DataFrame({'A':np.array(['foo','foo','foo','foo','bar','bar']),
      'B':np.array(['one','one','two','two','three','three']),
     'C':np.array(['small','medium','large','large','small','small']),
     'D':np.array([1,2,2,3,3,5])})
df.groupby('B')['D'].mean()
```

```python
df.groupby(col1)[col2].mean() # 按照列col1对数据框df做分组处理后，返回对应的col2的平均值

df = pd.DataFrame({'A':np.array(['foo','foo','foo','foo','bar','bar']),
      'B':np.array(['one','one','two','two','three','three']),
     'C':np.array(['small','medium','large','large','small','small']),
     'D':np.array([1,2,2,3,3,5])})
df.groupby('B')['D'].mean()
```

```
//计算每一单的平均金额
order_grouped = chipo.groupby(by=['order_id']).sum() 
print order_grouped.mean()['item_price'] #What is the average amount per order?
```

```pythyon
df.pivot_table(index=col1,values=[col2,col3],aggfunc=mean) # 做透视表，索引为col1,针对的数值列为col2和col3，分组函数为平均值

df = pd.DataFrame({'A':np.array(['foo','foo','foo','foo','bar','bar']),
      'B':np.array(['one','one','two','two','three','three']),
     'C':np.array(['small','medium','large','large','small','small']),
     'D':np.array([1,2,2,3,3,5])})

df.pivot_table(df,index=['A','B'],
               columns=['C'],aggfunc=np.sum)
```

```python
df.groupby(col1).agg(np.mean) # 以col1分组，分组函数为平均值

df = pd.DataFrame({'A':np.array(['foo','foo','foo','foo','bar','bar']),
      'B':np.array(['one','one','two','two','three','three']),
     'C':np.array(['small','medium','large','large','small','small']),
     'D':np.array([1,2,2,3,3,5])})
df.groupby('A').agg(np.mean)
```

```python
df.apply(np.mean) # 对数据框df的每一列求平均值

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.apply(np.mean)
```

```python
df.apply(np.max,axis=1) # 对数据框df的每一行求最大值

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.apply(np.max,axis=1)
```

# 10.数据的连接(join)与组合(combine)

```python
df1.append(df2) # 在数据框df2的末尾添加数据框df1，其中df1和df2的列数应该相等

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df1.append(df2)
```

```python
df1.join(df2,on=col1,how='inner') # 对数据框df1和df2做内连接，其中连接的列为col1

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],           
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'key': ['K0', 'K1', 'K0', 'K1']})
   

df2 = pd.DataFrame({'C': ['C0', 'C1'],
                      'D': ['D0', 'D1']},
                     index=['K0', 'K1'])
   

df1.join(df2, on='key')
```

```python 
pd.merge(data1, data2, on='subject_id', how='inner') #Merge only the data that has the same 'subject_id' on both data1 and data2

pd.merge(data1, data2, on='subject_id', how='outer') # Merge all values in data1 and data2, with matching records from both sides where available
```

# 11.数据的统计

```python
df.describe() # 得到数据框df每一列的描述性统计
df.mean()
df.describe(include = "all") #统计所有的列

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.describe()

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.mean()
```

```python
df.corr() # 得到数据框df中每一列与其他列的相关系数

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.corr()
```

```python
df.count() # 得到数据框df中每一列的非空值个数

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.count()
```

```python
df.max() # 得到数据框df中每一列的最大值

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.max()
```

```python
df.min() # 得到数据框df中每一列的最小值

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.min()
```

```python
df.median() # 得到数据框df中每一列的中位数

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.median()
```

```python
df.std() # 得到数据框df中每一列的标准差

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
df.std()
```

