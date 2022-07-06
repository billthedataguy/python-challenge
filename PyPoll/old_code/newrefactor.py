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
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    print(csv_header)

    for row in csvreader:
        candidate_list.append(row[2])
    
    candidate_set = set(candidate_list)
    
    for candidate in candidate_set: 
        candidate_vote_count = candidate_list.count(candidate)
        total_vote_count = len(candidate_list)
        percent_won = round((candidate_vote_count / total_vote_count) * 100, 3)
        candidate_dict[candidate] = candidate_vote_count
        
        print(f"{candidate} {percent_won}% ({candidate_vote_count})")

    winner = max(candidate_dict, key=candidate_dict.get)

    print(f"Winner: {winner}")







