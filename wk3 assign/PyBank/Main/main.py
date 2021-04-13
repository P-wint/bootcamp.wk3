#import dependencies

import os
csvpath = os.path.join('..', 'Resources','budget_data.csv')

import csv
with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	
	#print(csvreader)
	header = next(csvreader)	
	#print(header)	
	#print(header[0],header[1])

# - Define Variables		
	total_months = 0	
	total_Profit = 0
	average_change = 0		
	giip = 0
	temp_giip = 0	
	gdip = 0
	line_count = 0
	current_num = 0
	previous_num = 0
	running_sum = 0
	total_running_sum = 0
	First_Ext = 867884
	str_giip_date = ""
	str_gdip_date = ""

# - Loop through each row in file	
	for row in csvreader:
		line_count += 1		
		#print(row[1])		
		total_months += 1				
		total_Profit += int(row[1])

		current_num = int(row[1])
		running_sum = previous_num - current_num 
		print('Running sum = ', int(running_sum))
		print('int(row[1])', int(row[1]))
		previous_num = current_num
		print('Previous-Num b4 loop', int(previous_num))
		total_running_sum = total_running_sum  + running_sum
		print('Total Running Sum', int(total_running_sum))

#Greatest increase and decrease
		if running_sum < 0: 
			temp_giip = int(running_sum * -1)
			if temp_giip > giip:
				giip = temp_giip
				str_giip_date = row[0]

		if running_sum > 0: 
			temp_giip = int(running_sum * -1)
			if temp_giip < gdip:
				gdip = temp_giip
				str_gdip_date = row[0]

#============================================Write to Screen	
print(' ')	
print(' ')	
print(' ')	
print('Financial Analysis')	
print('--------------------')	
print(' ')	
print('Total Months: ', int(total_months))	
print('Total Profit/Loss: $', int(total_Profit))

print('Total Running Sum:  ', int(total_running_sum))
total_running_sum  = int(total_running_sum) * -1
print('running sum:  ', int(running_sum))
print('total running sum:  ', int(total_running_sum - First_Ext))	
print('Average  Change: ', float(total_running_sum - First_Ext)  / (total_months - 1))
	
print('Greatest Increase in Profits: ', str_giip_date, int(giip))	
print('Greatest Decrease in Profits: ', str_gdip_date, int(gdip)) 
print(f'Processed {line_count} lines.')

#=============================================Write to text File
fb = open('Analysis/Financial_Analysis.txt', 'w')

strWrite = ""
fb.write("\n")
fb.write('Financial Analysis \n')	
fb.write('-------------------- \n')	

strWrite = " "
strWrite = 'Total Months: ' + str(int(total_months))
fb.write(strWrite)
fb.write("\n")
strWrite = " "
strWrite = 'Total Profit/Loss: $' + str(int(total_Profit))
fb.write(strWrite)
fb.write("\n")
strWrite = ""

strWrite ="Average  Change: ", float(total_running_sum - First_Ext)  / (total_months - 1)
fb.write(str(strWrite))
fb.write("\n")

strWrite = "Greatest Increase in Profits: ", str_giip_date, int(giip) 
fb.write(str(strWrite))
fb.write("\n")

strWrite = "Greatest Decrease in Profits: ", str_gdip_date, int(gdip)
fb.write(str(strWrite))
fb.write("\n")
fb.close()
