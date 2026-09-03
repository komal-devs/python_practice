import numpy as np
import pandas as pd
# loading the data
df = pd.read_csv(r"c:\Users\Dell\Downloads\anime (1).csv")

# printing first five rows
print(df.head())
# last five rows
print(df.tail())

# make a column for episode count
# feature extraction

def extract_episodes(Title):
    data = ""
    check = False
    for i in Title:
        if i == ')':
            break
        if check == True :
            data += i
        if i == '(':
            check = True
        
    return data


# applying extract_episodes
df["Episodes"] = df["Title"].apply(extract_episodes)
df["Episodes"] = df["Episodes"].str.replace(" eps"," ")
# convert string into integer
df["Episodes"] = df["Episodes"].astype(int)
print(df["Episodes"])

# adding a column for time stamp
print(df.iloc[1])
def extract_time(txt):
    data = ""
    pos = txt.find(")")
    start = pos+1
    end = pos + 20
    return txt[start:end]
df["Time"]  =  df["Title"].apply(extract_time)    
print(df["Time"])

# which anime has highest score
print(df[df["Score"] == df["Score"].max()]["Title"])

# top 5 highest score anime
print(df["Title"].head())

# anime that has highest episode count
print(df[df["Episodes"] == df["Episodes"].max()]["Title"])

# animes with top  5 highest count
print(df.sort_values("Episodes",ascending= False).head()["Title"])


        
    

