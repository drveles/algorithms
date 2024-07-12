def main():
    n, k = map(int, input().split())
    my_tuple = tuple(map(int, input().split()))
    my_dict = {}
    print_flag = False

    for id, el in enumerate(my_tuple):
        if el in my_dict:
            my_dict[el][1] = my_dict[el][0] - id
            my_dict[el][0] = id
        else:
            my_dict[el] = [id, 0]

    for val in my_dict.values():
        if -k <= val[1] < 0:
            print_flag = True
            break

    if print_flag:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()

# OK