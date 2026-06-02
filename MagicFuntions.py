class x:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

class Addition:
    def __init__(self, *arguments):
        if len(arguments) == 0:
            self.numbers = (0,0)
        else:
            self.numbers = arguments

    def __add__(self, other):
        sum = tuple(x + y for x,y in zip(self.numbers, other.numbers))
        return Addition(*sum)

    def __mul__(self, other):
        mul = tuple(x * y for x,y in zip(self.numbers, other.numbers))
        return Addition(*mul)


obj1 = Addition(2,3)
obj2 = Addition(4,5)
obj3 = obj1 + obj2
obj4 = obj1 * obj2
print(obj3.numbers)
print(obj4.numbers)

#obj1 = x(3,4)
#print(obj1.sum())

