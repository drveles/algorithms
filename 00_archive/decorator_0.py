def decorator(func):
    counter = 0
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        result = func(*args, **kwargs)
        print(f"running {func.__name__} thats returns {result}, this is {counter} call this func")
        return result
    return wrapper

@decorator
def beautiful_func(x, y):
    return x + y

if __name__ == "__main__":
    beautiful_func(1,2)
    beautiful_func(4,2)
    beautiful_func(3,2)
    beautiful_func(2,2)
