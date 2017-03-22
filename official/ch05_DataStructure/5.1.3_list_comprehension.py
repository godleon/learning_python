from math import pi


SQUARES = list(map(lambda x: x**2, range(10)))
print(SQUARES)

STR_TMP = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(STR_TMP)

VEC = [-4, -2, 0, 2, 4]
STR_TMP = [x * 2 for x in VEC if x >= 0]
print(STR_TMP)

STR_TMP = [abs(x) for x in VEC]
print(STR_TMP)

FRUIT = ['  banana', '  loganberry ', 'passion fruit  ']
STR_TMP = [w.strip() for w in FRUIT]
print(STR_TMP)

VEC = [[1,2,3], [4,5,6], [7,8,9]]
STR_TMP = [num for elem in VEC for num in elem]
print(STR_TMP)

STR_TMP = [str(round(pi, i)) for i in range(1, 10)]
print(STR_TMP)
