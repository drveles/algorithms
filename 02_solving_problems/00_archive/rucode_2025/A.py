def main():
    first_number = int(input())
    second_number = int(input())
    
    remainder = first_number % second_number
    remainder *= 10
    first_digit_after_decimal = remainder // second_number
    
    print(first_digit_after_decimal)

if __name__ == "__main__":
    main()
