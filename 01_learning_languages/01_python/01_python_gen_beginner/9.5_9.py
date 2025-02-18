#  n (1≤ n≤ 25) – сдвиг, во второй строке даётся закодированное сообщение в виде строки со строчными латинскими буквами.

shift_value = int(input())
cesar_string = input()

for i in cesar_string:
    if (ord(i) - 96 - shift_value) >= 0:
        print((chr(96 + ((ord(i) - 96) - shift_value))), end="")
    else:
        print((chr(96 + (ord(i) - 96 - shift_value + 26))), end="")
