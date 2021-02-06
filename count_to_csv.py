###Yash Murthy
###DU ID 873564446
#This script will take an additional argument over count.py:
# the final argument should be the name of a csv file to
# which you will write the data printed.
# python3 count_to_csv.py -z -c test1.txt test2.txt out.csv

import sys
import count
import csv


def count_to_csv():
    csvArgs = sys.argv
    csvFileArgs = [i for i in csvArgs if '.csv' in i]
    csvFileName = ""
    for i in csvFileArgs:
        csvFileName += i
    csvArgs.remove(csvFileName)         ###Removes file name from args
    d={}
    d = count.main()
    a_file = open(csvFileName, "w")     ###Writing the dictionary to CSV
    csvWriter = csv.writer(a_file)
    for key, value in d.items():
        csvWriter.writerow([key,value])
    a_file.close()
    print('Your file has been saved as a CSV: ', csvFileName)
def main():

    count_to_csv()

main()

###Worked with DuncanF and Danny V