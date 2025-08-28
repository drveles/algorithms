def main():
    center_x, center_y, radius = map(int, input().split())
    
    colors_in_circle = set()
    
    if abs(center_x) <= radius or abs(center_y) <= radius:
        colors_in_circle.add('black')
    
    radius_squared = radius * radius
    
    if center_x > 0 and center_y > 0:
        colors_in_circle.add('gold')
    elif center_x + radius > 0 and center_y + radius > 0:
        distance_to_quadrant = max(0, 1 - center_x) ** 2 + max(0, 1 - center_y) ** 2
        if distance_to_quadrant <= radius_squared:
            colors_in_circle.add('gold')
    
    if center_x < 0 and center_y > 0:
        colors_in_circle.add('white')
    elif center_x - radius < 0 and center_y + radius > 0:
        distance_to_quadrant = max(0, center_x + 1) ** 2 + max(0, 1 - center_y) ** 2
        if distance_to_quadrant <= radius_squared:
            colors_in_circle.add('white')
    
    if center_x < 0 and center_y < 0:
        colors_in_circle.add('blue')
    elif center_x - radius < 0 and center_y - radius < 0:
        distance_to_quadrant = max(0, center_x + 1) ** 2 + max(0, center_y + 1) ** 2
        if distance_to_quadrant <= radius_squared:
            colors_in_circle.add('blue')
    
    if center_x > 0 and center_y < 0:
        colors_in_circle.add('red')
    elif center_x + radius > 0 and center_y - radius < 0:
        distance_to_quadrant = max(0, 1 - center_x) ** 2 + max(0, center_y + 1) ** 2
        if distance_to_quadrant <= radius_squared:
            colors_in_circle.add('red')
    
    print(len(colors_in_circle))

if __name__ == "__main__":
    main()
