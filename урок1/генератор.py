def foo():
    yield 12
    yield 14

names = foo()
print(next(names))
print(next(names))
print(next(names))