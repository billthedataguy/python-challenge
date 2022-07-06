# William Vann, Homework #3 PyPoll

import csv
import os

# Relative filepath for csv file 
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, "r", encoding="utf") as csvfile:

    # Advance past header row
    csvheader = next(csvfile)

    # <<<Header test>>>:
    # print(csvheader) 

    csvreader = csv.reader(csvfile, delimiter=",")









# DELIVERABLE EXAMPLE:

'''
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------

'''

# DELIVERABLE TEMPLATE:

'''
f"Election Results"
f"-------------------------"
f"Total Votes: {total_votes}"
f"-------------------------"
f"{candidate}: {percent_won}% ({candidate_vote_total})"
f"{candidate}: {percent_won}% ({candidate_vote_total})"
f"{candidate}: {percent_won}% ({candidate_vote_total})"
f"-------------------------"
f"Winner: {winner}"
f"-------------------------"

'''