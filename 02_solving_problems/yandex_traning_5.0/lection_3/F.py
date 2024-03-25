def main():
    set_1 = input().split()
    list_2 = input().split()

    for el in set_1:
        for el2 in set_1:
            if len(el) < len(el2) and el2[:len(el)]:
                set_1.remove(el2)

    for list_2_id, list_2_el  in enumerate(list_2):
        for set_1_el in set_1:
            if list_2_el[:len(set_1_el)] == set_1_el:
                list_2[list_2_id] = set_1_el
    
    print(*list_2, end='')
    print()

if __name__ == "__main__":
    main()
