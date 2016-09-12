import sys

raw_paras = input("Please enter two numbers separated by a comma:")
para1, para2 = int(raw_paras.split(',')[0]), int(raw_paras.split(',')[1])
smallest_multi = para2
multi = 1

while para1 > smallest_multi:
    multi += 1
    smallest_multi = para2 * multi

print(smallest_multi)

"""Sample code to read in test cases:
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        para1, para2 = int(test.split(',')[0]), int(test.split(',')[1])
        smallest_multi = para2
        multi = 1

        while para1 > smallest_multi:
            multi += 1
            smallest_multi = para2 * multi

        print(smallest_multi)
"""