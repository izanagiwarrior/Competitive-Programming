import string
List = input()
List = List.upper()
splitList = List.split()
splitList2 = [i for ele in splitList for i in ele]
test_list = list(string.ascii_uppercase) 
test_list.remove("J")
newList = []
for i in splitList2:
    if i in test_list and i not in newList :
        newList.append(i)
p = 0
p2 = 0
for i in range (0,5):
    for j in range (0,5):
        
        if p < len(newList):
            print(newList[p], end = " ")
        elif p >= len(newList):
            running = True
            while running:
                if test_list[p2] in newList:
                    p2 += 1
                elif test_list[p2] == "J":
                    p2 += 1
                else:
                    print(test_list[p2], end = " ")
                    p2 += 1
                    running = False
        p += 1
    print("")