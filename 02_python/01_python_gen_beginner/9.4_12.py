# Программа должна вывести символ, который появляется наиболее часто.

string = input()
most_used_symbol = '\0'
most_used_symbod_counter = 0

for i in string:
    if string.count(i) >= most_used_symbod_counter:
        most_used_symbol = i
        most_used_symbod_counter = string.count(i)

print(most_used_symbol)