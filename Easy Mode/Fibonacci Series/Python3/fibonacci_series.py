import sys

desired_num = input('Please input desired sequence: ')
first_fib, second_fib = 0, 1
latest_fib = second_fib

for x in range(1, int(desired_num)-1):
    first_fib = second_fib
    second_fib = latest_fib
    latest_fib = first_fib + second_fib

print(latest_fib)

"""Sample code to read in test cases:
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if int(test) == 0:
            print('0')
            continue

        first_fib, second_fib = 0, 1
        latest_fib = second_fib

        for x in range(1, int(test)-1):
            first_fib = second_fib
            second_fib = latest_fib
            latest_fib = first_fib + second_fib

        print(latest_fib)
"""