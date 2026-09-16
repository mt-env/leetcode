# incomplete

first_line = map(int, input())
n = next(first_line)
q = next(first_line)

vertices: list[tuple[int, int]] = []
for _ in range(n):
    line = map(int, input())
    vertices.append((next(line), next(line)))

pixels: list[tuple[int, int]] = []
for _ in range(q):
    line = map(int, input())
    pixels.append((next(line), next(line)))


