#Import needed modules
from datetime import date
import os
import csv

#Create file path and open file to read
inputcsvpath = os.path.join('Resources','budget_data.csv')

#Create file path for writing
outputcsvpath = os.path.join('analysis','budget_analysis.csv')

#Open the budget_data.csv for reading
with open(inputcsvpath) as csvinputfile:

    csvreader = csv.reader(csvinputfile, delimiter=',')

    #Read the header row first
    csv_header = next(csvreader)

    #Initialize Variables
    NumRows = 0
    GreatestIncAmt = 0
    GreatestIncDate = 1/1/2020
    GreatestDecAmt = 0
    GreatestDecDate = 1/1/2020
    NetProfitLoss = 0
    ProfitLossChngAmt = 0
    ProfitLossChng = []
    PrevProfitLoss = 0
    ProfitLoss = 0


    #Read each row of data after the header
    for row in csvreader:
        #Count rows
        NumRows = NumRows +1

        #Sum Profit/Losses
        ProfitLoss = float(row[1])
        NetProfitLoss = float(NetProfitLoss) + ProfitLoss

        #Calculate the profit/loss changes and sum them
        if NumRows>1:
            ProfitLossChngAmt = ProfitLoss-PrevProfitLoss
            ProfitLossChng.append(ProfitLossChngAmt)
            

        #Save current Profitloss to PrevProfitLoss variable for next row calc
        PrevProfitLoss = ProfitLoss

        #The greatest increase in profits (date and amount) over the entire period
        if ProfitLossChngAmt > GreatestIncAmt:
            GreatestIncAmt = ProfitLossChngAmt
            GreatestIncDate = row[0]

        #The greatest decrease in profits (date and amount) over the entire period
        if ProfitLossChngAmt < GreatestDecAmt:
            GreatestDecAmt = ProfitLossChngAmt
            GreatestDecDate = row[0]

#Print the data to screen

# Print the header section
print('Financial Analysis')
print('------------------------------')

# Print the Total number of months
print(f'Total Months: {NumRows}')

# Print the Total
formatted_NetProfitLoss = "${:,.2f}".format(NetProfitLoss)
print(f'Total: {formatted_NetProfitLoss}')

# Calc (sum of Profit/loss changes divided by 1 less than the total rows) and Print the Average Change
formatted_AvgChange = "${:,.2f}".format(sum(ProfitLossChng)/(NumRows-1))
print(f'Average Change: {formatted_AvgChange}')

# Print Greatest Increase in Profits
formatted_GreatestIncAmt = "${:,.2f}".format(GreatestIncAmt)
print(f'Greatest Increase in Profits: {GreatestIncDate} {formatted_GreatestIncAmt}')

# Print the Greatest Decrease in Profits
formatted_GreatestDecAmt = "${:,.2f}".format(GreatestDecAmt)
print(f'Greatest Decrease in Profits: {GreatestDecDate} {formatted_GreatestDecAmt}')

#Create and export table to csv file
with open(outputcsvpath, 'w') as csvoutputfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvoutputfile, delimiter=',')

    # Write the header section
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------------------'])

    # Write the Total number of months
    csvwriter.writerow([f'Total Months: {NumRows}'])

    # Write the Total
    csvwriter.writerow([f'Total: {formatted_NetProfitLoss}'])

    # Write the Average Change
    csvwriter.writerow([f'Average Change: {formatted_AvgChange}'])

    # Write Greatest Increase in Profits
    csvwriter.writerow([f'Greatest Increase in Profits: Aug-16 ($1862002)'])
    
    # Write the Greatest Decrease in Profits
    csvwriter.writerow([f'Greatest Decrease in Profits: Feb-14 ($-1825558)'])

