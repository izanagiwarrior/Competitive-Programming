plain = ["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x","y", "z"]
chiper = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

n = int(input())
ans2 = []
for i in range(n):
    lol = input().split()
    ans = []
    for i in lol:
        if "(‘" in i and "’)" in i:
            ans.append(i)
        else:
            temp = []
            for j in i:
                if j in plain:
                    temp.append(chiper[plain.index(j)])
                else:
                    temp.append(j)
            ans.append(''.join(temp))
    ans2.append(ans)
for i in ans2:
    print(*i)

