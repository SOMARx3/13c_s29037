import square_gengerator


class CubicGenerator(square_gengerator.SquareGenerator):
    @staticmethod
    def func2(start, end):
        if end < start:
            raise Exception("end smaller than start")
        else:
            return [x ** 3 for x in range(start, end)]


print(CubicGenerator.func2(1, 11))
