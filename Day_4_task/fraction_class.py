# Fraction Class
# Demonstrates dunder methods.

import math


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        gcd = math.gcd(
            self.numerator,
            self.denominator
        )

        return Fraction(
            self.numerator // gcd,
            self.denominator // gcd
        )

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        num = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )

        den = (
            self.denominator
            * other.denominator
        )

        return Fraction(num, den).simplify()

    def __eq__(self, other):
        a = self.simplify()
        b = other.simplify()

        return (
            a.numerator == b.numerator
            and a.denominator == b.denominator
        )

    def __lt__(self, other):
        return (
            self.numerator * other.denominator
            < other.numerator * self.denominator
        )


f1 = Fraction(1, 2)
f2 = Fraction(1, 4)

print(f1 + f2)
print(f1 == Fraction(2, 4))
print(f2 < f1)

# Explore:
# total_ordering can generate remaining comparison methods automatically.