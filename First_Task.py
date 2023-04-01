def pythagorean_triangle(arr):
    arr_sq = [x ** 2 for x in arr]
    arr_sq.sort()
    for i in range(len(arr_sq) - 2):
        for j in range(i + 1, len(arr_sq) - 1):
            for k in range(j + 1, len(arr_sq)):
                if arr_sq[i] + arr_sq[j] == arr_sq[k]:
                    return True

    return False
arr = [6,10,8]
print(pythagorean_triangle(arr))
