a,b = input().split()
a,b = int(a), int(b)
listT = list(map(int,input().split()))
cb = 0
price = 0
for i in range(b):
    c,d = input().split()
    c,d = int(c),int(d)
    tempCB = 0
    tempPR = 0
    for j in range(len(listT)):
        temp = listT[j] * (c/100)
        if temp > d:
            temp = d
        if j == 0:
            tempCB = temp
            tempPR = listT[j]
        else:
            if temp > tempCB:
                tempCB = temp
                tempPR = listT[j]
            elif temp == tempCB and listT[j] < listT[j-1]:
                tempCB = temp
                tempPR = listT[j]
    cb += tempCB
    price += tempPR 
    listT.remove(tempPR)
print(int(cb),price)
        
        
    