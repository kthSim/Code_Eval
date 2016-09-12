import sys
from collections import Counter
import collections

raw_elements = input('Please enter list of elements separated by commas: ')

elements = raw_elements.split(',')

counted_elements = Counter(elements)

print(counted_elements)
print(counted_elements.most_common(2))

if counted_elements.most_common(2)[0][1] == counted_elements.most_common(2)[1][1]:
    print('None')
else:
    print(counted_elements.most_common(2)[0][0])

"""
import sys
from collections import Counter

with open(sys.argv[1], 'r') as test_cases:
    for test1 in test_cases:
        elements = test1.split(',')

        counted_elements = Counter(elements)

        if int(counted_elements.most_common(2)[0][1]) == int(counted_elements.most_common(2)[1][1]):
            print('None')
        else:
            print(counted_elements.most_common(2)[0][0])
"""