# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# The data we need to retrieve
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("resources","election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Alternative way of opening file: file_to_load = 'resources/election_results.csv'

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do : Perform analysis
    file_reader = csv.reader(election_data)

    # print the header row
    header=next(file_reader)
    print(header)

    # for row in file_reader:
    #     print(row)
    
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


# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote