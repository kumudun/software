import random
import math
# Module 2



# Exercise 2
radius =float(input("what is your radius of the circle? "))
print(f"Area of the circle is {math.pi*radius**2:2f}")

# Exercise 3
rec_length = float(input("What is the length of the rectangle? "))
rec_width = float(input("What is the width of the rectangle? "))
peri_rec =2*rec_length + 2*rec_width
area_rec = rec_length*rec_width
print(f"The perimeter of the rectangle is :{peri_rec:1f}")
print(f"The area of the rectangle is :{area_rec:1f}")

# Exercise 4
num1 =int(input("Give three integer number:"))
num2 =int(input())
num3 =int(input())
print(f"sum of 3 numbers is{num1+num2+num3} , product{num1*num2*num3} , average{(num1+num2+num3)/3}")

# Exercise 5
talents =float(input("Enter talents:"))
pounds =float(input("Enter pounds:"))
lots =float(input("Enter lots:"))
kg_weight =((talents*20 + pounds)*32+lots)*0.0133
gr_weight =1000.0*(kg_weight-int(kg_weight))
print(f"The weight in modern units: \n {int(kg_weight)}kilograms and {gr_weight:2f}grams")

 # Exercise 6
number1 = random.randint(0,9)
number2 = random.randint(0,9)
number3 = random.randint(0,9)
print(F"first combination:{number1} ,{number2} ,{number3}")

number4 = random.randint(1,6)
number5 = random.randint(1,6)
number6 = random.randint(1,6)
number7 = random.randint(1,6)
print(f"second combination:{number4} ,{number5} ,{number6} ,{number7}")

