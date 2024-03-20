# объявление функции
def is_one_away(word1, word2):
    flag = False

    if len(word1) == len(word2):
        count_difference = 0  
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count_difference += 1
                if count_difference == 1:
                    flag = True
                else:
                    flag = False
                    break

    return flag

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
