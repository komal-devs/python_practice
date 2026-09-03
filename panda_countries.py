import numpy as np
import pandas as pd
df = pd.read_csv(r"c:\Users\Dell\Downloads\Countries (1).csv")

# data preprocessing
print(df.shape)
df.info()

# which country has highest population
print(df[df["population"] == df["population"].max()])
# what is the capital of country that has highest population
print(df[df["population"] == df["population"].max()]["capital_city"])
print(df.columns)
# which country has least population
print(df[df["population"] == df["population"].min()])
# capital of country that has last population
print(df[df["population"] == df["population"].min()]["capital_city"])
# give me top 5 countries that has highest democratic score
print(df.sort_values(by = "democracy_score",ascending = False).head())
# how many total regions are there
print(df["region"].value_counts().count())
# how many countries in eastern europe region
print(df["region"].value_counts()["Eastern Europe"])
print(df[df["region"] == "Eastern Europe"]["country"])
# who is the leader of second highest populated region
print(df[df["population"]== df["population"].nlargest(2).iloc[1]]["political_leader"])
print(df[df["political_leader"].isna()]["country"].count())
print(df["country_long"])
