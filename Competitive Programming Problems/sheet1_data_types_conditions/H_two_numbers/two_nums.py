import math 

numbers = input().split()
numbers = [int(n) for n in numbers]

print(f"floor {numbers[0]} / {numbers[1]} = {math.floor(numbers[0] / numbers[1])}")
print(f"ceil {numbers[0]} / {numbers[1]} = {math.ceil(numbers[0] / numbers[1])}")
print(f"round {numbers[0]} / {numbers[1]} = {round(int(numbers[0] / numbers[1] + 0.5))}")