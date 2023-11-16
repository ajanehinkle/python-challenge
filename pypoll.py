import os
import csv

BallotID = []
County = []
Candidate = []

csvpath = os.path.join('Resources','election_data.csv' )


print("Election Results")
print("--------------------")

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    next(csv_reader)
    data = list(csv_reader)
    line_count = len(data)
    
    vote = list(data)
    candidatelist = list()
    tally = list()

print(f"Total Votes: {line_count}")


for m in range (0,line_count):
        candidate = vote[m][2]
        tally.append(candidate)
        if candidate not in candidatelist: 
            candidatelist.append(candidate)
totalcount = len(candidatelist)

votes = list()
percentage = list()
for n in range (0,totalcount):
        name = candidatelist[n]
        votes.append(tally.count(name))
        vprct = votes[n]/line_count
        percentage.append(vprct)

winner = votes.index(max(votes))   

print ("--------------------")
for s in range (0,totalcount): 
        print(f"{candidatelist[s]}: {percentage[s]:.3%} ({votes[s]:,})")
print("----------------------------")
print(f"Winner: {candidatelist[winner]}")
print("----------------------------")

file = open('textpypoll', 'w')

file.write('Election Results\n')
file.write('--------------------\n')
file.write(f'Total Votes: {line_count}\n')
file.write('--------------------\n')
for s in range (0,totalcount):
    file.write(f'{candidatelist[s]}: {percentage[s]:.3%} ({votes[s]:,})\n')
file.write(f'----------------------------\n')
file.write(f'Winner: {candidatelist[winner]}\n')
file.write(f'----------------------------')

file.close()