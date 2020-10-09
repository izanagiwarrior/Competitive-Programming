x = int(input())
sum = 0
ar = list(map(int, input().rstrip().split()))
ar2 = []
for i in range(len(ar)):
    sum = sum + ar[i]
    ar2.append(sum)
print(max(ar2))