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
# Alternative way of opening file: file_to_load = 'resources/election_results.csv'

# Open the election results and read the file.

with open(file_to_load) as election_data:

    # To do : Perform analysis

    print(election_data)   
# Alternative way of opening file: election_data = open(file_to_load, 'r')

# Close the file

election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote