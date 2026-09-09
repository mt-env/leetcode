first_line = input().split(" ")
n = int(first_line[0])
k = int(first_line[1])

joined_at: dict[int, int] = {}
left_at: dict[int, int] = {}

for i in range(25):
    joined_at[i] = 0
    left_at[i] = 0

intervals: list[tuple[int, bool]] = []
for i in range(n):
    line = map(int, input().split(" "))
    joined_at[next(line)] += 1
    left_at[next(line)] += 1

num_hours = 0
curr_count = 0
for i in range(25):
    curr_count -= left_at[i]
    curr_count += joined_at[i]
    if curr_count >= k:
        num_hours += 1

print(num_hours)
