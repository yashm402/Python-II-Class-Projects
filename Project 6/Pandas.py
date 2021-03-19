# Yash Murthy
# 873564446
#Project 6 - 3006

###This program has four main parts. The first being a generation of a 1000 x 10 matrix. I chose to do a random generation of craps rolls (dice game)
### We then create a csv with the matrix with 10 column headers. The next section loads with csv file into a dataframe. Thirdly, we use the file to calculate the mean,
#median, std dev, and mode of the columns. Finally we are creating a txt file that shows the calculated stats, column names, and 3 rows from the dataframe to show.

import numpy as np
import pandas as pd

"""This function is used to generate a 1000x10 matrix"""
def matrix():
    #a = (np.arange(10000,).reshape(1000,10))
    rows = 1000
    columns = 10

    mx = np.random.randint(2,12, (rows, columns))
    #print(mx)
    return mx

"""This function creates a csv file with the randomized craps rolls matric. There are ten players, and each roll the dice 1000 times. 
    We used pandas to save it as a CSV file called TekkenCraps.csv."""
def create_csv(rolls):

    columnsHeaders = ["Yoshimitsu", "Heihachi","Jin", "Eddy", "King", "Panda", "Kuma", "Law", "Ogre", "Nina"]      ###Create the names of the Craps players aka Column headers
    rolls = pd.DataFrame(rolls)         ###creates two dimensional matrix uses dataframes function of pandas
    rolls.columns = columnsHeaders
    rolls.to_csv("TekkenCraps.csv", index=False)        ##Saves as CSV file and uses the column names without an index value

    print("Here are the randomized craps rolls for the 10 players\n", rolls)
    #with open("Matrix.csv", mode="w") as f:
      #     f.write(columns)


"""This function loads the csv file that was created above"""
def load():
    data = pd.read_csv("TekkenCraps.csv", header=0, index_col=False)
    return data


"""This function """
def statistics(crapsRollsPd):


    stats = pd.DataFrame(columns=crapsRollsPd.columns, index=["mean", "standard deviation", "mode", "median"])  ###This creates a dataframe to records reqd stats

    for players in stats.keys():
        for i in stats.index:
            stats[players][0] = crapsRollsPd[players].mean()
            stats[players][1] = crapsRollsPd[players].std()
            stats[players][2] = crapsRollsPd[players].mode()[0]
            stats[players][3] = crapsRollsPd[players].median()

    print ("\nPlayer Rolls statistics:\n\n", stats)


"""This function is used to create a txt file which contains the stats, column names, and 3 sample rows"""
def SummaryFile(statRolls, DFfull):

    DFfull = DFfull.sample(n=3).to_string()
    print("\nHere are three sample rows:\n", DFfull)

    statRolls = statRolls.to_string()                       ##stat to text file
    with open("TekkenCraps.txt", mode='w') as f:            ###writing into csv
        f.write(statRolls)
        f.write("\nHere are three random sample rows\n")        ###Writing three samples into csv
        f.write(DFfull)


def main():

    create = matrix()           ###creates 1000 x 10 matrix
    create_csv(create)          ###saves matric to the CSV file
    crapsRollsPd = load()       ###opens csv and converts to dataFrame using pd
    statRolls = statistics(crapsRollsPd)    #calls stats function
    SummaryFile(statRolls, crapsRollsPd)    ###saves data to txt file

if __name__ == "__main__":
    main()



###Walked through some hurdles that I was having with the for loops and csv creation with classmate Duncan Furguson
