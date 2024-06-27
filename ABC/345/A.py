s = input()

print("Yes" if s[0] == "<" and s[-1] == ">" and s.count("=") == len(s) - 2 else "No")
