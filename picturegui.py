picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

st = ""
for ls in picture:
    for char in ls:
        if char == 0:
            st += " "
        else:
            st += "*"
    print(st)
    st = ""

# another option:

for ls in picture:
    for char in ls:
        if char == 0:
            print(" ", end="")
        else:
            print("*", end="")
    print()
