#正解

s = input()

dictionary = []
i = 0

while i < len(s):
    if s[i].isupper():
        j = i+1
        while not s[j].isupper():
            j += 1
        dictionary.append(s[i:j+1])
        i = j+1
    else:
        i += 1

nums = [i for i in range(len(dictionary))]
copy_dict = [dictionary[i].upper() for i in range(len(dictionary))]

copy_dict, nums = zip(*sorted(zip(copy_dict, nums)))

sentence = ""
for i in range(len(dictionary)):
    sentence += dictionary[nums[i]]
print(sentence)