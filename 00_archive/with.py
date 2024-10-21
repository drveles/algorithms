class ContexManager():
    def __enter__(self):
        print("entered to context manager")
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("exited from context manager")


with ContexManager() as c: 
    raise Exception("testing close context manager")
    print("inside with block")
