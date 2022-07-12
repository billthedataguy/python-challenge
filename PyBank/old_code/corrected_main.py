
# William Vann, Homework #3 PyBank

import csv
from doctest import master
import os

    # Relative filepath for csv file 

csvpath = os.path.join("Resources", "budget_data.csv")

my_list = []

with open(csvpath, "r", encoding="utf") as csvfile:
    
        # Advance past header row

    csvheader = next(csvfile)

        # <<<Header test>>>:
        # print(csvheader) 

    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
              
        my_list.append(row)
   
    master_list = list(my_list)

    new_master_list = []
        
    for i,list in enumerate(master_list):
        
        if i==0:
            delta = None
        else:
            try:
                delta = int(master_list[i][1]) - int(master_list[i-1][1]) 
            except:
                delta = None


       
        new_master_list.append([i, list[0], list[1], delta])

    delta_list = []

    total_months = 0

    total_months = len(new_master_list)

    earnings_list = []

    for list in new_master_list:
        # print(list)
        if list[3]:
            delta_list.append(list[3])

        if list[2]:
            earnings_list.append(int(list[2]))

    total_earnings = 0 

    total_earnings = sum(earnings_list)

    greatest_increase_profits = max(delta_list)
    greatest_decrease_profits = min(delta_list)

    greatest_increase_profits_date = new_master_list[delta_list.index(greatest_increase_profits)+1][1]
    greatest_decrease_profits_date = new_master_list[delta_list.index(greatest_decrease_profits)+1][1]

        
    # print(greatest_increase_profits, greatest_increase_profits_date)
    # print(greatest_decrease_profits, greatest_decrease_profits_date)

    average_change = round(sum(delta_list) / len(delta_list), 2)
    # print(average_change)
       
       # Print summary results to terminal

    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_earnings}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_profits_date} (${greatest_increase_profits})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_profits_date} (${greatest_decrease_profits})")
    
        # Print summary results to txt file

        # Relative filepath for txt file (need \n at end of each line for txtfile)
        
    txtpath = os.path.join("analysis", "budget_data_csv_financial_analysis.txt")
    
    with open(txtpath, "w", encoding="utf") as txtfile:

        txtfile.write(f"Financial Analysis\n")
        txtfile.write(f"----------------------------\n")
        txtfile.write(f"Total Months: {total_months}\n")
        txtfile.write(f"Total: ${total_earnings}\n")
        txtfile.write(f"Average Change: ${average_change}\n")
        txtfile.write(f"Greatest Increase in Profits: {greatest_increase_profits_date} (${greatest_increase_profits})\n")
        txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_profits_date} (${greatest_decrease_profits})\n")



