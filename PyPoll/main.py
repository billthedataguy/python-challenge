import csv
from hashlib import new
import os

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, "r", encoding="utf") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # print(f"HEADER: {csv_header}")
    
    election_dict = {}
    candidates = set()
    ballotIDlist = []
    
    for row in csvreader:
        election_dict[row[0]] = row[2]
        

    candidates = {v for k,v in election_dict.items()}
    total_votes = len(election_dict.keys())

    txtpath = os.path.join("analysis", "analysis.txt")

    with open(txtpath, "w", encoding="utf") as txt_file:
    
        print("Election Results")
        txt_file.write("Election Results\n")

        print("-------------------------")
        txt_file.write("-------------------------\n")

        print(f"Total Votes: {total_votes}")
        txt_file.write(f"Total Votes: {total_votes}\n")

        print("-------------------------")
        txt_file.write("-------------------------\n")

        new_election_dict = {}
        vote_tote = 0
        percent_won = 0
        winner = ""

        for candidate in sorted(candidates):

            cand_vote_tot = len([int(k) for k,v in election_dict.items() if v == candidate])
            new_election_dict[candidate] = cand_vote_tot
            percent_won = (cand_vote_tot / total_votes) * 100
            vote_tote += cand_vote_tot

            print(f"{candidate}: {round(percent_won, 3)}% ({cand_vote_tot})")
            txt_file.write(f"{candidate}: {round(percent_won, 3)}% ({cand_vote_tot})\n")


        print("-------------------------")
        txt_file.write("-------------------------\n")
        
        
    # The total number of votes cast

        for k,v in new_election_dict.items():
            if v == max(new_election_dict.values()):
                winner = k
                print(f"Winner: {k}")
                txt_file.write(f"Winner: {k}\n")

        print("-------------------------")
        txt_file.write("-------------------------\n")

        # Election Results
        # -------------------------
        # Total Votes: 369711
        # -------------------------
        # Charles Casper Stockham: 23.049% (85213)
        # Diana DeGette: 73.812% (272892)
        # Raymon Anthony Doane: 3.139% (11606)
        # -------------------------
        # Winner: Diana DeGette
        # -------------------------