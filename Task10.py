from abc import ABC, abstractmethod


class SquareGenerator(ABC):
    @staticmethod
    @abstractmethod
    def generate_squares(start, end):
        pass


class CubicGenerator(SquareGenerator):
    @staticmethod
    def generate_squares(start, end):
        return [x ** 3 for x in range(start, end)]


print(CubicGenerator.generate_squares(1, 11))
