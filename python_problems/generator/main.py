def func():
     yield 5
     yield 2
     yield 3




value=func()
print(next(value))
print(next(value))