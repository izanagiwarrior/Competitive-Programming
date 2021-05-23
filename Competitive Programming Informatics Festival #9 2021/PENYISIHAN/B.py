A,B = input().split()
A,B = int(A), int(B)
temp = [x for x in range(1,A+1)]
tempB= B
# B -= 1
while len(temp) > 1:
    while B > len(temp):
        B -= len(temp)
    temp.pop(B-1)
    B += tempB - 1 
print(temp[0])