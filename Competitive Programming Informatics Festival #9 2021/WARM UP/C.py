#Soal C
n = list(map(int, input().split()))
n = list(dict.fromkeys(n))
for i in range(0, len(n)-1):
    for j in range(i+1, len(n)):
        if abs(n[i] - n[j]) == 1:
            print(min(n[i], n[j]), max(n[i], n[j]))