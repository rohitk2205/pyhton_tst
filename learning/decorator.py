import time

def timefunc(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@timefunc
def add(x, y) :
    return x + y
@timefunc
def sub(x, y):
    return x - y
@timefunc
def mul(x, y):
    return x * y
@timefunc
def div(x, y) :
    return x / y
print (add (4,5) )
print (sub (4,5) )
print (mul (4,5) )
print (div (4,5) )