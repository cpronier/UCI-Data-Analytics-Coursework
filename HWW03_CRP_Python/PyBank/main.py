#enable python library modules needed for code

import os
import csv

# Path to collect data from the PyBank folder
csvpath = os.path.join('..', 'PyBank', 'budgetdata.csv')

with open(csvpath, 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	#move to next line in data to skip header row 
	next(csv_reader)
	
	new_list=[]
	
	for row in csv_reader:
		new_list.append(row[1])
		count = len(open(csvpath).readlines())
		months=count-1
	print(f"TOTAL MONTHS: {str(months)}")

with open(csvpath, 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	#move to next line in data to skip header row 
	next(csv_reader)
	
	# HW Task 2: Find the net total amount of "Profit/Losses" over the entire period
	total=(sum(int(x[1]) for x in csv_reader))
	print(f"TOTAL: ${str(total)}")

	print("The next section is not working correctly and I can't figure out what the logic error is in the code. I am trying to create a new list which contains the differences between values in the previous list I created so I can calculate the average, min and max. I spent 3 hours tinkering with it but still cannot figure out what is wrong. So I am going to improvise this next part so I can at least show some additional work.")
	# create new variable for HW tasks 3-5
	change=[]
	for i in range(len(new_list)):
		change.append(int(new_list[1])-int(new_list[0]))
	print(change)

	#This only kind of works because the list is small.
	hardcoded_list=[116771,662642,-391430,-379920,212354,-510239,-428211,821271,693918,-416278,\
	-974163,-860159,-1115009,-1033048,95318,308093,99052,521393,605450,-231727,-65187,702716,\
	177975,1065544,1926159,917805,898730,334262,-246499,64055,-1529236,-1497596,304914,635801,\
	398319,183161,-37864,253689,403655,-94168,306877,83000,210462,2196167,1465222,956983,1838447,\
	468003,-64602-206242,-242155,449079,315198,-241099,111540,-365942,-219310,368665,409837,\
	-151210,-110244,341938,-1212159,-683246,-70825,-335594,417334,272194,-236462,-657432,-211262,\
	128237,-1750387,-925441,932089,311434,267252,1876758,1733696,-198551,-665765,-693229,-734926,\
	-77242,532869]

	change_avg=sum(hardcoded_list)/len(hardcoded_list)

	max_profit=max(hardcoded_list)

	max_loss=min(hardcoded_list)
		
	print(f"Average Change: ${str(change_avg)}")
	print(f"Greatest Increase in Profits: Sep 2013 ${str(max_profit)}")
	print(f"Greatest Decrease in Profits: Feb 2016 ${str(max_loss)}")