stock_num = int(input())
n = stock_num
# количество цифр 3 в нем;
counter_3_digit = 0
# сколько раз в нем встречается последняя цифра;
last_digit_of_stock = stock_num % 10
counter_last_digit = 0
# количество четных цифр;
counter_even_digit = 0
# сумму его цифр, больших пяти;
sum_digits_greater_5 = 0
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
multip_digit_greater_7 = 1
# сколько раз в нем встречаются цифры 0 и 5 (всего суммарно).
counter_0_5_digit = 0

while n > 0:
    last_digit = n % 10
    if last_digit == 3:
        counter_3_digit += 1
    if last_digit == last_digit_of_stock:
        counter_last_digit += 1
    if last_digit % 2 == 0:
        counter_even_digit += 1
    if last_digit > 5:
        sum_digits_greater_5 += last_digit
    if last_digit > 7:
        multip_digit_greater_7 *= last_digit
    if last_digit in (0, 5):
        counter_0_5_digit += 1
    n //= 10

print(
    counter_3_digit,
    counter_last_digit,
    counter_even_digit,
    sum_digits_greater_5,
    multip_digit_greater_7,
    counter_0_5_digit,
    sep="\n",
    end="",
)

# OK 
