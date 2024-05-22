import sys
from statistics import median


def find_steps(nums):
    median_number = median(nums)
    steps = [abs(n - median_number) for n in nums]
    return sum(steps)


def main():
    if len(sys.argv) != 2:
        print("""
              Введите команду:
              python3 solution_4.py <наименование файла в текущей директории>
              или:
              python3 solution_4.py <путь к файлу>
              """
              )
        return
    file_path = sys.argv[1]
    nums = []
    with open(file_path, 'r') as file:
        for line in file:
            nums.extend(map(int, line.split()))
    result = find_steps(nums)
    print(int(result))


if __name__ == "__main__":
    main()
