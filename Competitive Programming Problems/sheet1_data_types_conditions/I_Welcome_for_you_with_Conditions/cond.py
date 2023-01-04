numbers = input().split()

a, b = [int(n) for n in numbers]

if a >= b:
    print("Yes")
else:
    print("No")