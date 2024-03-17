fors_flag = 0

for i in range(10_001_000):
    counter_cube_combination = 0
    for j in range(1, 33):
        for k in range(1, 33): 
            if j ** 3 + k ** 3 == i :
                for l in range(1, 33):
                    for m in range(1, 33): 
                        if l ** 3 + m ** 3 == i and l != j and l != k and m != j and m != k :
                            counter_cube_combination += 1
    if counter_cube_combination > 0:
        print(i)
        fors_flag += 1
    if fors_flag >= 5:
        break

# OK 