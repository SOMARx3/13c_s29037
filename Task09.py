class CubeGenerator:
    @staticmethod
    def square_generator(start, end):
        if end < start:
            raise Exception("end smaller than start")
        else:
            return [x ** 3 for x in range(start, end)]


class SquareGenerator(CubeGenerator):
    @staticmethod
    def square_generator(start, end):
        if end < start:
            raise Exception("end smaller than start")
        else:
            return [x ** 2 for x in range(start, end)]


print(SquareGenerator.square_generator(1, 11))
