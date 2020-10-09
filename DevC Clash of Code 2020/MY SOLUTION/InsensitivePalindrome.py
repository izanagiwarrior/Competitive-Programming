x = input()
if x == x[::-1]:
    print("sensitive palindrome")
elif x.lower() == x[::-1].lower():
    print("insensitive palindrome")
else:
    print("not a palindrome")