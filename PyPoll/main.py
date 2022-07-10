#The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 

#Import Modules
import os
import csv

#Create file path and open file to read
inputcsvpath = os.path.join('Resources','election_data.csv')

#Create file path for writing
outputcsvpath = os.path.join('analysis','election_analysis.csv')

#Open the election_data.csv for reading
with open(inputcsvpath) as csvinputfile:

    csvreader = csv.reader(csvinputfile, delimiter=',')

    #Read the header row first
    csv_header = next(csvreader)

    #Initialize Variables
    NumRows = 0

#The total number of votes cast 
#   count on the loop running through the rows of the file
    #Read each row of data after the header
    for row in csvreader:
        #Count rows
        NumRows = NumRows +1



#A complete list of candidates who received votes 
#   loop through adding unique candidate names to a Candidate list

#The percentage of votes each candidate won
#   Calculation of num votes/total voles

#The total number of votes each candidate won
#   Need to look at lists vs dictionaries, how to assign the number to the name

#The winner of the election based on popular vote.
#   Greatest vote number is the winner



#Print the data to screen

# Print the header section
print('Election Results')
print('------------------------------')

# Print the Total number of votes
print(f'Total Votes: {NumRows}')
print('------------------------------')


#Create and export table to csv file
with open(outputcsvpath, 'w') as csvoutputfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvoutputfile, delimiter=',')

    # Write the header section
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['------------------------------'])

    # Write the Total number of votes
    csvwriter.writerow([f'Total Votes: {NumRows}'])
    csvwriter.writerow(['------------------------------'])
