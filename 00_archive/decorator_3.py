def decor(func):
    def wrapper(*args, **kwargs):
        print("Inside decor")
        return func(*args, **kwargs)
    return wrapper

@decor
def func():
    print("Inside func")

if __name__ == "__main__":
    func()
