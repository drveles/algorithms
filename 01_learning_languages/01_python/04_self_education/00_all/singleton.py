class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


assert Singleton() is Singleton()
assert isinstance(Singleton(), Singleton)
