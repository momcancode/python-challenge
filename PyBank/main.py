import os
import csv

# Define function to get the analysis from a file whose name is its sole parameter
def get_summary(file_name):

    # Path to collect data from the Resources folder
    path = os.path.join("Resources", file_name)

    # Declare lists to hold months, amounts of profits/losses, and changes in profits/losses
    month_list = list()
    pl_list = list()
    change_list = list()
    
    # Open and read the csv file, skip the header row
    with open(path, "r") as inputfile:
        inputcsv = csv.reader(inputfile, delimiter = ",")
        header = next(inputcsv)

        # Loop through each row in the input file
        for row in inputcsv:
            month = row[0]
            profit_loss = int(row[1])

            month_list.append(month)
            pl_list.append(profit_loss)

    # Find the total number of months in the dataset
    number_of_months = len(month_list)

    # Loop through the profit/loss list to calculate the changes
    for i in range(1, number_of_months):
        change = pl_list[i] - pl_list[i-1]
        change_list.append(change)

    # Find the net total amount of profit/losses over the entire period
    total = sum(pl_list)

    # Find the average of the changes in profit/losses over the entire period
    average_change = round(sum(change_list)/len(change_list),2)

    # Find the greatest increase in profits (date and amount) over the entire period
    max_increase = max(change_list)
    indexone = change_list.index(max_increase)
    max_increase_month = month_list[indexone + 1]

    # Find the greatest decrease in profits (date and amount) over the entire period
    max_decrease = min(change_list)
    indextwo = change_list.index(max_decrease)
    max_decrease_month = month_list[indextwo + 1]

    # Return the required summary analysis
    return (
        "Financial Analysis",
        "-----------------------------",
        f"Total Months: {number_of_months}",
        f"Total: ${total}",
        f"Average Change: ${average_change}",
        f"Greatest Increase in Profits: {max_increase_month} (${max_increase})",
        f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})"
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
summary = get_summary("budget_data.csv")
print_summary(summary)
export_summary(summary)

