import argparse
import csv

def ParseEntryFile():
    """
    1. Give a CSV file of company names, 
    """
    lst_fileNames=[]
    parser = argparse.ArgumentParser(description = 'obtains the number of employees working on a list of companies')
    parser.add_argument ('file', metavar='file', type=str, help='Enter only the name of a .csv file')
    parser.add_argument ('email', metavar='email', type=str, help='Enter email address for linkedin')
    parser.add_argument ('password', metavar='password', type=str, help='Enter password for linkedIn')
    args = parser.parse_args()

    fileName = args.file
    email = args.email
    password = args.password

    #print(f"fileName {fileName}")
    try:
        with open(fileName, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #print(row['Name'])
                lst_fileNames.append(row['Name'])  ###validate the existence of the Name column
    except FileNotFoundError:
        msg = "Sorry, the file "+ fileName + "does not exist."
        print(msg) # Sorry, the file  does not exist.

    return lst_fileNames, fileName, email, password
