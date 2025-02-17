class CustomContextManager():
    _opened_file = None

    def __enter__(self):
        print('Entered')
        
    def __exit__(self, type, value, traceback):
        print('Exited')


def main():
    with CustomContextManager(): 
        print('In context block')


if __name__ == '__main__':
    main()
