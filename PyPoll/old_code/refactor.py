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
        percent_won = (candidate_vote_count / total_vote_count) * 100
        candidate_dict[candidate] = percent_won
        # print(f"dict.values : {candidate_dict.values()}")
        
        print(f"{candidate} {round(percent_won, 3)}% ({candidate_vote_count})")
    
    winner = max(candidate_dict, key=candidate_dict.get)
    # winner = [k for k in candidate_dict.keys() if candidate_dict[k] == max(candidate_dict.values())][0]
    max_keys = [key for key, value in candidate_dict.items() if value == max(candidate_dict.values())]

    print(f"{total_vote_count} total votes")
    print(f"Winner: {winner} {max_keys}")

    