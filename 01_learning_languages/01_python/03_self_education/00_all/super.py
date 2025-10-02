class FirstClass:
    def __init__(self):
        self.first = 1


class SecondClass(FirstClass):
    def __init__(self, parameter: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.second = 2
        self.parameter = parameter

    def print_all(self):
        print(self.first)
        print(self.second)
        print(self.parameter)


if __name__ == "__main__":
    s = SecondClass("test")
    s.print_all()
