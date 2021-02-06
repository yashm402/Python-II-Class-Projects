###Yash Murthy
###DU ID 873564446

import unittest
import sys
import count



class TestCount(unittest.TestCase):

    def testCFlag(self):
        """This test looks at the l flag and determines if the dictionary reads the specified requested letter"""""
        sys.argv = ['-c', 'text.txt']
        print('testsys',sys.argv)
        result = count.main()
        print('testResult: ',result)
        check = {'A': 2, 'b': 2, 'C': 1, 'c': 1, 'D': 1, 'd': 1}
        self.assertDictEqual(result,check)

    def testLFlag(self):
        """This test looks at the l flag and determines if the dictionary reads the specified requested letter"""""
        sys.argv = ['-l', 'abc', 'text.txt']
        print('testsys',sys.argv)
        result = count.main()
        print('testResult: ',result)
        check = {'a': 2, 'b': 2, 'c': 2}
        self.assertDictEqual(result,check)

    def testZFlag(self):
        """This test looks at the l flag and determines if the dictionary reads the specified requested letter"""""
        sys.argv = ['-z', 'text.txt']
        print('testsys',sys.argv)
        result = count.main()
        print('testResult: ',result)
        check = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.assertDictEqual(result,check)

    def testCandLFlag(self):
        """This test looks at the l flag and determines if the dictionary
        reads the specified requested letter"""
        sys.argv = ['-c', '-l', 'abc', 'text.txt']
        print('testsys',sys.argv)
        result = count.main()
        print('testResult: ',result)
        check = {'a': 2, 'b': 2, 'c': 2}
        self.assertDictEqual(result,check)


if __name__ == '__main__':
    unittest.main()

#Run w/ : python -m unittest TestCount.py

###Worked with classmates Duncan F and Danny V
