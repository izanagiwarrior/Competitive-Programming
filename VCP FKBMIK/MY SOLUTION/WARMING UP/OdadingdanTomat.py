import numpy as np
jumlahKasus = int(input())
for i in range(0,jumlahKasus):
    b1 = input()
    listB1 = b1.split()
    newb3 = []
    newb4 = []
    total = 0
    total = float(total)
    if int(listB1[0]) > 100:
        total = -1.000
        print("{:.3f}".format(round(total, 3)))
        break
    elif int(listB1[1]) > 1000:
        total = -1.000
        print("{:.3f}".format(round(total, 3)))
        break
    elif int(listB1[1]) > 100 and int(listB1[1]) < 2:
        total = -1.000
        print("{:.3f}".format(round(total, 3)))
        break
    else:
        for j in range (0,int(listB1[2])):
            if j < 2:
                b3 = []
                b4 = []
                b2 = input()
                listB2 = b2.split()
                b3.append(int(listB2[0]))
                b3.append(int(listB2[1]))
                b4.append(int(listB2[2]))
                newb3.append(b3)
                newb4.append(b4)
            else:
                b2 = input()
                pass
    A = np.array(newb3)
    B = np.array(newb4)
    x = np.linalg.solve(A, B)  
    f1 = float(x[0])
    f2 = float(x[1])
    f3 = float(listB1[0])
    f4 = float(listB1[1])
    total = (f3*f1) + (f4*f2)
    print("{:.3f}".format(round(total, 3)))