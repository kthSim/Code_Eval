import sys

raw_string = input('Please enter raw text:')
print(raw_string.lower())

"""Sample code to read in test cases:
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print(test.lower())
"""