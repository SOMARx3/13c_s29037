class SquareGenerator:
    @staticmethod
    def func(start1, end):
        if end < start1:
            raise Exception("end smaller than start")
        else:
            return [x * x for x in range(start1, end)]
