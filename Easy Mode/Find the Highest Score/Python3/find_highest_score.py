import sys
import math

collated_scores = []
highest_scores = []

raw_score_table = input("Please enter raw scores:")

split_table = raw_score_table.split("|")

for i in split_table:
    collated_scores.append(i.strip().split())

print(split_table)
print(collated_scores, len(collated_scores))

a = len(collated_scores)
b = len(collated_scores[0])

print(a, " x ", b)

for x in range(0, b):
    temp_list = []
    for y in range(0, a):
        print(collated_scores[y][x])
        temp_list.append(int(collated_scores[y][x]))
    temp_list.sort(reverse=True)
    print(temp_list)
    highest_scores.append(temp_list[0])

print(highest_scores)
for z in highest_scores:
    print(z, end=" ")
print('\n')


"""For Code_Eval
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        collated_scores = []
        highest_scores = []

        split_table = test.split("|")

        for i in split_table:
            collated_scores.append(i.strip().split())

        a = len(collated_scores)
        b = len(collated_scores[0])

        for x in range(0, b):
            temp_list = []
            for y in range(0, a):
                temp_list.append(int(collated_scores[y][x]))
            temp_list.sort(reverse=True)
            highest_scores.append(temp_list[0])

        for z in highest_scores:
            print(z, end=" ")
        print('')
"""
