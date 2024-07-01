# OK
import sys


def main():
    A = int(input())
    B = int(input())
    N = int(input())

    B = (B // N) + (1 if B % N else 0)

    if A > B:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
