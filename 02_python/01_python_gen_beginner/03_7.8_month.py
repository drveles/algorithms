for i in range(1, 13):
    for j in range(0, 12):
        for k in range(0, 12):
            if (i * 28 + j * 30 + k * 31 == 365):
                print("i == ", i, "j ==", j, "k ==", k)