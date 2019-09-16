# import csv file
import os

import csv

csvpath = os.path.join('.', 'homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

# open csv file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header
    csv_header = next(csvreader)

    # create variables and set starting values to 0
    sum_revenue = 0
    mom_change = 0
    prev_revenue = 0
    total_rev_chg = 0
    greatest_inc = 0
    greatest_dec = 0
    months = 0

    # iterate over rows to find sum of profit/loss column
    for row in csvreader:
         month_revenue = float(row[1])
         sum_revenue = sum_revenue + month_revenue
         sum_revenue = int(sum_revenue)

         # find each month's change from the previous month, and save a running total
         mom_change = month_revenue - prev_revenue
         total_rev_chg = total_rev_chg + mom_change
         
         # save month's change if it is the greatest increase or greatest decrease, along with corresponding month
         if mom_change > greatest_inc:
            greatest_inc = mom_change
            greatest_inc_name = str(row[0])
         if mom_change <= greatest_dec:
            greatest_dec = mom_change
            greatest_dec_name = str(row[0])

         prev_revenue = month_revenue   
         months = months + 1
    
     # calculate average revenue change
    avg_rev_chg = round(total_rev_chg / months, 2)

     # print out findings in summary table
    print("Financial Analysis\n----------------------------------")
    print(f"Total Months : {str(months)}")
    print(f"Total : ${str(sum_revenue)}")
    print(f"Average Change : ${str(avg_rev_chg)}")
    print(f"Greatest Increase in Profits : {greatest_inc_name} (${str(greatest_inc)})")
    print(f"Greatest Decrease in Profits : {greatest_dec_name} (${str(greatest_dec)})")

# output to text file
text_file = open("financial_summary.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("------------------------\n")
text_file.write("Total Months : " + str(months) + "\n")
text_file.write("Total : $" + str(sum_revenue) + "\n")
text_file.write("Average Change : $" + str(avg_rev_chg) + "\n")
text_file.write("Greatest Increase in Profits: " + str(greatest_inc_name) + " ($" + str(greatest_inc) + ")\n")
text_file.write("Greatest Decrease in Profits: " + str(greatest_dec_name) + " ($" + str(greatest_dec) + ")\n")
text_file.close()
