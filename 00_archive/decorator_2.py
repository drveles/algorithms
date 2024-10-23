from functools import wraps

def print_func_out(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

@print_func_out
def foo(a, b):
    return a + b


if __name__ == "__main__":
    foo(1, 2)