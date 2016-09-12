import sys

# test = "Testing"
# print(test[1])

raw_paras = input("Please input parameters separated by a comma: ")
para_list = raw_paras.split(',')
binary_int = format(int(para_list[0]), 'b')

print(binary_int[-int(para_list[1])], binary_int[-int(para_list[2])])

if binary_int[-int(para_list[1])] == binary_int[-int(para_list[2])]:
    print('true')
else:
    print('false')

print(binary_int)

"""Sample code to read in test cases:
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:

        para_list = test.split(',')
        binary_int = format(int(para_list[0]), 'b')

        if binary_int[-int(para_list[1])] == binary_int[-int(para_list[2])]:
            print('true')
        else:
            print('false')
"""