###Yash Murthy 873564446
###In this program we are writing two functions. The first takes three parameters (a dictionary, a file object, and
#a boolean remove case). The functions adds the frequency of character counts to the file in the dictionary.
#This function contains the boolean remove_case which, if false, the uppercase letter is put into the dictionary.
# If true the lowercase letter is the key to the dictionary.
##The other function (main()) handles the arguments and calls the function add frequencies. There are four main
# functions of the main funtion.
# 1. Parse the command line arguments -c, -l, -z
# 2. Create an empty dictionary
# 3. Add the frequencies for each file in the argument list to that dictionary
# 4. Print out the elements of that dictionary in CSV format

# The flags allow us to change those options:
# -c :: an optional flag that distinguishes between upper and lower case. For example, the file 'aA' would count one 'a' and one 'A'.
# -l :: an optional flag with an argument, that only prints out the frequencies of the characters in the argument letters. For example, '-l aeiou' counts only vowels.
# -z :: an optional flag that prints a row for every character, even when it occurs zero times.
import sys

def add_frequencies(d, file, remove_case):

    text = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upperLetters = ['A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in upperLetters:
        letters.append(i)           ###takes letter list and adds the uppercase chars to it
    with open(file, mode='r', encoding='UTF-8') as f:
        for row in f:
            text += row

    if remove_case == True:
        for character in letters:
            d[character] = 0            ###setting value = to 0
        for i in text:
            i = i.lower()       ###making it lower case
            if i in d:
                d[i] += 1
    elif remove_case == False:
        for character in letters:
            d[character] = 0
        for i in text:
            if i in d:
                d[i] += 1

    return d


def main(add_frequencies):
    '''function (main()) handles the arguments and calls the function add frequencies. There are four main
# functions of the main funtion.
# 1. Parse the command line arguments -c, -l, -z
# 2. Create an empty dictionary
# 3. Add the frequencies for each file in the argument list to that dictionary
# 4. Print out the elements of that dictionary in CSV format'''
    ###need to append the frequencies of each character and add it to the dictionary
    commandline = []
    readFile = []
    flags = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ###making the dictionary and added the alaphabet contained in letters to it
    d = {}

    for word in sys.argv:
        commandline.append(word)

    for i in commandline:
        if i[-4:] == '.txt':
            readFile.append(i)  ###taking characters from text file and adding it to our list
        elif i[0] == '-':   ### looks for initial character in i
            flags.append(i)
    remove_case = False

    ###loop through flaglist and see if char is in there
    for file in readFile:###opening txt file
        d = add_frequencies(d, file, remove_case)
    ### if z is in the dictionary we want to print it
    ### if z is not in the dictionary, we want to get rid of 0 values
    # for i.upper in commandline:
    #     if i[-4] == '.txt':
    #         readFile.append(i)
    #     elif i[0] == '-':
    #         flags.append(i)




    ###if l is in there
    ###???

    print(d)


main(add_frequencies)









###Sources: Lecture Notes, talked through with classmate Duncan F
