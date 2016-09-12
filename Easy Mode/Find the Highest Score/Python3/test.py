class Person(object):
    def __init__(self):
        self.data = []

    def greet(self, name, other_name):
        return "Hi {0}, my name is {1}".format(other_name, name)

print(Person().greet('Keith', 'Jon'))