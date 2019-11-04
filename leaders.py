a = [16, 19, 4, 3, 8, 3]
leaders= []
for i in range(len(a)):
    if max(a[i:])==a[i]:
        leaders.append(a[i])

print(leaders)
