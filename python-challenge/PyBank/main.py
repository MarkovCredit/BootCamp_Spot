# -*- coding: utf-8 -*-
"""

@author: markl
"""

#PyBank

"""Instructions:
    After creating the repo (python-challenge) and then
the PyBank directory with the main.py file, solve the following:
    
  In this challenge, you are tasked with creating a Python script for analyzing 
  the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to 
calculate each of the following:


The total number of months included in the dataset
The total net amount of "Profit/Losses" over the entire period
The average change in "Profit/Losses" between months over the entire period
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in losses (date and amount) over the entire period


As an example, your analysis should look similar to the one below:


  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)

In addition, your final script should both print the analysis to the terminal and export a text file with the results.  """


#First let's load in some modules/libraries

import csv as csv
import os as os

#let's check the wd and then set the working directory to where the file is located
os.getcwd()
os.chdir('C:\\Users\markl\PyBank')
os.getcwd()

#need to create empty list objects to put monthly revenues and months into
#also need a list to hold a list for monthly changes (n-1 length)
revenue_list = []
months_list = []
monthly_rev_change_list = []

#pass the file path to a str object;
csv_path_pybank = 'budget_data.csv'

#use with open statement to initialize our reading of the csv
with open(csv_path_pybank) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    
    #check type of object
    type(csvreader)
    
    #need to iterate over each row to grab rev and dates; 
    for row in csvreader:
        revenue_list.append(int(row[1]))
        months_list.append(row[0])

#lets store a total revenues object for later use
total_revenues = sum(revenue_list)
#now we need to start at the 1st index position (second actual row) and subtract the value
#from the preceding row. we set the range from 1 to length of revenue list since we skip
#the first row as there is no change from this position
#

    for i in range(1,len(revenue_list)):
        monthly_rev_change_list.append(revenue_list[i] - revenue_list[i-1])

#compute the average revenue change by summing all the monthly changes and dividing
#by the length
        
        
avg_rev_change = sum(monthly_rev_change_list) / len(monthly_rev_change_list)


#find max and min values
max_rev_change = max(monthly_rev_change_list)
min_rev_change = min(monthly_rev_change_list)
#using indexing and .index function, find the month of each max and min
max_rev_change_date = months_list[monthly_rev_change_list.index(max(monthly_rev_change_list))]
min_rev_change_date = months_list[monthly_rev_change_list.index(min(monthly_rev_change_list))]

#print necessary items to the console>      
print("Financial_Analysis\n")
print("---------------------------\n")
print("There are "+ str(len(months_list))+" months in the budget\n")
print("Total Revenues of $",'{:,}'.format(sum(revenue_list)))        
print("The average revenue change was $",'{:,}'.format(avg_rev_change))
print("The maximum change in revenue was $", '{:,}'.format(max_rev_change),"occuring during",max_rev_change_date)
print("The minimum change in revenue was $", '{:,}'.format(min_rev_change),"occuring during",min_rev_change_date)

#create an output text file for the output; need to use a new line for each statement
#then close the file
output_text_file = open("PyBankOutput.txt","w")
output_text_file.write("Financial_Analysis\n")
output_text_file.write("----------------------\n")

output_text_file.write(str("There are "+ str(len(months_list))+" months in the budget\n"))
output_text_file.write(f"Total Revenues of ${total_revenues}.\n" )
output_text_file.write(f"The average revenue change was $ {avg_rev_change} per month.\n")
output_text_file.write(f"The maximum change in revenue was ${max_rev_change} occuring during {max_rev_change_date}\n")
output_text_file.write(f"The minimum change in revenue was ${min_rev_change} occuring during {min_rev_change_date}\n")

output_text_file.close()

