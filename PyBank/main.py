import os
import csv

path = os.path.join("Resources", "budget_data.csv")

month_list = list()
pl_list = list()
change_list = list()

with open(path, "r") as inputfile:
    inputcsv = csv.reader(inputfile, delimiter = ",")
    header = next(inputcsv)

    for row in inputcsv:
        month = row[0]
        profitLoss = int(row[1])

        month_list.append(month)
        pl_list.append(profitLoss)

number_of_months = len(month_list)

for i in range(1, number_of_months):
    change = pl_list[i] - pl_list[i-1]
    change_list.append(change)

total = sum(pl_list)
average_change = round(sum(change_list)/len(change_list),2)
max_increase = max(change_list)
indexone = change_list.index(max_increase)
max_decrease = min(change_list)
indextwo = change_list.index(max_decrease)

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {number_of_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {month_list[indexone + 1]} (${max_increase})")
print(f"Greatest Decrease in Profits: {month_list[indextwo + 1]} (${max_decrease})")

writepath = os.path.join("analysis", "analysis.txt")

with open(writepath, "w") as outputfile:
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {number_of_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {month_list[indexone + 1]} (${max_increase})")
    print(f"Greatest Decrease in Profits: {month_list[indextwo + 1]} (${max_decrease})")