import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"time taken by {func.__name__}: {end_time - start_time}")
        return result
    return wrapper


@timer
def sing():
    return "Caller"


"""
Advanced function
"""


def timer(unit='seconds'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if unit == 'milliseconds':
                elapsed_time *= 1000
                print(f"Time taken by {func.__name__}: {elapsed_time} milliseconds")
            elif unit == 'microseconds':
                elapsed_time *= 1_000_000
                print(f"Time taken by {func.__name__}: {elapsed_time} microseconds")
            else:
                print(f"Time taken by {func.__name__}: {elapsed_time} seconds")
            return result

        return wrapper

    return decorator


@timer(unit='milliseconds')
def some_function():
    time.sleep(0.1)
    pass


some_function()
