def main():
    words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']

    myset = {string[:1].lower() for string in words}
    print(*sorted(myset))

if __name__ == "__main__":
    main()
