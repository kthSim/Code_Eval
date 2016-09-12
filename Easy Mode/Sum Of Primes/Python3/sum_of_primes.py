def main():
    prime_list = []
    prime_total = 0
    num = 1
    while len(prime_list) != 1000:
        num += 1
        for div in range(2, num+1):
            if num == div:
                prime_list.append(num)
            elif num % div == 0:
                break

    for x in prime_list:
        prime_total += x
    print(prime_total)

if __name__ == '__main__':
    main()
