# William Vann, Homework #3 PyBank, Submission #2 (got the delta average figured out!)

import csv
import os
    
csvpath = os.path.join("Resources", "budget_data.csv")
csvdata = []

with open(csvpath, "r", encoding="utf") as csvfile:
    
        # Advance past header row

    csvheader = next(csvfile)

        # create csvreader object
            
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        csvdata.append([row[0], int(row[1])]) # add month-yr str and profit/loss int to list
       
    new_csv_list = []
    delta = None
        
    for i,list in enumerate(csvdata):   # iterate over list, compute delta value, append to new list
        
        if i==0:
            delta = None
        else:
            try:
                delta = int(csvdata[i][1]) - int(csvdata[i-1][1]) 
            except:
                delta = None
       
        new_csv_list.append([i, list[0], list[1], delta])  # index number, date/yr, profit/loss, delta value

    delta_list = []

    total_months = 0
    total_months = len(new_csv_list)

    earnings_list = []

    for list in new_csv_list:       # iterate over all lists and populate delta_list and earnings_list for computations
        
        if list[3]:       
            delta_list.append(list[3])         

        if list[2]:
            earnings_list.append(int(list[2]))

    total_earnings = 0 
    total_earnings = sum(earnings_list)

    greatest_increase_profits = max(delta_list)
    greatest_decrease_profits = min(delta_list)

    greatest_increase_profits_date = new_csv_list[delta_list.index(greatest_increase_profits)+1][1]     # add 1 to delta_list index for 
    greatest_decrease_profits_date = new_csv_list[delta_list.index(greatest_decrease_profits)+1][1]     #   index in new_csv_list where date/yr
                                                                                                        #   can be retrieved
    average_change = round(sum(delta_list) / len(delta_list), 2)                                        # average of all the delta values
       
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



