import sys

raw_timestamp = input("Please enter time stamps: ")
timestamp_list = raw_timestamp.split()
sorted_stamps = ''

for stamp in sorted(timestamp_list)[::-1]:
    sorted_stamps += (stamp + ' ')
print(sorted_stamps.strip())

"""Sample code to read in test cases:
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        timestamp_list = test.split()
        sorted_stamps = ''

        for stamp in sorted(timestamp_list)[::-1]:
            sorted_stamps += (stamp + ' ')
        print(sorted_stamps.strip())
"""