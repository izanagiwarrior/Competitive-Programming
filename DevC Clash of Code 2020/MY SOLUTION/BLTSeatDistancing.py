s, k ,p = input().split()
s = int(s)
k = int(k)
p = int(p)
for i in range(1,k+1): 
    if i % 2 == 1:
        for i in range(0,s):
            for i in range(1,p+1):
                if i % 2 == 1:
                    for i in range(0,s):
                        print("*", end = "")
                else:
                    for i in range(0,s):
                        print(" ", end = "")
            print("")
    else:
        for i in range(0,s):
            for i in range(1,p+1):
                if i % 2 == 1:
                    for i in range(0,s):
                        print(" ", end = "")
                else:
                    for i in range(0,s):
                        print("*", end = "")
            print("")