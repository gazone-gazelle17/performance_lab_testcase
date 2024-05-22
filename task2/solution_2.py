import sys


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


def read_points_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def main():
    if len(sys.argv) != 3:
        print("""
              Введите команду:
              python3 solution_2.py <circle_file> <points_file>
              """
              )
        return
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    circle_points = read_points_from_file(circle_file)
    if len(circle_points) == 2:
        circle_points = circle_points[0].split() + [circle_points[1]]
    else:
        circle_points = circle_points[0].split() + circle_points[1:]
    single_points = read_points_from_file(points_file)
    result = circle_and_points(circle_points, single_points)
    for n in result:
        print(n)


if __name__ == '__main__':
    main()
