import timeit

def slow_function():
    total = 0
    for i in range(10000):
        total += i
    return total

print(timeit.timeit("slow_function()", globals=globals(), number=10))

#Optimization involves improving the
# performance and efficiency of your code. 
# This can be related to speed, memory usage, 
# or other resources.