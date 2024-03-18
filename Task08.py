import square_gengerator

class someClass2(square_gengerator.someClass):
    def func2(start1, end):
        if (end < start1):
            raise Exception("end smaller than start")
        else:
            return [x ** 3 for x in range(start1, end)]

print(someClass2.func2(1, 11))