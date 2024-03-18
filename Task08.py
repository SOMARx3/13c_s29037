import square_gengerator


class someClass2(square_gengerator.someClass):
    @staticmethod
    def func2(start, end):
        if end < start:
            raise Exception("end smaller than start")
        else:
            return [x ** 3 for x in range(start, end)]


print(someClass2.func2(1, 11))
