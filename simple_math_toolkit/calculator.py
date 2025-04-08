"""
Simple Math Toolkit - Calculator module
Provides basic and advanced mathematical operations
"""

def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a"""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base: float, exponent: float) -> float:
    """Calculate base raised to the power of exponent"""
    return base ** exponent

def percentage(part: float, whole: float) -> float:
    """Calculate what percentage part is of whole"""
    if whole == 0:
        raise ValueError("Whole cannot be zero")
    return (part / whole) * 100 