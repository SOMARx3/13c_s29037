import math

class someClass:
    def func(range1):
        return [x * x for x in range1]

print(list(map(math.sqrt, someClass.func(range(1, 11)))))

