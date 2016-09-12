__author__ = 'keith'

import sys
import datetime
import re

raw_string = input("Enter Test string: ")

# clean_string = raw_string + "123"
clean_string1 = re.sub(r'[^a-zA-Z ]', ' ', raw_string)  # removes non-letters
clean_string2 = clean_string1.lower()
clean_string3 = clean_string2.strip(' ')
while '  ' in clean_string3:
    clean_string3 = re.sub(r'  ', ' ', clean_string3)

print("Clean String: ", clean_string3)

"""
import sys
import re

def main():
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            clean_string1 = re.sub(r'[^a-zA-Z ]', ' ', test)  # removes non-letters
            clean_string2 = clean_string1.lower()
            clean_string3 = clean_string2.strip(' ')
            while '  ' in clean_string3:
                clean_string3 = re.sub(r'  ', ' ', clean_string3)

            print(clean_string3)

if __name__ == '__main__':
    main()
"""