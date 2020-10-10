n = int(input())
x = "{0:b}".format(n)
running = True
while running:
    if '01' in x:
        x = x.replace('01', '')
    elif '10' in x:
        x = x.replace('10', '')
    else:
        running = False
if "1" not in x:
    print(len(x))
else:
    def binerKeDesimal(biner):
        pangkat = len(biner) - 1
        desimal = 0
        for i in range(len(biner)):
            iBin = int(biner[i])
            iDes = iBin * (2**pangkat)
            desimal += iDes
            pangkat -= 1
        return desimal
    print(binerKeDesimal(x))