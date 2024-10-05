def decorator(func):
    counter = 0
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f"running {func.__name__} thats returns {func(*args, **kwargs)}, this is {counter} call this func")
        return func
    return wrapper

@decorator
def beautiful_func(x, y):
    return x + y


beautiful_func(1,2)
beautiful_func(4,2)
beautiful_func(3,2)
beautiful_func(2,2)
