def is_correct_bracket(text):
    open_bracket = 0
    close_bracket = 0
    flag = True

    for i in text:
        if i == '(':
            open_bracket += 1
        elif i == ')':
            close_bracket += 1
        else:
            flag = False
            break
        if close_bracket > open_bracket:
            flag = False 
            break
    if close_bracket != open_bracket: 
        flag = False 

    return flag

txt = input()

print(is_correct_bracket(txt))
