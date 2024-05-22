from statistics import median


def find_steps(nums):
    median_number = median(nums)
    steps = [abs(n - median_number) for n in nums]
    return sum(steps)


nums = []

with open('nums_file.txt', 'r') as file:
    for number in file:
        nums.extend(map(int, number.split()))
result = find_steps(nums)
print(int(result))
