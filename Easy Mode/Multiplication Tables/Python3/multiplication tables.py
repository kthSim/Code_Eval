
def main():

    for x in range(1, 13):
        multi_row = ''
        for y in range(1, 13):
            print('{:4}'.format(x*y), end="")
            # multi_row += (str(x*y) + '   ')
        print('')

if __name__ == '__main__':
    main()
