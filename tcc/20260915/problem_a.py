n = int(input())

# bool: true if end of interval, false if start
# intervals: list[tuple[int, int]] = []
events: list[tuple[int, bool]] = []
for _ in range(n):
    line = map(int, input().split(" "))
    start = next(line)
    end = next(line)
    # print(f"{start} {end}")
    # intervals.append((start, end))
    events.append((start, False))
    events.append((end, True))

events.sort()
days = 0
active = 0
curr_start = 0
for (time, is_end) in events:
    if not is_end:
        if active == 0:
            curr_start = time
        active += 1
    elif is_end:
        active -= 1
        if active == 0:
            days += time - curr_start + 1
    # print(f"time: {time}, is_start: {is_end}, curr_start: {curr_start}, days: {days}")

print(days)
