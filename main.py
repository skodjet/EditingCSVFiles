""" Removes gibberish characters from csv files.
    Place this file in the same location as the csv file you want to modify.
"""

import csv

# TODO: Replace 'bad_file' with the input data, and 'new_file' to what you want the output file to be named as
bad_file = 'June 11 00_00 - 10_00ver2.csv'
new_file = 'June 11 00_00 - 10_00_clean.csv'

# Write the list of attributes at the top of the file
attributes = ['timestamp', 'data.content', 'type', 'application-id', 'level', 'correlationId', 'data.requestUrl']
csv.writer(open(new_file, 'a')).writerow(attributes)

# Open the csv file and filter out junk rows
with open(bad_file, 'r', encoding='latin-1') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if line:
            check = line[0]
            print(check)
        else:
            continue


        new_row = []

        # TODO: Replace "Jun" with whatever month you're taking data from
        if "Jun" in check:
            for val in line:
                if val != '' or val != '-' or val is not None:
                    new_row.append(val)

            try:
                if len(new_row) != 0:
                    csv.writer(open(new_file, 'a')).writerow(new_row)

            # Gets rid of non-unicode characters in the file.
            except:
                print("Junk character found!")


#TODO: If there is a null character error, perform the following steps:

# 1. Open the csv file in Excel
# 2. Press ctrl + H
# 3. Search for x00 and leave the "replace with" field blank. Press "replace all"
# 4. Save the file and run this program again.

