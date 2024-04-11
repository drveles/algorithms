import bisect 

def main():
    _ = int(input())
    arr = sorted(map(int, input().split()))
    k = int(input())

    for _ in range(k):
        l, r = map(int, input().split())
        print(bisect.bisect_right(arr, r) - bisect.bisect_left(arr, l))

if __name__ == "__main__":
    main()
