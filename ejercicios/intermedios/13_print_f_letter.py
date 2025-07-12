repeat_x = [5, 2, 5, 2, 2]

for repeat in repeat_x:
    xs = ""
    for i in range(repeat):
        xs += "x"
    print(xs)

repeat_y = [3, 3, 3, 3, 3, 8]

print('\n')

for x_count in repeat_y:
    ys = ""
    for i in range(x_count):
        ys += "y"
    print(ys)