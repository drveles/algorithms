# На вход программе подается строка, состоящая из цифр. Необходимо определить, верно ли, что в ее записи ни одна из цифр не повторяется?

stock_input_str = input()

print("YES" if len(stock_input_str) == len(set(stock_input_str)) else "NO")
