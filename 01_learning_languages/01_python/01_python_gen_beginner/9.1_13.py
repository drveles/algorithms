string = input()
counter_glass_letter = 0
counter_soglass_letter = 0

for i in string:
    if i in "ауоыиэяюеАУОЫИЭЯЮЕ":
        counter_glass_letter += 1
    if i in "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ":
        counter_soglass_letter += 1
print("Количество гласных букв равно", counter_glass_letter)
print("Количество согласных букв равно", counter_soglass_letter)

# Количество гласных букв равно 25
# Количество согласных букв равно 24

# бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ
# ауоыиэяюёеАУОЫИЭЯЮЁЕ
