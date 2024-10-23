from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("hello from decorator")
        return func(*args, **kwargs)
    return wrapper


@decorator
def foo(int_arg: int, other_str_arg: str) -> str:
    return f"hello from func with args {int_arg},{other_str_arg}"


if __name__ == "__main__":
    print(foo(1, other_str_arg="str"))
