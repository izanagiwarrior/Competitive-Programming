def printout(A,B):
    # A -> mulai duluan
    for i in range(len(B)):
        print(min(A),end=" ")
        A.remove(min(A))
        print(min(B),end=" ")
        B.remove(min(B))
    print(min(A),end=" ")

n = int(input())
lol = list(map(int,input().split()))
lol_genap = []
lol_ganjil = []
for i in lol:
    if i % 2 == 0:
        lol_genap.append(i)
    else:
        lol_ganjil.append(i)
if len(lol_genap) > len(lol_ganjil):
    printout(lol_genap,lol_ganjil)
elif len(lol_genap) < len(lol_ganjil):
    printout(lol_ganjil,lol_genap)
else:
    A = lol_genap
    B = lol_ganjil
    for i in range(len(B)):
        print(min(A),end=" ")
        A.remove(min(A))
        print(min(B),end=" ")
        B.remove(min(B))
    
    

