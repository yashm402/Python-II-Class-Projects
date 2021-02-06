###Yash Murthy
###DU ID 873564446
import sys
import string

## function to do the counting
def add_frequencies(d, f, remove_case):
   '''Adds the character frequencies of the given text file to the given
   dictionary.

   Arguments:
      d (dict): map from characters (str) to frequency counts (int)
      f (file): text file to read characters from
      remove_case (bool): if true, runs .lower() on chars before mapping
   '''
   ## iterate through the file, char-by-char
   for line in f:
      for c in line:
         ## convert c to key (use 'remove_case' to check for lower-casing)
         key = c.lower() if remove_case else c

         ## increment that char in the dictionary
         if key in d:
            d[key] += 1
         else:
            d[key] = 1

   ## return that dictionary (unnecessary, but matches intuition when calling)
   return d

## character counting function
'''Prints out the frequencies of various characters in input files. Uses
   sys.argv to determine what those characters are, and which input files to
   read from.'''
def charCount():


   ## default settings
   output_chars = string.ascii_letters
   remove_case = True
   print_zeroes = False

   ## get "real arguments".  that is, ignore the script name
   #if test == True:    ###Try Boolean to fix args issue

   args = sys.argv[1:]###Comment out when running the program from test_count.py, ON when running from command line term
   #args = sys.argv ###Comment out when running the program from command line terminal, ON when running test_count.py

   ## process the leading flags, this process loops through the leading flags
   while args and args[0].startswith('-'):
      ## remove the next flag from the list
      arg = args.pop(0)

      ## handle that flag
      if arg == '-c':
         remove_case = False
      elif arg == '-l':
         output_chars = args.pop(0)
      elif arg == '-z':
         print_zeroes = True
      elif arg == '--':
         break
      else:
         ## unknown argument!
         print(f'unknown argument: \'{arg}\'', file=sys.stderr)

   ## if we have to remove the case, remove it from the output_chars first!
   if remove_case == True:
      output_chars = ''.join(c for c in output_chars if c.islower())
      print('Output characters:', output_chars)

   ## the remaining arguments must all be files... process them!
   d = {}
   for filename in args:
      with open(filename, 'r') as f:
         add_frequencies(d, f, remove_case)

   newchars = []                    ###New character list
   newLandZchars = []               ###New l and z list
   newFreq = []                     ### list containing new frequencies
   newDict = {}                     ### new dictionary


   ## print out the output characters, as requested, in CSV format
   for c in output_chars:
      ## get the frequency count from the dictionary, or zero if not present
      freq = d[c] if c in d else 0
      newFreq.append(freq)
      ## print that row, if needed (if zero, check print_zeroes first)
      if freq != 0 or print_zeroes:
         print(f'"{c}",{freq}')

   ###New information to return to the list, added if the freq !=0
   newLandZchars = [x for x in output_chars]
   print('New l and z Characters', newLandZchars)
   print('L characters', output_chars)
   print('Total new dictionary', d)
   print('L frequency', freq)
   print('New Frequency', newFreq)

   try:
      if '-c' in arg:
         print('we have c')
         if '\n' in d:
            del d['\n']
         newDict = d
      elif '-l' in arg:
         print('we have l')
         # to convert lists to dictionary
         newDict = {newLandZchars[i]: newFreq[i] for i in range(len(newLandZchars))}
      elif '-z' in arg:
         print('we have z')
         # to convert lists to dictionary
         newDict = {newLandZchars[i]: newFreq[i] for i in range(len(newLandZchars))}
      elif arg == '--':
         print('break')
      else:
         print('Error')
   except NameError:
      arg = False
      if '\n' in d:
         del d['\n']
      newDict = d
   else:
      arg = True
   #   print('we made it to this else and argTrue')

   return newDict


###Main Function
def main():

   args = sys.argv
   print('mainArgs: ', args)
   d = charCount(args)
   print('main: ', d)
   return d

if __name__ == '__main__':
   main()



###Worked with classmates Duncan F and Danny V
