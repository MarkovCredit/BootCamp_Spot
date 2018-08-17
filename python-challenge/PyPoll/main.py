# -*- coding: utf-8 -*-
"""


@author: markl

In this challenge, you are tasked with helping a small, rural town modernize its 
vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying 
them one-by-one, but unfortunately, his concentration isn't what it used to be.)

You will be give a set of poll data called election_data.csv. The dataset is 
composed of three columns: Voter ID, County, and Candidate. 

Your task is to create a Python script that analyzes the votes and calculates each of the following:


The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.


As an example, your analysis should look similar to the one below:


  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

"""

import csv as csv
import os as os



#let's check the wd and then set the working directory to where the file is located
os.getcwd()
os.chdir(r'C:\Users\markl\get_testing\UCI-Data-Analytics\python-challenge\PyPoll')
os.getcwd()
#pass the file path to a str object 
csv_path_pypoll = 'election_data.csv'

#create lists to hold items from our for loops
votes_list = []
khan_votes = []
correy_votes = []
li_votes = []
otooley_votes = []



#use with open statement to initialize our reading of the csv
with open(csv_path_pypoll) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    
    #check type of object
    type(csvreader)
    
    #need to iterate over each row to grab the count of votes
    for row in csvreader:
        votes_list.append(row[0])
        if row[2] == "Khan":
            khan_votes.append(row[0])
        elif row[2] == "Correy":
            correy_votes.append(row[0])
        elif row[2] == "Li":
            li_votes.append(row[0])
        else:
            otooley_votes.append(row[0])

#create a votes total object for the total number of votes
votes_total = len(votes_list)

#conversely, we can just add up all the candidate votes to make sure we tie out
total_votes = khan_votes+li_votes+otooley_votes+correy_votes

#long way of calculating percentages; probably a better way to do this with pandas!
khan_percentage = len(khan_votes)/len(total_votes)
correy_percentage = len(correy_votes)/len(total_votes)
li_percentage = len(li_votes)/len(total_votes)    
otooley_percentage = len(otooley_votes)/len(total_votes)


#Create a dictionary with the candidates and their votes
voter_dict = {"Khan": len(khan_votes),
              "Correy": len(correy_votes),
              "Li": len(li_votes),
              "O'Tooley": len(otooley_votes)}

    
#Find the candidate with the most votes (and least for kicks)

Winner_by_pop_vote = max(voter_dict, key = lambda x: voter_dict[x])
Loser_by_pop_vote = min(voter_dict, key = lambda x: voter_dict[x])




#print the statements out
print("Election Results\n")
print("--------------------\n")
print("Total votes:"+ str(len(total_votes)))
print("--------------------\n")
print("Khan:  "+"{:.3%}".format(khan_percentage)+" "+"("+str(len(khan_votes))+")"+"votes")
print("Correy:  "+"{:.3%}".format(correy_percentage)+" "+"("+str(len(correy_votes))+")"+"votes")
print("Li:  "+"{:.3%}".format(li_percentage)+" "+"("+str(len(li_votes))+")"+"votes")
print("O'Tooley:  "+"{:.3%}".format(otooley_percentage)+" "+"("+str(len(otooley_votes))+")"+"votes")
      
print("---------------------\n")

print(f"Winner : {Winner_by_pop_vote} ")

#create an output text file for the output; need to use a new line for each statement
#then close the file. 
output_text_file = open("PyPollOutput2.txt","w")
output_text_file.write("Election Results\n")
output_text_file.write("----------------------\n")
output_text_file.write(str("Total votes:   "+ str(votes_total)+"\n"))
output_text_file.write("----------------------\n")
output_text_file.write("Khan:  "+"{:.3%}".format(khan_percentage)+" "+"("+str(len(khan_votes))+")"+"votes\n")
output_text_file.write("Correy:  "+"{:.3%}".format(correy_percentage)+" "+"("+str(len(correy_votes))+")"+"votes\n")
output_text_file.write("Li:  "+"{:.3%}".format(li_percentage)+" "+"("+str(len(li_votes))+")"+"votes\n")
output_text_file.write("O'Tooley:  "+"{:.3%}".format(otooley_percentage)+" "+"("+str(len(otooley_votes))+")"+"votes\n")
output_text_file.write("---------------------\n")
output_text_file.write("Winner :  "+Winner_by_pop_vote)
output_text_file.close()
    





