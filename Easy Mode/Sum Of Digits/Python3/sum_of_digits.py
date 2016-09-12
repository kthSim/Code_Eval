import sys


def main():
    raw_int = input('Please enter a number: ')
    sum_digit = 0
    for i in str(raw_int):
        sum_digit += int(i)
    print(sum_digit)

if __name__ == '__main__':
    main()

"""Sample code to read in test cases:
import sys

def main():
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            sum_digit = 0
            for i in test.strip():
                sum_digit += int(float(i))
            print(sum_digit)

if __name__ == '__main__':
    main()
"""