numbers = input().split()

numbers = [int(n) for n in numbers]

print((numbers[0]%10 + numbers[1]%10))