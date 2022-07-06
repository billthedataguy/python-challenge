import csv
import os

csvpath = os.path.join("Resources", "election_data.csv")

candidate_list = []
candidate_set = set()
candidate_dict = {}

candidate_vote_count = 0
total_vote_count = 0
percent_won = 0
winner = ""

with open(csvpath, "r", encoding="utf") as csvfile:
    csv_dictreader = csv.DictReader(csvfile)
    # csv_header = next(csvreader)
    # print(csv_header)

    for row in csv_dictreader:
        candidate_list.append(row["Candidate"])
        
    candidate_set = set(candidate_list)

    for c in candidate_set:
        candidate_vote_count = candidate_list.count(c)
        total_vote_count = len(candidate_list)
        candidate_dict[c] = candidate_vote_count
        percent_won = round((candidate_vote_count / total_vote_count) * 100, 3)
        print(f"{c} {percent_won}% {candidate_dict[c]}")


    winner = max(candidate_dict, key=candidate_dict.get)
    print(f"Winner: {winner}")

    print(f"Winner: {[key for key,value in candidate_dict.items() if value == max(candidate_dict.values())][0]}") 
    
    
    
    # sorted(candidate_dict.values(), reverse=True)[0]}") 

