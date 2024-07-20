def main():
    n, _ = map(int, input().split())
    bus_stops = list(map(int, input().split()))
    bus_locations = list(map(int, input().split()))
    left = 0
    right = n - 1

    for location in bus_locations:
        while not bus_stops[left] <= location < bus_stops[right] or left < right:
            mid = (right - left) // 2 
            if bus_stops[left] < location and bus_stops[right] < location:
                left = mid
            else:
                right = mid
        print(left + 1 if abs(bus_stops[left] - location) <= abs(bus_stops[right] - location) else right + 1)


if __name__ == "__main__":
    main()


#WA + TL