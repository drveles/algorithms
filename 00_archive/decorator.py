from functools import wraps

def decorator_with_params(parameter: str):
    def main_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'decorator {parameter=}')
            print(f'{args=},{kwargs=}')
            return func(args, kwargs)
        return wrapper
    return main_wrapper


@decorator_with_params('some parameter')
def foo(kwarg):
    print(f'Insade function with {kwarg=}')


def main():
    foo('arg', kwarg='kwarg')


if __name__ == '__main__':
    main()
