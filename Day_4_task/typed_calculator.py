# Type-Hinted Calculator Module
# Demonstrates type hints, docstrings, and Optional return type.

from typing import Optional

def add(a: float, b: float) -> float:
    """Returns sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns difference of two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns product of two numbers."""
    return a * b

def divide(a: float, b: float) -> Optional[float]:
    """Returns division result or None if division by zero."""
    if b == 0:
        return None
    return a / b

def power(base: float, exp: float) -> float:
    """Returns base raised to exponent."""
    return base ** exp

def modulo(a: int, b: int) -> Optional[int]:
    """Returns modulo result."""
    if b == 0:
        return None
    return a % b

print(add(10, 5))
print(divide(10, 0))
print(power(2, 3))
print(modulo(10, 3))