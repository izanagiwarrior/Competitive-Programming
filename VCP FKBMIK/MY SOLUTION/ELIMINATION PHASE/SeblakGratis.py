n = input()
x = n.split()
n1 = int(x[0])
s = int(x[1])
c1 = 0
for i in range(n1):
    y = input()
    y1 = y.split()
    if y1[0] == "+":
        s += int(y1[1])
    else:
        if (s - int(y1[1])) < 0 :
            c1 += 1
        else:
            s -= int(y1[1])
print(s, c1)