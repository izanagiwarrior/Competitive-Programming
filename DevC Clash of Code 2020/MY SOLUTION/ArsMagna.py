a,b = input().split()
a = int(a)
b = int(b)
first = []
second = []

for i in range(a):
    x = input()
    x = ''.join(sorted(x))
    first.append(x)

for i in range(b):
    x = input()
    x = ''.join(sorted(x))
    second.append(x)

same = set(first).intersection(set(second))
jumlah = 0
for data in same:
    jumlah = jumlah + (first.count(data)*second.count(data))
print(jumlah)