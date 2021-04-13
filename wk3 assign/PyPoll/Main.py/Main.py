#import dependencies
import os
import csv

# - Read in file
csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath, newline = '') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter = ',')
	
	#print(csvreader)
	header = next(csvreader)

	#print(header[0], header[1])
	#print(header[0],header[1])

# - Define Variables
		
	cand1 = ""
	cand1_total_votes = 0.0
	cand1_pctg = 0.0

	cand2 = ""
	cand2_total_votes = 0.0
	cand2_pctg = 0.0

	cand3 = ""
	cand3_total_votes = 0
	cand3_pctg = 0

	cand4 = ""
	cand4_total_votes = 0.0
	cand4_pctg = 0.0

	total_votes = 0
	winner = ""
	winner_Votes = 0

# - Loop through each row in file
	#candidates = int(row[2][2])

	for row in csvreader:
		total_votes += 1
				

		if str(row[2]) == 'Khan':
			cand1 = str(row[2])
			cand1_total_votes += 1
			
		if str(row[2]) == 'Correy':
			cand2 = str(row[2])
			cand2_total_votes += 1
			
		if str(row[2]) == 'Li':
			cand3 = str(row[2])
			cand3_total_votes += 1

		if str(row[2]) == "O'Tooley":
			cand4 = str(row[2])
			cand4_total_votes += 1
			
# - Calculate winner
	winner = cand1
	winner_votes = cand1_total_votes 
	if cand2_total_votes > winner_votes :
		winner = cand2
	elif cand3_total_votes > winner_votes :
		winner = cand3
	elif cand3_total_votes > winner_votes :
		winner = cand4

# - Print output to screen
print('\n\nElection Results:')
print('-----------------------------')
print('Total Votes:  ', int(total_votes))
print('-----------------------------\n')
print(cand1, ':  ', round(float(cand1_total_votes / total_votes), 2) * 100, '%', '\t', '(',int(cand1_total_votes),')')
print(cand2, ':  ', round(float(cand2_total_votes / total_votes), 2) * 100, '%', '\t', '(',int(cand2_total_votes),')')
print(cand3, ':  ', round(float(cand3_total_votes / total_votes), 2) * 100, '%', '\t','(',int(cand3_total_votes),')')
print(cand4, ':  ', round(float(cand4_total_votes / total_votes), 2) * 100, '%','\t', '(',int(cand4_total_votes),')')
print('Winner:  ', str(winner))

# - Writr to text =========================
fb = open("Analysis", "Election_results.txt","w")

strwrite = " "
Winner = []
fb.write("-----------------------------\n")
fb.write('Election_results:\n')	
fb.write('-----------------------------\n')	
fb.write("\n")

#strwrite = 'Total Months: ' + str(int(total_months))
strwrite = " "
strwrite = "Total Votes:  " +  str(int(total_votes))
fb.write(strwrite)

fb.write('-----------------------------\n')

canresults = round(float(cand1_total_votes / total_votes),2) * 100
strwrite = str((canresults))
strwrite = (cand1 + ':  ' + str((canresults)) + '%' + '\t' + '(' + str(int(cand1_total_votes)) + ')') + '\n'
fb.write(strwrite)

canresults = round(float(cand2_total_votes / total_votes),2) * 100
strwrite = str((canresults))
strwrite = (cand2 + ':  ' + str((canresults)) + '%' + '\t' + '(' + str(int(cand2_total_votes)) + ')') + '\n'
fb.write(strwrite)

canresults = round(float(cand3_total_votes / total_votes),2) * 100
strwrite = str((canresults))
strwrite = (cand3 + ':  ' + str((canresults)) + '%' + '\t' + '(' + str(int(cand3_total_votes)) + ')') + '\n'
fb.write(strwrite)

canresults = round(float(cand4_total_votes / total_votes),2) * 100
strwrite = str((canresults))
strwrite = (cand4 + ':  ' + str((canresults)) + '%' + '\t' + '(' + str(int(cand4_total_votes)) + ')') + '\n'
fb.write(strwrite)





