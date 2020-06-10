import os
import csv
import numpy as np



csvpath = os.path.join('Resources', 'budget_data.csv')

count = 0
total = 0 
largest_loss = []
largest_profit = []
placeholder = []
months = []
with open("C:\\Users\\winyi\\OneDrive\\Desktop\\LearnPython\\gt-inc-data-pt-05-2020-u-c\\02-Homework\\03-Python\\Instructions\\PyBank\\Resources\\budget_data.csv") as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        
        count += 1

        total += int(row[1]) 
        current_pl = row[1] 
        months.append(row[0])
        placeholder.append(current_pl)

      
    
    y = [int(s) for s in placeholder] # changes items in whole list into integers
    x = np.array(y)
    profit_loss = (np.diff(x))
    
    avg = np.average(profit_loss)
    c_avg = round(avg, 2)
    
    greatestLoss = profit_loss.min()
    greatestInc = profit_loss.max()
    result = np.where(profit_loss == greatestInc) #returns index number as array
    result_loss = np.where(profit_loss == greatestLoss)
    
    month_max = months[int(result[0])+1] 
    month_loss = months[int(result_loss[0])+1]
    
    data = (
        f"Financial Analysis\n"
        f"---------------------------------\n"
        f"Total Months: {count}\n"
        f"Total Profit/Loss: ${total}\n"
        f"Average Change: $ {c_avg}\n"
        f"Greatest Increase in Profit: {month_max} ${greatestInc}\n"
        f"Greatest Decrease in Profit: {month_loss} ${greatestLoss}\n"
    )

    print(data)

output_path = os.path.join('Resources', 'results.txt')

with open("C:\\Users\\winyi\\OneDrive\\Desktop\\LearnPython\\python_challenge\\PyBank\\Resources\\results.txt", 'w') as newtextfile:
    csvwriter = csv.writer(newtextfile)
    newtextfile.write(data)

    




