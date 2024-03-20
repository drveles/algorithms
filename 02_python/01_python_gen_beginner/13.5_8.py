def is_palindrome(text):
    flag = True

    for i in " .,!?-":
        text = text.replace(i, '')
    text = text.lower()
    if text != text[::-1]:
        flag = False

    return flag

def is_prime(num):
    result = True
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            result = False
            break

    return result


def is_valid_password(password):
    flag = True
    password = password.split(':')

    if len(password) > 3:
        flag = False
    elif not is_palindrome(password[0]):
        flag = False
    elif not is_prime(int(password[1])):
        flag = False
    elif int(password[2]) % 2 != 0:
        flag = False

    return flag

psw = input()

print(is_valid_password(psw))