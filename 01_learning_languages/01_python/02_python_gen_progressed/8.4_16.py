#На вход программе подается строка, состоящая из трех слов. 
#Верно ли, что для записи всех трех слов был использован один и тот же набор букв?
first_str_set, second_str_set, third_str_set = map(set, input().split())

print("YES" if first_str_set == second_str_set == third_str_set else "NO")
