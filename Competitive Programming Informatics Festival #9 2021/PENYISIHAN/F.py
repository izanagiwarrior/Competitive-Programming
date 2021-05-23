n = int(input())
for i in range(n):
    _ = input()
    listTemp = list(map(int,input().split()))
    sum = 0
    sama = False
    for i in range(1,len(listTemp)):
        if sama == False:
            if listTemp[i] != listTemp[i-1]:
                sum += 2
                sama = True
        else:
            if listTemp[i] != listTemp[i-1]:
                sum += 1
            sama = False
    print(sum)