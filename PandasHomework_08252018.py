# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:22:56 2018

@author: markl
Homework

Your final report should include each of the following:


Player Count


Total Number of Players



Purchasing Analysis (Total)


Number of Unique Items
Average Purchase Price
Total Number of Purchases
Total Revenue



Gender Demographics


Percentage and Count of Male Players
Percentage and Count of Female Players
Percentage and Count of Other / Non-Disclosed



Purchasing Analysis (Gender)


The below each broken by gender


Purchase Count
Average Purchase Price
Total Purchase Value
Average Purchase Total per Person by Gender





Age Demographics


The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)


Purchase Count
Average Purchase Price
Total Purchase Value
Average Purchase Total per Person by Age Group





Top Spenders


Identify the the top 5 spenders in the game by total purchase value, then list (in a table):


SN
Purchase Count
Average Purchase Price
Total Purchase Value





Most Popular Items


Identify the 5 most popular items by purchase count, then list (in a table):


Item ID
Item Name
Purchase Count
Item Price
Total Purchase Value





Most Profitable Items


Identify the 5 most profitable items by total purchase value, then list (in a table):


Item ID
Item Name
Purchase Count
Item Price
Total Purchase Value




As final considerations:


You must use the Pandas Library and the Jupyter Notebook.
You must submit a link to your Jupyter Notebook with the viewable Data Frames.
You must include a written description of three observable trends based on the data.
See Example Solution for a reference on expected format.


"""

import pandas as pd
import numpy as np

DataFrame = pd.read_csv(r"C:\Users\markl\get_testing\UCI-Data-Analytics\Pandas\purchase_data.csv")
DataFrame.columns
DataFrame.describe()
DataFrameCopy = DataFrame.copy()

#Player Count
DataFrame_playerscount = DataFrame["SN"].nunique()
print(f"There are {DataFrame_playerscount} unique players")

#Purchasing Analysis (Total)
DataFrame_uniqueitems = DataFrame['Item Name'].nunique()
DataFrame_averageprice = DataFrame['Price'].mean()
NumberofPurchases = DataFrame['Purchase ID'].nunique()
TotalRevenue = DataFrame['Price'].sum()

SummaryPurchasing = pd.DataFrame({'Number of Unique Items': [DataFrame_uniqueitems],
                                  'Average Price': [DataFrame_averageprice],
                                  'Number of Purchases': [NumberofPurchases],
                                  'Total Revenue': [TotalRevenue]})

#Gender Demographics

#Percentage and count of male players
    
male_players = DataFrame.loc[DataFrame["Gender"] == "Male"]
female_players = DataFrame.loc[DataFrame["Gender"] == "Female"]
DataFrame.head()
other_players = DataFrame.loc[DataFrame["Gender"] == "Other / Non-Disclosed"]


male_count = male_players["SN"].nunique()
female_count = female_players["SN"].nunique()
total_players_count = DataFrame["SN"].nunique()
other_count = total_players_count - male_count - female_count

male_percentage = male_count / total_players_count
female_percentage = female_count / total_players_count
other_percentage = other_count / total_players_count


GenderDemographics = pd.DataFrame({"Gender Cat": ["Male","Female","Other"],
                                   "Percentage of Players": [male_percentage, female_percentage,other_percentage],
                                   "Total Counts": [male_count, female_count, other_count]})
    
GenderDemographics

#Purchase Count, Avg Purchase Price, Total Purchase Value and Avg Pur per Person
Male_Purchases = male_players["Purchase ID"].nunique()
Female_Purchases = female_players["Purchase ID"].nunique()
Others_Purchases = other_players["Purchase ID"].nunique()
Male_Avg_Price = male_players["Price"].mean()
Female_Avg_Price = female_players["Price"].mean()
Others_Avg_Price = other_players["Price"].mean()
Male_Avg_Per_Person = male_players["Price"].sum() / male_count
Female_Avg_Per_Person = female_players["Price"].sum() / female_count
Other_Avg_Per_Person = other_players["Price"].sum() / other_count

Purchase_Analysis_Gender = pd.DataFrame({"Gender": ['Female','Male','Other/Non-Disclosed'],
                                         "Female":[Female_Purchases,Female_Avg_Price,Female_Avg_Per_Person],
                                         "Male":[Male_Purchases,Male_Avg_Price,Male_Avg_Per_Person],
                                         "Other/NonDisclosed":[Others_Purchases,Others_Avg_Price,Other_Avg_Per_Person]})
#Age Demographics
    
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

DataFrame["AgeBins"] = pd.cut(DataFrame["Age"], age_bins, labels = group_names)

AgePivot = pd.pivot_table(DataFrame, index = 'AgeBins',values = 'SN',
                          aggfunc = lambda x: len(x.unique()))  
AgePivot_2 = pd.pivot_table(DataFrame,index = 'AgeBins', values = 'SN',
                            aggfunc = 'count')

AgePivot_2["Percentage"] = (AgePivot_2["SN"]/AgePivot_2["SN"].count())

AgePivot_2.sort_values(by = 'AgeBins', ascending = True)

#Purchasing Analysis by Age part 2
PurPivot = pd.pivot_table(DataFrame, values = ['SN','Price','Price','Price'])

PurchaseAgePivot_1 = pd.pivot_table(DataFrame, values = ['SN'], index = ['AgeBins'],
                     aggfunc = [np.count_nonzero])

PurchaseAgePivot_2 = pd.pivot_table(DataFrame, values = ['Price'], index = ['AgeBins'],
                     aggfunc = [np.average])

PurchaseAgePivot_3 = pd.pivot_table(DataFrame, values = ['Price'], index = ['AgeBins'],
                     aggfunc = [np.sum])


PurchaseAgePivot_4 = pd.pivot_table(DataFrame, values = ['Price'], index = ['AgeBins'],
                     aggfunc = [np.average])


Purch_Pivot_Combined = pd.concat((PurchaseAgePivot_1, PurchaseAgePivot_2,PurchaseAgePivot_3,PurchaseAgePivot_4), axis=1)
Purch_Pivot_Combined.sort_values(by = 'AgeBins', ascending = True)

#Top Spenders

TopGrouped1 = pd.DataFrame(DataFrame.groupby('SN')['Purchase ID'].nunique())
TopGrouped2 = pd.DataFrame(DataFrame.groupby('SN')['Price'].mean())
TopGrouped3 = pd.DataFrame(DataFrame.groupby('SN')['Price'].sum())
TopGrouped_Combined = pd.concat((TopGrouped1,TopGrouped2,TopGrouped3),axis = 1)
TopGrouped_Combined_Top5 = TopGrouped_Combined.nlargest(5,'Purchase ID')


#Most Popular Items
TopGrouped4 = pd.DataFrame(DataFrame.groupby(['Item ID'])['Purchase ID'].nunique())
TopGrouped4.columns = ['Count of Purchases']
TopGrouped5 = pd.DataFrame(DataFrame.groupby(['Item ID'])['Price'].mean())
TopGrouped5.columns = ['PriceAvg']
TopGrouped6 = pd.DataFrame(DataFrame.groupby(['Item ID'])['Price'].sum())
TopGrouped6.columns = ['Price Sum']

TopGrouped_Combined_Items = pd.concat((TopGrouped4,TopGrouped5,TopGrouped6),axis = 1)

TopGrouped_Combined_Items_Top5 = TopGrouped_Combined_Items.nlargest(5,'Count of Purchases')






#Most Profitable Items
TopGrouped_Combined_Items_Profitable = TopGrouped_Combined_Items.nlargest(5,'Price Sum')







