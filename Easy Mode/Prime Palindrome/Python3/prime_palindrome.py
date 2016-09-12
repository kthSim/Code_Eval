import sys

def main():
    prime_list = []
    for num in range(2, 1001):
        for div in range(2, num+1):
            if num == div:
                prime_list.append(num)
            elif num % div == 0:
                break

    for x in (list(reversed(prime_list))):
        if str(x) == str(x)[::-1]:
            print(x)
            break


if __name__ == '__main__':
    main()

import sys
"""For Code_Eval
def main():
    prime_list = []
    for num in range(2, 1001):
        for div in range(2, num+1):
            if num == div:
                prime_list.append(num)
            elif num % div == 0:
                break

    for x in (list(reversed(prime_list))):
        if str(x) == str(x)[::-1]:
            print(x)
            break


if __name__ == '__main__':
    main()
"""