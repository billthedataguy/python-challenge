# William Vann, Homework #3 PyPoll

import csv
import os

    # Relative filepath for csv file 

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, "r", encoding="utf") as csvfile:
   
        # Advance past header row

    csvheader = next(csvfile)

        # <<<Header test>>>
        # print(csvheader) 

    csvreader = csv.reader(csvfile, delimiter=",")
    
    candidate_list = []
    candidate_set = set()

    for row in csvreader:

        candidate_list.append(row[2])

    total_votes = len(candidate_list)
    candidate_set = set(candidate_list)
            
    election_data_dict = {}

        # iterate over candidates sorted alphabetical by first name

    for candidate_name in sorted(candidate_set):

        candidate_vote_total = candidate_list.count(candidate_name)
        candidate_percent_won = round((candidate_vote_total / total_votes) * 100, 3)
        election_data_dict[candidate_name] = [candidate_percent_won, candidate_vote_total]

        # cast dict.values() as list 
    
    percent_won_list = list(election_data_dict.values())
    winner_candidate = ""

        # find winner

    for k,v in election_data_dict.items():
        
        if v == max(percent_won_list):

            winner_candidate = k                               
         
        # Print summary results to terminal

    print(f"Election Results")
    print(f"-------------------------")
        
    print(f"Total Votes: {total_votes}")       
    print(f"-------------------------")
        
    for candidate, (percent_won, candidate_vote_total) in election_data_dict.items():
        
        print(f"{candidate}: {percent_won}% ({candidate_vote_total})")

        # print winner_candidate  
         
    print(f"-------------------------")
    print(f"Winner: {winner_candidate}")
    print(f"-------------------------")
           
        # Print summary results to txt file

        # Relative filepath for txt file (need \n at end of each line for txtfile)
    
    txtpath = os.path.join("analysis", "election_data_csv_analysis.txt")
    
    with open(txtpath, "w", encoding="utf") as txtfile:
        
        txtfile.write(f"Election Results\n")
        txtfile.write(f"-------------------------\n")
        txtfile.write(f"Total Votes: {total_votes}\n")
        txtfile.write(f"-------------------------\n")
    
        for candidate,(percent_won, candidate_vote_total) in election_data_dict.items():

            txtfile.write(f"{candidate}: {percent_won}% ({candidate_vote_total})\n")
                 
        txtfile.write(f"-------------------------\n")      
        txtfile.write(f"Winner: {winner_candidate}\n")
        txtfile.write(f"-------------------------\n")



#####################################################################
######################## DELIVERABLE EXAMPLE ########################
#####################################################################
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
#####################################################################
######################## DELIVERABLE TEMPLATE #######################
#####################################################################
'''
f"Election Results"
f"-------------------------"

    # total_votes = length of candidate_list

f"Total Votes: {total_votes}"       
f"-------------------------"

    # get list of distinct candidate names (use set(candidate_list))
    # candidate_vote_total = count the number of rows in candidate_list for each distinct candidate name
    # percent_won = round((candidate_vote_total / total_votes) * 100, 3)
    
f"{candidate}: {percent_won}% ({candidate_vote_total})"
f"{candidate}: {percent_won}% ({candidate_vote_total})"
f"{candidate}: {percent_won}% ({candidate_vote_total})"
f"-------------------------"

    # winner = candidate name corresponding to max(percent_won) 

f"Winner: {winner_candidate}"
f"-------------------------"

'''
