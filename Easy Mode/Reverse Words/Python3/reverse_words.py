import sys

raw_string = input("Please input a sentence")
raw_str_list = raw_string.split()
reverse_str = ''
print(raw_str_list)

for word in raw_str_list[::-1]:
    reverse_str += word
    reverse_str += ' '
print(reverse_str.strip())

"""Sample code to read in test cases:
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        raw_str_list = test.split()
        reverse_str = ''

        for word in raw_str_list[::-1]:
            reverse_str += word
            reverse_str += ' '
        print(reverse_str.strip())
"""