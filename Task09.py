class someClass2:
    @staticmethod
    def func2(start, end):
        if end < start:
            raise Exception("end smaller than start")
        else:
            return [x ** 3 for x in range(start, end)]


class someClass3(someClass2):
    @staticmethod
    def func2(start, end):
        if end < start:
            raise Exception("end smaller than start")
        else:
            return [x ** 2 for x in range(start, end)]


print(someClass3.func2(1, 11))
