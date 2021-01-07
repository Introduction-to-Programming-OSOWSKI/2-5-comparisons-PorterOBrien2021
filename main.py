def greaterThan(x, y):
    if x > y:
        return True
    else:
        return False
def lessThan(x, y):
    if x < y:
        return True
    else:
        return False
def equalTo(x, y):
    if x == y:
        return True
    else:
        return False
def greaterOrEqual(x, y):
    if x >= y:
        return True
    else:
        return False
def lessOrEqual(x, y):
    if x <= y:
        return True
    else:
        return False

print(greaterThan(100, 10))

print(lessThan(9, 10))

print(equalTo(2, 2))

print(greaterOrEqual(100, 100))

print(lessOrEqual(50, 100))
