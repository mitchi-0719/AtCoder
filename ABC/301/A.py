n = int(input())
s = input()

if n - s.count("A") < n/2:
    print("A")
elif n - s.count("T") < n/2:
    print("T")
else:
    if s[-1] == "A":
        print("T")
    else:
        print("A")