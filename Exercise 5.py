# exercise 1

import random
num_dice = int(input("Enter how many dice to roll: "))
total_sum = 0
for i in range(num_dice):
    roll = random.randint(1, 6)
    total_sum = total_sum + roll
    print(f"The sum of the dice rolled is :{total_sum}")

# exercise 2

numbers = []

number = input("Enter the first number or quit by pressing Enter: ")
while number != "":
    numbers.append(number)
    number = input("Enter the next number or quit by pressing Enter: ")
numbers.sort(reverse=True)
top_five = numbers[:5]
print("The five greatest numbers are:", top_five)


# exercise 3
num = int(input("Enter an integer number: "))
if num > 1:
    for i in range(2 , num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# exercise 4

cities = []

for i in range(5):
    city = input(f"Enter a city name {i+1}: ")
    cities.append(city)

print("The cities you entered are:")
for city in cities:
    print(city)

