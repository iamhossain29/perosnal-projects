class Person:
    def __init__(self):
        self.name = 'Bobby'

Bobby = Person()
same_bobby = Bobby
print(Bobby is same_bobby)

another_bobby = Person()

print(Bobby is another_bobby)
