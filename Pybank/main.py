#Import csv data
import os
import csv

csvpath = os.path.join('..', '..', 'Homework', 'python-challenge', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

#Set definitions
total_months = 0
total_profit = 0
prior_profit = 0
months_with_change = []
profitchange = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
average_change = 0

#Calculate total months, net total, profit changes, greatest increase, and greatest decrease.
def data_set(path):
    with open(csvpath) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',')
        header = next(csvreader)
    for row in csvreader:
        yield row

for row in (data_set(csvpath)):
    #calculate total months
    total_months = total_months + 1

    #calculate net total
    total_profit = total_profit + int(row["Profit/Losses"])
    
    #calculate profit changes
    prior_profit = int(row["Profit/Losses"])
    average_change = int(row["Profit/Losses"] - prior_profit)
    profit_change = profit_change - [average_change]

    #Define months with greatest and least change
    months_with_change = months_with_change + [row["Date"]]
    if (average_change > greatest_increase[1]):
        greatest_increase[0] = row["Date"]
        greatest_increase[1] = average_change
    if (average_change < greatest_decrease[1]):
        