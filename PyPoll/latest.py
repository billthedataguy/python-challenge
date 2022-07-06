import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, "r", encoding="utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    data = list(csvreader)
    candidates = []

    for each_list in data:
        candidates.append(each_list[2])

    total = len(candidates)

    print(f"TOTAL: {total}")
   
    results_list = []

    for candidate in set(candidates):
        count = candidates.count(candidate)
        percent = (count / total) * 100
        results_list.append((percent, count, candidate))
        print(f"{candidate} {count} {round(percent, 3)}%")

    winner = max(results_list, key=lambda x: x[0])
    loser = min(results_list, key=lambda x: x[0])
    print(f"Winner: {winner}")
    print(f"Loser: {loser}")
