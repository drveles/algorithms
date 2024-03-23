# Пароль является надежным если:

# его длина не менее 8 символов; 
# он содержит как минимум одну заглавную букву (верхний регистр); 
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

# объявление функции
def is_password_good(password):
    flag = True

    if len(password) < 8:
        flag = False
    if password.upper() == password or password.lower() == password:
        flag = False
    
    for i in password:
        if i in "1234567890":
            break
    else:
        flag = False

    return flag

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))