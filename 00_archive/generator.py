def generator(len: int):
    for el in range(len):
        yield el + 1

iterator = generator(10)

for _ in range(5):
    print(iterator.__next__())