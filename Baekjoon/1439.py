s = input()

count = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count += 1

print(round((count + 0.5) / 2))
