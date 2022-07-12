#The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 

#Import Modules
from operator import contains
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
    CandidateName = ""
    Candidates = {}
    VoteCount = 0

#The total number of votes cast - count on the loop running through the rows of the file
    #Read each row of data after the header
    for row in csvreader:
        #Count rows
        NumRows = NumRows +1

        #A complete list of candidates who received votes loop through adding unique candidate names to a Candidate list and counting votes per candidate
        CandidateName = row[2]
        if CandidateName in Candidates:
            VoteCount = Candidates[CandidateName] +1
            Candidates[CandidateName] = VoteCount
        else:
            Candidates[CandidateName] = 1


#----------Print the data to screen and write to the file----------------
# Print the header section
with open(outputcsvpath, 'w') as csvoutputfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvoutputfile, delimiter=',')
    
    #Print Header Section to screen
    print('Election Results')
    print('------------------------------')

    # Write the header section to file
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['------------------------------'])

    # Print the Total number of votes to screen
    print(f'Total Votes: {NumRows}')
    print('------------------------------')

    # Write the Total number of votes to file
    csvwriter.writerow([f'Total Votes: {NumRows}'])
    csvwriter.writerow(['------------------------------'])

    #Print Candidate Names, percent of vote and total votes to screen and write to file
    Count = 0
    HighVotes = 0

    for x in Candidates:
        CandidateName = list(Candidates.items())[Count][0]
        VoteCount = list(Candidates.items())[Count][1]
        formatted_VotePercent = "{:,.3f}%".format(VoteCount/NumRows*100)
        print(f'{CandidateName}:  {formatted_VotePercent} ({VoteCount})')
        csvwriter.writerow([f'{CandidateName}:  {formatted_VotePercent} ({VoteCount})'])
        Count = Count+1

        #Identify the winner by finding candidate with highest votes
        if VoteCount>HighVotes:
            Winner = CandidateName
            HighVotes = VoteCount
        
    print('------------------------------')
    csvwriter.writerow(['------------------------------'])

    #Print Winner to screen
    print(f'Winner: {Winner}')
    print('------------------------------')

    #Write winner to the file
    csvwriter.writerow([f'Winner: {Winner}'])
    csvwriter.writerow(['------------------------------'])
