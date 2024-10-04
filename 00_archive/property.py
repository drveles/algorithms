class Class:
    """
    Example class
    """
    def __init__(self):
        self._atribute = "i am atribute"
        self.test = "test"

    @property
    def method(self):
        print("method:", self._atribute)

    @method.setter
    def method(self, new):
        self._atribute = new

    @method.deleter
    def method(self):
        print("method: i am clearing now")
        self._atribute = ""


if __name__ == "__main__":
    c = Class()
    c.method
    c.method = "now i am method"
    c.method
    del c.method
    c.method
    print(c.__doc__)