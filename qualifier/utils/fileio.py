# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data



#Saves qualifying loans to a csv
def save_csv(csvpath, header, qualifying_loans):
    print("Saving qualifying loans to csv file")
    #Alerts user what is happening while file is being created.

    with open (csvpath, "w") as csvfile:
    #Creates a CSV writer
        csvwriter = csv.writer(csvfile, delimiter=",")
    #Establishes the delimiter as ",".
        csvwriter.writerow(header)
    #Adds header to the csv file.
        #for item in save_qualifying_loans:
        csvwriter.writerows(qualifying_loans)    
    #Rights a new row for each value from the daily rate sheet.




