text_list = input().split('#')

for i in range(int(text_list[1])):
    string = input()
    if '#' in string:
        string = string[:string.index('#')]
    print(string.rstrip())
