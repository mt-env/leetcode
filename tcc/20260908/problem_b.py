correct = input()
sticky = input()
i, j = 0, 0

output: set[str] = set()

while i < len(correct) and j < len(sticky):
    if correct[i] == sticky[j]:
        i += 1
        j += 1
    else:
        output.add(sticky[j])
        while correct[i] != sticky[j]:
            j += 1

if j != len(sticky):
    output.add(sticky[len(sticky) - 1])

for item in output:
    print(item, end="")
