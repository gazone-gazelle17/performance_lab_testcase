def circular_array(n, m):
    n_list = list(range(1, n + 1))
    arrays = []
    index = 0
    while True:
        short_list = [n_list[(index + i) % n] for i in range(m)]
        arrays.append(short_list[0])
        index = (index + m - 1) % n
        if index == 0 and len(arrays) > 1:
            break
    return arrays


n, m = map(int, input().split())
resulting_array = circular_array(n, m)
print("".join(map(str, resulting_array)))
