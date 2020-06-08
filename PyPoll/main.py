import os
import csv

path = os.path.join("Resources", "election_data.csv")

votelist = list()
candidatelist = list()

with open(path, "r") as inputfile:
    csvinput = csv.reader(inputfile, delimiter = ",")
    header = next(csvinput)

    for row in csvinput:
        voteID = row[0]
        candidate = row[2]

        votelist.append(voteID)
        candidatelist.append(candidate)

writepath = os.path.join("analysis", "analysis.txt")

print("Election Results")
print("---------------------------")

total_vote = len(votelist)
print(f"Total Votes: {total_vote}")
print("---------------------------")

unique_candidate_list = list()

for candidate in candidatelist:
    if candidate not in unique_candidate_list:
        unique_candidate_list.append(candidate)

vote_for_x = 0

for x in unique_candidate_list:
    for y in candidatelist:
        if x == y:
            vote_for_x += 1

    percent_vote = vote_for_x/total_vote*100
    print(f"{x}: {percent_vote:.3f}% ({vote_for_x})")
    vote_for_x = 0

print("---------------------------")



    
