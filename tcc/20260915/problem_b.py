first_line = map(int, input().split(" "))
w = next(first_line)
p = next(first_line)

partitions = list(map(int, input().split(" ")))
partitions.append(0)
partitions.append(w)

possible_widths: set[int] = set()
for i in partitions:
    for j in partitions:
        if not i == j:
            possible_widths.add(abs(i - j))

sorted = list(possible_widths)
sorted.sort()
print(" ".join(map(str, sorted)))
