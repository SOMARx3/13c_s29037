from Task08 import someClass2

class someClass3(someClass2):
    def func2(start1, end):
        if (end < start1):
            raise Exception("end smaller than start")
        else:
            return [x ** 2 for x in range(start1, end)]

print(someClass3.func2(1, 11))