stock_string = input()
counter_lowercase = 0

for i in stock_string:
    if i == i.lower() and i.lower() in "abcdefghijklmnopqrstuvwxyz":
        counter_lowercase += 1
print(counter_lowercase)