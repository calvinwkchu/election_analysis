# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# The data we need to retrieve
# Add our dependencies/modules
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("resources","election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Alternative way of opening file: file_to_load = 'resources/election_results.csv'

# 1. Initialize the total vote counter
total_votes=0

# Declare list of names for candidates, create dictionary for candidate votes, winning candidate and count tracker
candidate_options=[]
candidate_votes={}
winning_candidate=""
winning_count=0
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do : Perform analysis
    file_reader = csv.reader(election_data)

    # print the header row
    header=next(file_reader)
    print(header)

    # print each row in the csv file
    for row in file_reader:
        # 2a. Add to total vote counter
        total_votes+=1
        
        # 2b. Print candidate's names from each row
        candidate_name=row[2]

        # 2c. Add candidate's name if candidate's name does not match any existing, add it to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

        # 2d. Track each candidate's vote counter by adding into dictionary based on above condition and set vote counter to 0.
            candidate_votes[candidate_name] = 0

        # 2e. Count each candidate's vote
        candidate_votes[candidate_name]+=1
    #     print(row)

# 3. Print total votes & candidate names
print(total_votes)
print(candidate_votes)    


# 4. Determine the percentage of votes for each candidate by looping through the counts, and determine winner.
# 4a. Iterate through the candidates list

for candidate_name in candidate_votes:
    # 4b. Retrieve vote count of a candidate, and declare as variable (note current candidate_vote is a key inside dict, not a string/number therefore cannot use float function).
    vote = candidate_votes[candidate_name]
    # 4c. Calculate the percentage of votes.
    vote_percentage = float(vote)/float(total_votes) *100
    # 4d. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({vote:,})\n")
    
    # 4e. Determine winning vote count and candidate; determine if vote is greater than the winning count.
    if(vote>winning_count) and (vote_percentage>winning_percentage):
        # If true, then set winning_count = votes and winning_percentage = voting_percentage
        winning_count=vote
        winning_percentage=vote_percentage
        # And, set winning_candidate equal to candidate's name.
        winning_candidate=candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
    

# Alternative way of opening file: election_data = open(file_to_load, 'r')

# Close the file
election_data.close()

# Create a filename variable to a direct or indirect path to the file.

# # Using the with statement open the file as a text file.
# with open(file_to_save,"w") as txt_file:
#     # Write some data to file   
#     txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")
# # Close the file
# txt_file.close()



# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote