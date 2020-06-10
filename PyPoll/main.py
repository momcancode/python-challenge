import os
import csv

def get_summary(file_name):

	vote_count = dict()
	vote_percent = dict()
	summarylist = list()
	max_vote = 0

	path = os.path.join("Resources", file_name)

	with open(path, "r") as inputfile:
		csvinput = csv.reader(inputfile, delimiter = ",")
		header = next(csvinput)

		for row in csvinput:
			candidate = row[2]

			if candidate not in vote_count:
				vote_count[candidate] = 1
			else:
				vote_count[candidate] += 1

	total_vote = sum(vote_count.values())

	# Loop through each candidate name key in vote_count dictionary
	for key in vote_count:
		vote_percent[key] = vote_count[key]/total_vote*100	
		
		summary_element = f"{key}: {vote_percent[key]:.3f}% ({vote_count[key]})"
		summarylist.append(summary_element)
		summarylist_print = "\n".join(summarylist)

		if vote_percent[key] > max_vote:
			max_vote = vote_percent[key]
			election_winner = key
		
	return (
		"Election Results",
		"---------------------------",
		f"Total Votes: {total_vote}",
		"---------------------------",
		summarylist_print,
		"---------------------------",
		f"Winner: {election_winner}",
		"---------------------------"
	)

def print_summary(outcome):
    print(*outcome, sep="\n")


def export_summary(outcome_to_export):
    writepath = os.path.join("analysis", "analysis.txt")
    with open(writepath, "w") as outputfile:
        print(*outcome_to_export, sep="\n", file=outputfile)


summary = get_summary("election_data.csv")
print_summary(summary)
export_summary(summary)