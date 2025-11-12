
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def power(a, n):
    return a ** n

def root(a, n):
    if n == 0:
        return "Не може да се изчисли корен с нула!"
    return a ** (1 / n)
