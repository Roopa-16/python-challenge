import os
import csv

budgetData = os.path.join("budget_data.csv")

totalMonths = 0
totalProfitlosses = 0
value = 0
changes = 0
date = []
profit = []

with open(budgetData, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)

    firstRow = next(csvreader)
    totalMonths += 1
    totalProfitlosses += int(firstRow[1])
    value = int(firstRow[1])
    
    for row in csvreader:
        date.append(row[0])
        changes = int(row[1])-value
        profit.append(changes)
        value = int(row[1])
        totalMonths += 1
        totalProfitlosses = totalProfitlosses + int(row[1])

    greatestIncrease = max(profit)
    greatestIndex = profit.index(greatestIncrease)
    greatestDate = date[greatestIndex]

    greatestDecrease = min(profit)
    greatestDecreaseindex = profit.index(greatestDecrease)
    greatestDecreasedate = date[greatestDecreaseindex]

    averageChange = sum(profit)/len(profit)
    

print("Financial Analysis")
print("---------------------------------------------------")
print(f"Total Months: {str(totalMonths)}")
print(f"Total: ${str(totalProfitlosses)}")
print(f"Average Change: ${str(round(averageChange,2))}")
print(f"Greatest Increase in Profits: {greatestDate} (${str(greatestIncrease)})")
print(f"Greatest Decrease in Profits: {greatestDecreasedate} (${str(greatestDecrease)})")

output = open("output.txt", "w")
line1 = "Financial Analysis"
line2 = "---------------------------------------------------"
line3 = str(f"Total Months: {str(totalMonths)}")
line4 = str(f"Total: ${str(totalProfitlosses)}")
line5 = str(f"Average Change: ${str(round(averageChange,2))}")
line6 = str(f"Greatest Increase in Profits: {greatestDate} (${str(greatestIncrease)})")
line7 = str(f"Greatest Decrease in Profits: {greatestDecreasedate} (${str(greatestDecrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))