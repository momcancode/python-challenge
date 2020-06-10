import os
import csv


def get_summary(file_name):

    path = os.path.join("Resources", file_name)

    month_list = list()
    pl_list = list()
    change_list = list()
    
    with open(path, "r") as inputfile:
        inputcsv = csv.reader(inputfile, delimiter = ",")
        header = next(inputcsv)

        for row in inputcsv:
            month = row[0]
            profit_loss = int(row[1])

            month_list.append(month)
            pl_list.append(profit_loss)

    number_of_months = len(month_list)

    for i in range(1, number_of_months):
        change = pl_list[i] - pl_list[i-1]
        change_list.append(change)

    total = sum(pl_list)

    average_change = round(sum(change_list)/len(change_list),2)

    max_increase = max(change_list)
    indexone = change_list.index(max_increase)
    max_increase_month = month_list[indexone + 1]

    max_decrease = min(change_list)
    indextwo = change_list.index(max_decrease)
    max_decrease_month = month_list[indextwo + 1]

    return ("Financial Analysis",
                "-----------------------------",
                f"Total Months: {number_of_months}",
                f"Total: ${total}",
                f"Average Change: ${average_change}",
                f"Greatest Increase in Profits: {max_increase_month} (${max_increase})",
                f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})"
            )


def print_summary(outcome):
    print(*outcome, sep="\n")


def export_summary(outcome_to_export):
    writepath = os.path.join("analysis", "analysis.txt")
    with open(writepath, "w") as outputfile:
        print(*outcome_to_export, sep="\n", file=outputfile)


summary = get_summary("budget_data.csv")
print_summary(summary)
export_summary(summary)

