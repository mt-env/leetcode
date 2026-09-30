from operator import contains

n = int(input())

env: dict[str, list[str]] = {}
scopes: list[dict[str, str]] = []
scopes.append({})

def handle_declare(ident: str, ty: str):
    last_scope = scopes[len(scopes) - 1]
    if contains(last_scope, ident):
        print("MULTIPLE DECLARATION")
        exit(0)
    last_scope[ident] = ty

    if not contains(env, ident):
        env[ident] = []
    curr_list = env[ident]
    curr_list.append(ty)


def handle_typeof(ident: str):
    mylist = env.get(ident)
    if mylist is None or len(mylist) == 0:
        print("UNDECLARED")
        return
    print(mylist[len(mylist) - 1])

for _ in range(n):
    line = input().split()
    if line[0] == "{":
        scopes.append({})
    elif line[0] == "}":
        last_scope = scopes.pop()
        for key in last_scope:
            _ = env[key].pop()
    elif line[0] == "DECLARE":
        handle_declare(line[1], line[2])
    elif line[0] == "TYPEOF":
        handle_typeof(line[1])

