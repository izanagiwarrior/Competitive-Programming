n = int(input())
res = []
for i in range(n):
    l, p = map(str, input().split())
    if (l in p) or (p in l):
        res.append("BOLEH")
    else:
        res.append("JANGAN")
for i in res:
    print(i)