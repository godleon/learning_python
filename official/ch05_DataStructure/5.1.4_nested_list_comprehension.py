
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

STR_TMP = [[row[i] for row in matrix] for i in range(4)]
print(STR_TMP)


print(list(zip(*matrix)))
