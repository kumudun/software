# exercise 1
length_zander =float(input("Enter a length of zander in centimeters: "))
size_limit = 42
if size_limit >= length_zander :
    print("release the fish back")
difference = size_limit - length_zander
print(f"THe difference is {difference :1f}centimeters below the limit")

#exercise 2
cabin_class =input("Enter a cabin class(LUX,A,B,C):").strip().upper()
if cabin_class == "LUX":
    print("upper_deck cabin with a balcony")
elif cabin_class == "A":
    print("above the car deck,equipped with a window")
elif cabin_class == "B":
    print("windows cabin above the car deck")
elif cabin_class =="C":
    print("windows cabin below the car deck")
else:
    print("Invalid cabin class")


# exercise 3
gender = input("Enter your biological gender (male or female): ").strip().lower()
hemoglobin = float(input("Enter your hemoglobin value (g/l): "))
if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin value is low.")
    elif 117 <= hemoglobin <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin value is low.")
    elif 134 <= hemoglobin <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")

# exercise 4
year = int(input("Enter a year: "))
if (year /4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(f"{year} is a leap year")








