n = int(input())

for _ in range(n):
    line = input()
    if line.startswith("Simon says "):
        print(line[len("Simon says "):])

