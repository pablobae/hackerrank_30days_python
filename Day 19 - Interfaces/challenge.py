class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):

        divisors = [n]
        if n <= 0 and not type(n) is int:
            raise ValueError('n is not a valid intenger >1 ')
        elif n > 1:
            for i in range(1, n // 2 + 1):
                if n % i == 0:
                    divisors.append(i)
        else:
            divisors = [1]

        return sum(divisors)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
