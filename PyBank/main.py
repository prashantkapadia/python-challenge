import os
import csv

csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    

   # print(csvreader)
    print("-------------------")
    print("Financial Analysis ")
    print("-------------------")

    num_rows = 0
    total = 0
    maxnumber = 0
    mxdt = " "
    mndt = " "
    minnumber = 0
    oldval = 867884
    newval = 0
    chgVal = []
    for row in csvreader:
#counting total months and total amount.

        num_rows += 1
        total = total + int(row[1])
    
# Max value calculation
        if maxnumber < int(row[1]):
            maxnumber = int(row[1])
            mxdt = row[0]
# Min value calculation
        if minnumber > int(row[1]):
            minnumber = int(row[1])
            mndt = row[0]
        
        if oldval != int(row[1]):
            newval = int(row[1]) - oldval
            oldval = int(row[1])
            chgVal.append(newval)

# Calculating Average change

avg_sum = 0
avg_chg = 0
for num in chgVal:

    avg_sum += num


avg_chg = round(avg_sum/len(chgVal),2)

# to find average

print("Total Months : " + str(num_rows))
print( "Total : " + str(total))
print(f"Average Change : {avg_chg} ")
print(f"Greatest Increase in Profits : {mxdt} {maxnumber}")
print(f"Greatest Decrease in Profits : {mndt} {minnumber}")


with open ('PyBank-analysis.txt', 'w+') as writer:
    writer.write(f"Total Months : {str(num_rows)}\n")
    writer.write(f"Total : {str(total)}\n")
    writer.write(f"Average Change : {avg_chg} \n")
    writer.write(f"Greatest Increase in Profits : {mxdt} {maxnumber}\n")
    writer.write(f"Greatest Decrease in Profits : {mndt} {minnumber}\n")
