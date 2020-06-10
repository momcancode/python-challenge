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

total_vote = len(votelist)

unique_candidate_list = list()

for candidate in candidatelist:
    if candidate not in unique_candidate_list:
        unique_candidate_list.append(candidate)

vote_each_won = list()
vote_for_x = 0

for x in unique_candidate_list:
    for y in candidatelist:
        if x == y:
            vote_for_x += 1

    vote_each_won.append(vote_for_x)
    vote_for_x = 0

percent_votes = [each/total_vote*100 for each in vote_each_won]

max_votes = max(vote_each_won)
winner_index = vote_each_won.index(max_votes)
winner = unique_candidate_list[winner_index]

summary = zip(unique_candidate_list, percent_votes, vote_each_won)

summarylist = list()
for element in summary:
    summaryelement = f"{element[0]}: {element[1]:.3f}% ({element[2]})"
    summarylist.append(summaryelement)

text = "\n".join(summarylist)

finalresult = (
    "Election Results",
    "---------------------------",
    f"Total Votes: {total_vote}",
    "---------------------------",
    text,
    "---------------------------",
    f"Winner: {winner}",
    "---------------------------"
)

print("\n".join(finalresult))


writepath = os.path.join("analysis", "analysis.txt")

with open(writepath, "w") as outputfile:
    print("\n".join(finalresult), file= outputfile)
