#正解

n = int(input())

if n < 42:
    if len(str(n)) == 1:
        print("AGC" + "00" + str(n))
    else:
        print("AGC" + "0" + str(n))
else:
    print("AGC" + "0" + str(n + 1))