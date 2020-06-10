import os
import csv

# Define function to get the analysis from a file whose name is its sole parameter
def get_summary(file_name):

	# Declare dictionaries to hold percentages & numbers of votes each candidate won
	# Declare a list to hold the analysis results and add new lines
	# Declare a variable to hold winner's number of votes, starting at 0
	vote_count = dict()
	vote_percent = dict()
	summarylist = list()
	max_vote = 0

	# Path to collect data from the Resources folder
	path = os.path.join("Resources", file_name)

	# Open and read the csv file, skip the header row
	with open(path, "r") as inputfile:
		csvinput = csv.reader(inputfile, delimiter = ",")
		header = next(csvinput)

		# Loop through each row in the input file
		for row in csvinput:
			candidate = row[2]

			# If a candidate name is not found as a key in vote_count dictionary,
			# add the candidate name as key and the number of votes won as value starting at 1
			# Each time a candidate name is found as key in the vote_count dictionary,
			# 1 is added to the number of votes
			if candidate not in vote_count:
				vote_count[candidate] = 1
			else:
				vote_count[candidate] += 1

	# Find the total number of votes cast
	total_vote = sum(vote_count.values())

	# Loop through each candidate name key in vote_count dictionary
	# Calculate the percentage of votes each candidate won
	for key in vote_count:
		vote_percent[key] = vote_count[key]/total_vote*100	
		
		# Concatenate a complete list of candidates who received votes,
		# the percentage and total number of votes each candidate won
		summary_element = f"{key}: {vote_percent[key]:.3f}% ({vote_count[key]})"
		summarylist.append(summary_element)
		summarylist_print = "\n".join(summarylist)

		# Find the winner of the election based on popular vote
		if vote_count[key] > max_vote:
			max_vote = vote_count[key]
			election_winner = key

	# Return the required summary analysis	
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

# Define function to print the results to the terminal
def print_summary(outcome):
    print(*outcome, sep="\n")

# Define function to print the results to a text file
def export_summary(outcome_to_export):
    writepath = os.path.join("analysis", "analysis.txt")
    with open(writepath, "w") as outputfile:
        print(*outcome_to_export, sep="\n", file=outputfile)

# Called the functions to print the analysis to the terminal and text file
summary = get_summary("election_data.csv")
print_summary(summary)
export_summary(summary)