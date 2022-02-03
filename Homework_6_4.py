from math import pi
x = str(pi)
length = []
for i in x:
    length.append(str(i))
    if 3 < len(length) < 14:
        print("".join(length))
