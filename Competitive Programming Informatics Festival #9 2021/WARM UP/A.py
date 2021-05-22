berapa=int(input())
for i in range(berapa):
    count=0
    aha=list(map(str, input().split()))
    bInt=int(aha[1])
    aInt=int(aha[0])
    hitung=aInt
    while hitung<=bInt:
        hitung=str(hitung)
        if hitung[-1]=="3" or hitung[-1]=="4":
            count+=1
            # print(hitung)
            hitung=int(hitung)
            hitung+=1
            # if hitung[-1]=="3":
            #     hitung=int(hitung)
            #     hitung+=1
            # elif hitung[-1]=="4":
            #     hitung=int(hitung)
            #     hitung+=9
        else:
            hitung=int(hitung)
            hitung+=1
        hitung=int(hitung)
    print(count)