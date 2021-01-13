#Import csv data
import os
import csv

csvpath = os.path.join('..', '..', 'Homework', 'python-challenge', 'budget_data.csv')

#Set Definitions
total_months = []
total_profit_changes = []
count_months = 0
total_profits_losses = 0
previous_loss_gain = 0
current_loss_gain = 0
profit_change = 0

#open and read csvfile
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

        #Count total months
        count_months += 1

        #Calculate net total of profits/losses
        current_loss_gain = int(row[1])
        total_profits_losses += current_loss_gain

        if (count_months == 1):
            previous_loss_gain = current_loss_gain
            continue

        else:
            profit_change = current_loss_gain - previous_loss_gain

            #Append Month and Profit data
            total_months.append(row[0])
            total_profit_changes.append(profit_change)

            #Prepare loss data for next loop
            previous_loss_gain = current_loss_gain

    #Total and average figures for profits/losses
    profit_changes_sum = sum(total_profit_changes)
    profit_changes_average = round(profit_changes_sum/(count_months - 1), 2)

    #Generate greatest increase and decrease of profits/losses
    profit_increase = max(total_profit_changes)
    loss_decrease = min(total_profit_changes)

    #Pull index information for profit max and min increase/decrease data, then assign to their given months.
    greatest_increase_index = total_profit_changes.index(profit_increase)
    greatest_decrease_index = total_profit_changes.index(loss_decrease)
    month_maximum_increase = total_months[greatest_increase_index]
    month_maximum_decrease = total_months[greatest_decrease_index]

    #Print Financial Analysis
    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {count_months}")
    print(f"Total: ${total_profits_losses}")
    print(f"Average Change: ${profit_changes_average}")
    print(f"Greatest Increase In Profits: {month_maximum_increase} ${profit_increase}")
    print(f"Greatest Decrease In Losses: {month_maximum_decrease} ${loss_decrease}")
