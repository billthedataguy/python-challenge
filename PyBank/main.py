# William Vann, Homework #3 PyBank

import csv
import os

    # Relative filepath for csv file 

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, "r", encoding="utf") as csvfile:
    
        # Advance past header row

    csvheader = next(csvfile)

        # <<<Header test>>>:
        # print(csvheader) 

    csvreader = csv.reader(csvfile, delimiter=",")

        # Initialize list for dates values, list for earnings values

    dates_list = []
    earnings_list = []

        # Iterate over rows in csvreader object

    for row in csvreader:

            # Append values to their respective lists, casting ints for earnings values

        dates_list.append(row[0])
        earnings_list.append(int(row[1]))
    
        # Run calculations and fetch dates

    total_months = len(dates_list)
    total_earnings = sum(earnings_list)

    greatest_increase_profits = max(earnings_list)
    greatest_decrease_profits = min(earnings_list)

    greatest_increase_profits_date = dates_list[earnings_list.index(greatest_increase_profits)]
    greatest_decrease_profits_date = dates_list[earnings_list.index(greatest_decrease_profits)] 
    
        # Initialize list for moving averages

    moving_averages_list = []

        # Make sure we have correct start and end earning values 

    start = earnings_list[0]
    end = earnings_list[len(earnings_list)-1]

        # <<<Start / End Test>>>: 
        # print(f"Start: {start}")
        # print(f"End: {end}")
        
        # Set moving average window size and initialize counter

    window_size = 3
    i = 0
    
        # Iterate through all 3 pane "windows" in earnings list
        # Calculate moving average for each window
        # Write moving average to moving averages list
        # (NB: I found the following logic here: 
        # https://www.geeksforgeeks.org/how-to-calculate-moving-averages-in-python/)

    while i < (len(earnings_list) - window_size + 1): 

        window = earnings_list[i : i + window_size]
        average = round(sum(window) / window_size, 2)
        moving_averages_list.append(average)
        i += 1
    
        # Calculate average change of moving averages

    average_change = round(sum(moving_averages_list) / len(moving_averages_list), 2)
    
        # Print summary results to terminal

    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {len(dates_list)}")
    print(f"Total: ${sum(earnings_list)}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_profits_date} (${max(earnings_list)})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_profits_date} (${min(earnings_list)})")
    
        # Print summary results to txt file

        # Relative filepath for txt file (need \n at end of each line for txtfile)
        
    txtpath = os.path.join("analysis", "budget_data_csv_financial_analysis.txt")
    
    with open(txtpath, "w", encoding="utf") as txtfile:

        txtfile.write(f"Financial Analysis\n")
        txtfile.write(f"----------------------------\n")
        txtfile.write(f"Total Months: {len(dates_list)}\n")
        txtfile.write(f"Total: ${sum(earnings_list)}\n")
        txtfile.write(f"Average Change: ${average_change}\n")
        txtfile.write(f"Greatest Increase in Profits: {greatest_increase_profits_date} (${max(earnings_list)})\n")
        txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_profits_date} (${min(earnings_list)})\n")



#####################################################################
######################## DELIVERABLE EXAMPLE ########################
#####################################################################

'''

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

'''

#####################################################################
######################## DELIVERABLE TEMPLATE #######################
#####################################################################

'''

f"Financial Analysis"
f"----------------------------"
f"Total Months: {total_months}"       # get length of months_list
f"Total: $ {total_earnings}"          # get sum of earnings_list
f"Average Change: $ {average_change}" # average of moving average list elements with "window" size = 3

    # get max of earnings list and fetch corresponding date 

f"Greatest Increase in Profits: {greatest_increase_profits_date} (${greatest_increase_profits})"  

    # get min of earnings list and fetch corresponding date 
    
f"Greatest Decrease in Profits: {greatest_decrease_profits_date} (${greatest_decrease_profits})"  

'''