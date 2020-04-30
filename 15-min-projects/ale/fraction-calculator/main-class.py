def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class Frac:
    def __init__(self, dividend, divisor):
        c = gcd(dividend, divisor)
        self.dividend = dividend // c
        self.divisor = divisor // c

    def __add__(self, other):
        a = self.dividend * other.divisor + other.dividend * self.divisor
        b = self.divisor * other.divisor
        c = gcd(self.divisor, other.divisor)
        a = a // c
        b = b // c
        return Frac(a, b)

    def __str__(self):
        return f'{self.dividend} / {self.divisor}'

a = Frac(1, 4)
b = Frac(3, 2)

print(a + b)
