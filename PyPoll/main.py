# import csv file
import os
import csv

election_csv = os.path.join('.', 'election_data.csv')

# open csv file
with open(election_csv, newline='') as csvfile: 

    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    csvheader = next(csvreader)
    
    # create variables and set to zero, create list for candidates and dictionary for candidates & votes
    ttl_votes = 0 
    candidates = []
    candidate_votes = {}
    winning_votes = 0

    # iterate over rows to find total number of votes
    for row in csvreader:
        ttl_votes = ttl_votes + 1

        candidate = row[2]
        
        # add candidates into candidate list if not already there, and set vote count to zero
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        # add row's vote to candidate vote counter
        candidate_votes[candidate] = candidate_votes[candidate] + 1

    # get total votes for each candidate
    for candidate, votes in candidate_votes.items(): 
        votes = candidate_votes.get(candidate)

        # find winning number of votes and corresponding candidate
        if votes > winning_votes:
            winning_votes = votes
            winning_candidate = candidate

    # print election results
    print("Election Results\n------------------------")
    print(f"Total Votes : {str(ttl_votes)}")
    print("------------------------")
    for candidate, votes in candidate_votes.items():
        print(f"{candidate} : {round(votes / ttl_votes * 100, 2)}% ({votes})")
    print("------------------------")
    print(f"Winner : {winning_candidate}")
    print("------------------------")

# output to text file
text_file = open("polling_summary.txt", "w")
text_file.write("Election Results\n")
text_file.write("------------------------\n")
text_file.write(f"Total Votes : {str(ttl_votes)}\n")
text_file.write("------------------------\n")
for candidate, votes in candidate_votes.items():
    text_file.write(f"{candidate} : {round(votes / ttl_votes * 100, 2)}% ({votes})\n")
text_file.write("------------------------\n")
text_file.write(f"Winner : {winning_candidate}\n")
text_file.write("------------------------\n")
text_file.close()
