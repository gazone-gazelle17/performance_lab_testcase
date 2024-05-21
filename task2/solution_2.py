def circle_and_points(circle_points, single_points):
    cx, cy, r = map(float, circle_points)
    r_squared = r ** 2
    results = []

    for point in single_points:
        x, y = map(float, point.split())
        distance_squared = (x - cx) ** 2 + (y - cy) ** 2

        if distance_squared == r_squared:
            results.append(0)
        elif distance_squared < r_squared:
            results.append(1)
        else:
            results.append(2)

    return results


circle_file = open('file_one.txt', 'r')
circle_points = [line.strip() for line in circle_file]
circle_file.close()

points_file = open('file_two.txt', 'r')
single_points = [line.strip() for line in points_file]
points_file.close()

result = circle_and_points(circle_points, single_points)
print(list(n for n in result))
