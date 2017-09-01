

ERROR_RANGE = 0.00001

class Operator:
    """Operator holds all the operators"""

    def __init__(self):
        pass

    def plus(self, number1, number2):
        """
        plus is the function for "+" operator.
        It returns (number1 + number2)
        """
        # TODO deal with double
        # TODO deal with minus
        gap = 0
        while gap < number2:
            gap = plus_one(gap)
            number1 = plus_one(number1)

        return number1

    def minus(self, number1, number2):
        """
        minus is the function for "-" operator.
        it returns (number1 - nubmer2)
        """
        # TODO deal with double
        # TODO deal with minus
        if number1 < number2:
            return self.minus(number2, number1)

        result = 0
        while number2 < number1:
            result = plus_one(result)
            number2 = plus_one(number2)

        return result

    def multiply(self, number1, number2):
        """
        multiply is the function for "*" operator.
        it returns (nubmer1 * number2)
        """
        # TODO deal with double
        # TODO deal with minus
        if number1 == 0 or number2 == 0:
            return 0

        iter_num = 0
        result = 0
        while iter_num < number2:
            iter_num = plus_one(iter_num)
            result = self.plus(result, number1)

        return result

    def divide(self, number1, number2):
        """
        divide is the function for "/" operator.
        it returns (number1 / number2)
        """
        # TODO deal with double
        # TODO deal with minus
        pass


def plus_one(base_num):
    """plus_one is the base function other operators."""
    return base_num + 1
