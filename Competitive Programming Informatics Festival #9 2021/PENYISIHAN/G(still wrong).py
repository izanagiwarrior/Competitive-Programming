plat=['AA','BB','BL','BK','BA','BM','BP','BG','BN','BE','BD','BH',
      'AA','AD','AB','AG','AE','DK','DR','EA','DH','EB','ED','KB',
      'DA','KH','KT','KU','DB','DL','DM','DN','DD','DC','DT','DE',
      'DG','DS','PB']
n = int(input())
for i in range(n):
    temp = input()
    listTemp = []
    sum = 0
    # depan
    for i in range(len(temp)-1):
        for j in range(i+1,len(temp)):
            if (temp[i] + temp[j]) in plat:
                listTemp.append(temp[i] + temp[j])
    #belakang
    for i in range(len(temp)-1,0,-1):
        for j in range(i-1,-1,-1):
            if (temp[i] + temp[j]) in plat:
                listTemp.append(temp[i] + temp[j])

    sum = len(set(listTemp).intersection(set(plat)))
    print(sum)
