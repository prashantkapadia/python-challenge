import os
import csv

electionpath = os.path.join('..','Resources','election_data.csv')

with open(electionpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    total_vote = 0
    
    khan_count = 0
    khan_cent = 0.00

    correy_count = 0
    correy_cent = 0.00

    li_count = 0
    li_cent = 0.00

    tooley_count = 0
    tooley_cent = 0.000

    for row in csvreader:

        total_vote = total_vote + 1

        if row[2] == "Khan":
            khan_count += 1
        if row[2] == "Correy":
            correy_count += 1
        if row[2] == "Li":
            li_count += 1
        if row[2] == "O'Tooley":
            tooley_count += 1       



# Calculating Percentage *******
khan_cent = round((khan_count * 100)/total_vote,3)
correy_cent = round((correy_count * 100)/total_vote,3)
li_cent = round((li_count * 100)/total_vote,3)
tooley_cent = round((tooley_count * 100)/total_vote,3)



# Announcing the Winner

WinnerName = ""

if (khan_cent > correy_cent and khan_cent > li_cent and khan_cent > tooley_cent):
    WinnerName = "Khan"
elif (correy_cent > khan_cent and correy_cent > li_cent and correy_cent > tooley_cent):
    WinnerName = "Correy"
elif (li_cent > khan_cent and li_cent > correy_cent and li_cent > tooley_cent):
    WinnerName = " Li"
else:
    WinnerName = "O'Tolley"


print("------------------------")
print("Election Results")
print("------------------------")
print(f"Total Votes : {total_vote} ")
print("------------------------")
print(f" Khan : {khan_cent}% ({khan_count} ) ")
print(f" Correy  : {correy_cent}% ({correy_count})")
print(f" Li : {li_cent}% ({li_count})")
print(f" O'Tooley : {tooley_cent}% ({tooley_count})")
print("------------------------")
print(f"Winner is : {WinnerName}")
print("------------------------")

# Writing output to txt file.
with open ('analysis.txt', 'w+') as writer:
    
    writer.write("------------------------\n" + "Election Results\n" + "------------------------\n" )
    #writer.write("Election Results")
    #writer.write("------------------------")
    writer.write(f"Total Votes : {total_vote} \n" + "------------------------\n")
    #writer.write("------------------------")
    writer.write(f" Khan : {khan_cent}% ({khan_count}) \n")
    writer.write(f" Correy  : {correy_cent}% ({correy_count})\n")
    writer.write(f" Li : {li_cent}% ({li_count})\n")
    writer.write(f" O'Tooley : {tooley_cent}% ({tooley_count})\n" + "------------------------\n")
    #writer.write("------------------------")
    writer.write(f"Winner is : {WinnerName}\n" + "------------------------")
    #writer.write("------------------------")




