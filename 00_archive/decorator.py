from functools import wraps

def decorator_with_params(parameter: str):
    def main_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'decorator {parameter=}')
            print(f'{args=},{kwargs=}')
            return func(*args, **kwargs)
        return wrapper
    return main_wrapper


@decorator_with_params('some parameter')
def foo(a, *args, **kwargs):
    print(f'Insade function with {a=}, {args}, {kwargs}')


def main():
    foo(1, 2, b=3)


if __name__ == '__main__':
    main()
