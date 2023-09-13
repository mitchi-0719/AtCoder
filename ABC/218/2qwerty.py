P = list(map(int, input().split()))

sentence = ""
for i in P:
    sentence += chr(i+96)
print(sentence)