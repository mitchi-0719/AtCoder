# 解説AC

s = input()
stack = []

for si in s:
    stack.append(si)
    if stack[-3:] == ["A", "B", "C"]:
        for i in range(3):
            stack.pop()

print("".join(stack))
