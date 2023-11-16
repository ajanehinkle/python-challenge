import os
import csv

months = []
profits_losses = []
changes = []

csvpath = os.path.join('Resources','budget_data.csv' )

print("Financial Analysis")
print("--------------")

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        months.append(row[0])
        profits_losses.append(int(row[1]))
    
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
           #print(f'\t{row[0]} profits or losses') - don't need
            line_count += 1
print(f'Total Months: {line_count} ')

def csv_total(brr):
    total = 0
    with open(brr) as a:
        csv_reader = csv.reader(a)
        csv_header = next(csv_reader)

        for line in csv_reader:
            total += int(line[1])
            
    return total
total = csv_total(csvpath)
print(f"Total: ${total}")

    
def csv_total(chill):
    total = 0
    with open(chill) as a:
        csv_reader = csv.reader(a)
        csv_header = next(csv_reader)

    
for i in range (1, len(months)):
        change = profits_losses[i]-profits_losses[i-1]
        changes.append(change)
        
        average_change = sum(changes)/len(changes)

print(f"Average Change is {average_change:.2f}")

def csv_total(ice):
    total = 0
    with open(ice) as a:
        csv_reader = csv.reader(a)
        csv_header = next(csv_reader)

 #Barb did this   
for i in range (1, len(months)):
        change = profits_losses[i]-profits_losses[i-1]
        changes.append(change)
        
        greatest_increase = max(changes)
        greatest_increase_date = months[changes.index(greatest_increase) + 1]

print(f"Greatest Increase in Profits: {greatest_increase_date} ($ {greatest_increase})")

def csv_total(ice):
    total = 0
    with open(ice) as a:
        csv_reader = csv.reader(a)
        csv_header = next(csv_reader)

  
for i in range (1, len(months)):
        change = profits_losses[i]-profits_losses[i-1]
        changes.append(change)
        
        worst_increase = min(changes)
        worst_increase_date = months[changes.index(worst_increase) + 1]

print(f"Biggest Decrease in Profits: {worst_increase_date} (${worst_increase})")

file = open('textpybank.txt', 'w')

file.write('Financial Analysis\n')
file.write('--------------\n')
file.write(f'Total Months: {line_count}\n')
file.write(f'Total: ${total}\n')
file.write(f'Average Change is {average_change:.2f}\n')
file.write(f'Greatest Increase in Profits: {greatest_increase_date} ($ {greatest_increase})\n')
file.write(f'Biggest Decrease in Profits: {worst_increase_date} (${worst_increase})')

file.close()
