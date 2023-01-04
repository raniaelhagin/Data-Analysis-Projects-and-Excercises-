numbers = input().split()

a, b = [int(n) for n in numbers]

if (a % b == 0) or (b % a == 0):
    print("Multiples")

else:
    print("No Multiples")
