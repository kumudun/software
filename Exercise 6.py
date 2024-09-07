import random
import math

# exercise 1
def roll_dice():
    return random.randint(1, 6)

while True:
    dice = roll_dice()
    print(f"Dice's eyes are: {dice}")
    if dice == 6:
        break  


# exercise 2
def roll_dice_side(num):
    return random.randint(1, num)

num = int(input("How many sides in your dice? "))
while True:
    dice = roll_dice_side(num)
    print(f"Dice's sides are: {dice}")
    if dice == num:
        break


# exercise 3
def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters
while True:
    gallons = float(input("Enter the volume in gallons (negative value to stop): "))
    if gallons < 0:
        print("Negative value entered. Stopping the program.")
        break
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons is equal to {liters:.2f} liters.")


# exercise 4
def sum (num_list):
     total_sum = 0
     for i in num_list:
         total_sum += i
     return total_sum
ex_list =[]
for number in range (10):
     ex_list.append(random.randint(1, 10))
print(f"The list of numbers is:")

for i in range(len(ex_list)):
    print(ex_list[i], end=" ")

print(f"\n The sum of all items in the list is: {sum(ex_list)}")


# exercise 5
def make_even(num_list):
    result = []
    for i in range(len(num_list)):
        if num_list [i] % 2 == 0:
            result.append(num_list[i])
    return result

def print_list (message,num_list):
    print(message,end=" ")
    for i in range(len(num_list)):
        print(num_list[i],end=" ")

example_list =[]
for n in range(10):
    example_list.append(random.randint(1,100))
print_list = ("Orginallist",example_list)
new_list = make_even(example_list)
print_list("Only even number list",new_list)


# exercise 6
def pizza_efficiency(d,price):
    return price/math.pi * (d/200.)**2

p1_diameter = float(input("What is the diameter of the 1st pizza(in cm)? : "))
p1_price = float(input("What is the price of the 1st pizza(in euros)? : "))
p2_diameter = float(input("What is the diameter of the 2nd pizza(in cm)? : "))
p2_price = float(input("What is the price of the 2nd pizza(in euros)? : "))

if pizza_efficiency(p1_diameter,p1_price) < pizza_efficiency(p2_diameter,p2_price):
    print("The first pizza is a better choice!")
else:
    print("The second pizza is a better choice!")








