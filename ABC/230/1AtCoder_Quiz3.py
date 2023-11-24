n = int(input())

print(f"AGC{'0' * (3 - len(str(n)))}{n if n < 42 else n+1}")
