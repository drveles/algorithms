from functools import wraps


def decorator_without_params(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Inside decorator_without_params")
        return func(*args, **kwargs)
    return wrapper


def decorator_with_params(repeat_times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(repeat_times):
                print("Inside decorator_with_params")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@decorator_with_params(3)
@decorator_without_params
def funciton(message: str = "Hello from function"):
    print(message)


if __name__ == "__main__":
    funciton()
