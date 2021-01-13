#import csv 
import os
import csv
import collections
from collections import Counter

os.chdir(os.path.dirname(__file__))
election_data_csv_path = os.path.join("Resources", "election_data.csv")

#Set defintions
candidates = []
votes_per = []

with open(election_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"CSV Header: {csv_header}")

    for row in csv_reader:
        candidates.append(row[2])

    #create a sorted list for candidates
    sorted_list = sorted(candidates)
    arrange_list = sorted_list

    #count candidates using counter
    total_candidates= collections.Counter(arrange_list)
    votes_per.append(total_candidates.most_common())

    #generate percentage of votes for each candidate
    for item in votes_per:
        candidate_one = format((item[0][1])*100/(sum(total_candidates.values())),'.3f')
        candidate_two = format((item[1][1])*100/(sum(total_candidates.values())),'.3f')
        candidate_three = format((item[2][1])*100/(sum(total_candidates.values())),'.3f')
        candidate_four = format((item[3][1])*100/(sum(total_candidates.values())),'.3f')

#Print the analysis for the terminal

print("Election Results")
print("--------------------------------")
print("Total Votes")
print("--------------------------------")




print("--------------------------------")
print("Winner")
print("--------------------------------")
