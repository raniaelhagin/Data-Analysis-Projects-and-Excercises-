c = ord(input())

if (c >= 65 and c <= 90):
    print(chr(c + 32))
elif (c >= 97 and c <= 122):
    print(chr(c - 32))