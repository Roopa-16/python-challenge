import os
import csv

electionData = os.path.join("election_data.csv")
candidates = []
numberVotes = []
percentVotes = []
totalVotes = 0

with open(electionData, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        totalVotes += 1 
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            numberVotes.append(1)
        else:
            index = candidates.index(row[2])
            numberVotes[index] += 1
    
    for votes in numberVotes:
        percentage = (votes/totalVotes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percentVotes.append(percentage)
    
    winner = max(numberVotes)
    index = numberVotes.index(winner)
    winningCandidate = candidates[index]

print("Election Results")
print("----------------------------")
print(f"Total Votes: {str(totalVotes)}")
print("----------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percentVotes[i])} ({str(numberVotes[i])})")
print("----------------------------")
print(f"Winner: {winningCandidate}")
print("----------------------------")

output = open("output.txt", "w")
line1 = "Election Results"
line2 = "----------------------------"
line3 = str(f"Total Votes: {str(totalVotes)}")
line4 = str("----------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percentVotes[i])} ({str(numberVotes[i])})")
    output.write('{}\n'.format(line))
line5 = "----------------------------"
line6 = str(f"Winner: {winningCandidate}")
line7 = "----------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))