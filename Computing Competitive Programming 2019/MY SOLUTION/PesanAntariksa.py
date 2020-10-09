def x(z):
    if z >= 1:
        x(z//2)
        print(z%2, end="")
n = int(input())
a=0
b=2
if 1 <= n <= 1000000:
    if n > 1:
        for i in range(n-1):
            a+=b
            b+=2
        x(a)
    else:
        print(0)