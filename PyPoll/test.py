import os
import csv

candidate_list = []
candidate_vote_count = 0
total_votes = 0
percent_won = 0


csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, "r", encoding="utf-8") as csvfile:
    csvDict = csv.DictReader(csvfile)
    for row in csvDict:
        candidate_list.append(row["Candidate"])
        # print(row)

    print(f"{len(set(candidate_list))} candidates")
    
    candidate_stats_dict = {}

    for candidate in set(candidate_list):
        print(f"{candidate} {candidate_list.count(candidate)}")

        candidate_stats_dict[candidate] = [candidate_list.count(candidate)]
        total_votes += candidate_list.count(candidate)
    
    print(total_votes)   
    
    for candidate in set(candidate_list):
        print(f"{(candidate_list.count(candidate) / len(candidate_list)) * 100}")

    
    
    print(total_votes)   

    print(candidate_stats_dict)





