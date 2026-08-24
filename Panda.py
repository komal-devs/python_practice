# Pandas Practice
# A human-readable collection of my Pandas practice and examples.

import numpy as np
import pandas as pd
# series 
my_list = [10,20,30,40]
pd.Series(my_list)

labels = ['a','b','c','d']
pd.Series(my_list,index = labels)


# creating series using dictionary 
d = {1 : 10,2 : 20,3: 30}
pd.Series(d)
# creating series using array
arr = np.array([10,20,300])
pd.Series(arr)


# creating a dataframe

data = {'Name': ['Linda','Peter','John','Marry'],
       'Age': [28,32,67,49],
       'City' : ['New York','Paris','London','Berlin'],
       'Salary' : [20000,3000000,45679,32000]}
df = pd.DataFrame(data)
df


# datafranme using list
data_list = [['Linda',28,'New York',20000],
            ['Peter',32,'Paris',3000000],
            ['John',67,'London',45679],
            ['Marry',49,'Berlin',32000]]
df2 = pd.DataFrame(data_list)
df2


# Selection and indexing of columns

labels = ['Name','Age','City','Salary']

df2 = pd.DataFrame(data_list,columns = labels)
df2

df2['City']


# accessing multiple columns
df2[['City','Age']]


# creating a new column

df2['Designation'] = ['Doc','Eng','Doc','Eng']
df2


# removing columns

df2.drop("Designation",axis = 1)


# to drop a column permanently use inplace = True 
# by default inplace ,= False is set
df2


# Selecting rows


# df2[0] will give key error
df2.loc[0]

df2.loc[[2,3]]

df2.iloc[1] # index based searching

# # Selecting subset of rows and columns

df2

df2.loc[[0,1]][["Salary","Designation"]]

df2.loc[[2,3]][['Name','Age']]


# conditional selection


# i want to select student whose age > 49
df2

df2[df2['Age']> 49]


# i want to see people whose age > 30 and must be resident of paris
df2[(df2['Age']>30)& (df2['City'] == 'Paris')]


# finding missing data

data = {'A': [1,2,3,4,5],
       'B': [1.0,2,3,4,5],
       'C':[1,2,3,np.nan,np.nan],
       'D': [1,np.nan,np.nan,np.nan,5]}
df = pd.DataFrame(data)
df

df.isna() # checks the null value

df.isna().sum()


# removing missing data
df.dropna()

df.dropna(thresh = 3) # returns column with 3 values


# filling missing values

df.fillna(0)

df.fillna(1)

values = {'A': 100,'B':209,'C':300,'D':400}
df.fillna(value = values)

df

df.fillna(df.mean())

df.fillna(df.max())


# Merging two dataframes

df1 = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Komal", "Riya", "Anu", "Priya"],
    "course": ["CSE", "IT", "CSE", "ECE"]
})
df1

df2 = pd.DataFrame({
    "student_id": [1, 2, 3, 5],
    "marks": [85, 90, 78, 88],
    "grade": ["A", "A+", "B+", "A"]
})
df2

pd.merge(df1,df2)

pd.merge(df1,df2,on = "student_id",how = "inner")

pd.merge(df1,df2,on = "student_id",how = "outer") 
# outer - merges all data with filling nulls

pd.merge(df1,df2,on = "student_id",how = "left")

pd.merge(df1,df2,on = "student_id",how = "right") # merging all values of right table


# concatenation of two dataframes

df1

df2

pd.concat([df1,df2])

pd.concat([df1,df2],axis = 1)


# joining two dataframes

df1 = pd.DataFrame({'Name': ['Alice','Bob','Charlie']},index = [1,2,3])
df1

df2 = pd.DataFrame({'Score':[ 10,20,30]},index = [2,3,4])
df2

df1.join(df2)

df2.join(df1)

df2.join(df1,how = "outer")


# group by

data = {
    "Date": ["Jan", "Jan", "Jan", "Feb", "Feb", "Feb",
             "Mar", "Mar", "Mar", "Apr", "Apr", "Apr"],
    
    "Region": ["North", "South", "North", "South", "North", "South",
               "North", "South", "North", "South", "North", "South"],
    
    "Product": ["Laptop", "Laptop", "Phone", "Phone", "Tablet", "Tablet",
                "Laptop", "Laptop", "Phone", "Phone", "Tablet", "Tablet"],
    
    "Sales": [50000, 45000, 30000, 28000, 20000, 22000,
              55000, 48000, 32000, 30000, 25000, 27000],
    
    "Units": [5, 4, 6, 5, 8, 9, 6, 5, 7, 6, 10, 11]
}

df = pd.DataFrame(data)
df

df.groupby("Region")["Sales"].mean()

pd.pivot_table(df, values="Sales", index="Product", aggfunc="sum")


# cross tab = return count

data = {
    "Gender": ["Female", "Male", "Female", "Male", "Female",
               "Male", "Female", "Male", "Female", "Male"],

    "Course": ["Python", "Python", "SQL", "SQL", "Python",
               "SQL", "SQL", "Python", "Python", "SQL"],

    "Result": ["Pass", "Pass", "Pass", "Fail", "Pass",
               "Pass", "Fail", "Pass", "Fail", "Pass"]
}

df = pd.DataFrame(data)
df

pd.crosstab(df["Gender"], df["Course"])


# operations

df

df.info()

df.describe()

df.columns

df.shape

df['Result'] + '**'


# applying functions in dataframes

df = pd.DataFrame({"a" : [10,20,30,40]})
df

def square(x):
    return x**2

df['a'].apply(square)

df['b'] = df['a'].apply(lambda x : x**2)
df

