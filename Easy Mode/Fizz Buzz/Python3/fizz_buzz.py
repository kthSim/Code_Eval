import sys

game_parameters = input("Please enter desired parameters: ")  # Parameters should be 3 numbers (e.g X Y N)
parameters = game_parameters.strip().split()
output_string = ''

for x in range(1, int(parameters[2])+1):
    if x % int(parameters[0]) == 0:
        output_string += 'F'
    if x % int(parameters[1]) == 0:
        output_string += 'B'
    if x % int(parameters[0]) != 0 and x % int(parameters[1]) != 0:
        output_string += str(x)
    output_string += ' '

print(output_string)

""" For Code_Eval
Sample code to read in test cases:
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        parameters = test.strip().split()
        output_string = ''

        for x in range(1, int(parameters[2])+1):
            if x % int(parameters[0]) == 0:
                output_string += 'F'
            if x % int(parameters[1]) == 0:
                output_string += 'B'
            if x % int(parameters[0]) != 0 and x % int(parameters[1]) != 0:
                output_string += str(x)
            output_string += ' '

        print(output_string)

"""