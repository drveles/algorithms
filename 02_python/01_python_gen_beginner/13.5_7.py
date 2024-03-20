def is_palindrome(text):
    flag = True

    for i in " .,!?-":
        text = text.replace(i, '')
    text = text.lower()
    if text != text[::-1]:
        flag = False

    return flag

txt = input()

print(is_palindrome(txt))
