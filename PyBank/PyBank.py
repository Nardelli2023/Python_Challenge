import os
import csv

# Path to collect data from the Resources folder
current_dir=os.getcwd()
csvpath = os.path.join(current_dir,'Resources','budget_data.csv')

print(current_dir)
print(csvpath)

# Define PyBank's variables
profit = []
monthly_changes = []
date = []

count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Open and read csv

with open (csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    print(csvreader)

    print(next(csvreader))

  # Read through each row of data after the header
    for row in csvreader:    
      # Use count to count the number months in this dataset
      count = count + 1 

      # Will need it when collecting the greatest increase and decrease in profits
      date.append(row[0])

      # Append the profit information & calculate the total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #Calculate the average change in profits from month to month. Then calulate the average change in profits
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      #Store these monthly changes in a list
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      #Calculate the average change in profits
      average_change_profits = (total_change_profits/count)
      
      #Find the max and min change in profits and the corresponding dates these changes were obeserved
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")