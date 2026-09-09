from math import ceil


n = int(input())
pizza_leftovers: list[tuple[str, int]] = []
for _ in range(n):
    foo = input().split(" ")
    pizza_leftovers.append((foo[0], int(foo[1])))

small_slices = 0
med_slices = 0
large_slices = 0
for (size, remainder) in pizza_leftovers:
    if size == "S":
        small_slices += remainder
    elif size == "M":
        med_slices += remainder
    else:
        large_slices += remainder

print(
    ceil(small_slices / 6) +
        ceil(med_slices / 8) +
        ceil(large_slices / 12)
)
