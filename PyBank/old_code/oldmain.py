import csv
import os

def formatDollarsCents(amount):
    return (f"${'{:,}'.format(amount)}")

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, "r", encoding="utf") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    profit_loss_total = 0
    
    average_change = 0
    greatest_increase_profits = 0
    greatest_decrease_profits = 0
    greatest_increase_month_year = ""
    greatest_decrease_month_year = ""
    budget_dict = {}

    # Read each row of data after the header
    for i, row in enumerate(csvreader, 1):
        #print(f"{i} {row}")
        budget_dict[row[0]] = int(row[1])

profit_loss_total = sum(budget_dict.values())

greatest_increase_profits = max(budget_dict.values())
greatest_decrease_profits = min(budget_dict.values())

greatest_increase_month_year = [k for k,v in budget_dict.items() if v == greatest_increase_profits][0]
greatest_decrease_month_year = [k for k,v in budget_dict.items() if v == greatest_decrease_profits][0]

moving_averages = []
window_size = 3
i = 0
arr = list(budget_dict.values())
#print(f"ARRAY: {arr}")

while i < len(arr) - window_size + 1:

    window = arr[i : i + window_size]
    window_average = round(sum(window) / window_size, 0)
    moving_averages.append(window_average)
    i += 1

#print(f"MOVING AVERAGES: {moving_averages}")

average_change = round(sum(moving_averages) / len(moving_averages))

txtpath = os.path.join("analysis", "financial_analysis.txt")

with open(txtpath, "w", encoding="utf") as txt_file:

    print("Financial Analysis1")
    txt_file.write("Financial Analysis1\n")
    print("----------------------------")
    txt_file.write("----------------------------\n")

    # The total number of months included in the dataset

    print(f"Total months: {i}")
    txt_file.write(f"Total months: {i}\n")

    # The net total amount of "Profit/Losses" over the entire period

    print(f"Total: {formatDollarsCents(profit_loss_total)}")
    txt_file.write(f"Total: {formatDollarsCents(profit_loss_total)}\n")
   
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes

    print(f"Average Change: {formatDollarsCents(average_change)}")
    txt_file.write(f"Average Change: {formatDollarsCents(average_change)}\n")

    # The greatest increase in profits (date and amount) over the entire period

    print(f"Greatest Increase in Profits: {greatest_increase_month_year} {formatDollarsCents(greatest_increase_profits)}")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month_year} {formatDollarsCents(greatest_increase_profits)}\n")

    # The greatest decrease in profits (date and amount) over the entire period

    print(f"Greatest Decrease in Profits: {greatest_decrease_month_year} {formatDollarsCents(greatest_decrease_profits)}")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month_year} {formatDollarsCents(greatest_decrease_profits)}\n")

'''

REPORT: (1) write to terminal and (2) to write to a txt file

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)


'''



