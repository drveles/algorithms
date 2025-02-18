def convert_to_python_case(text):
    text = list(text)
    
    for id in range(len(text) - 1, -1, -1):
        if text[id].isupper():
            text[id] = text[id].lower()
            if id != 0:
                text.insert(id,'_')

    return text

txt = input()

print(*convert_to_python_case(txt), sep='')