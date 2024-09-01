# exercise 1

num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1

# exercise 2

def inches_to_cm(inches):
    return inches * 2.54

while True:
    inches = float(input("Enter the value in inches (negative value to stop): "))
    if inches < 0:
        print("Program ended.")
        break
    cm = inches_to_cm(inches)
    print(f"{inches} inches is equal to {cm} centimeters.")


# exercise 3
Largest =0
smallest =0

while True:
    num =input("Enter a number: ")
    if num == "":
        break
        num = int(num)
        continue
    if Largest is 0:
        Largest = num
    elif Largest < num:
        Largest = num
    if smallest is 0:
        smallest = num
    elif smallest > num:
        smallest = num

        print("Maximum is", Largest)
        print("Minimum is", smallest)


# exercise 4
import random
random = random.randint(0,10)

while True:
    num_input = int(input("Enter a number: "))
    if num_input > random:
        print("Too high")
    elif num_input < random:
        print("Too low")
    else:
        print("Correct")


# exercise 5
username = "python"
password = "rules"
num_tries = 5

while num_tries > 0:
     name = input("Enter your username: ")
     pas = input("Enter your password: ")
     if name == username and pas == password:
         print("Welcome")
         break

     num_tries = num_tries - 1 # num_tries -=1

else:
     print("Access denied")

# exercise 6
import random
import math
random_points = int(input("How many random points to be generated ? "))
inside_points = 0
i = 0
while i < random_points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside_points += 1

    i += 1
pi = 4* inside_points / random_points
print(f"pi estimation is {pi},the difference with math pi is:{math.pi-pi}")

