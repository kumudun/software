
# exercise 1

seasons = ("winter", "spring", "summer", "Autumn")

def get_season(month):
    if month in (12,1,2):
        return seasons[0]
    elif month in (3,4,5):
        return seasons[1]
    elif month in (6,7,8):
        return seasons[2]
    else:
        return seasons[3]
month = int(input("Enter a month(1-12): "))
print(get_season(month))


# exercise 2
names = set()

while True:
    name = input("Enter a name or press enter to stop: ")
    if name == "" :
        break
    if name in names:
        print("existing name")
    else:
        names.add(name)
        print(" new names")

    print("\nlist of name entered")
    for name in names:
        print(name)


# exercise 3
airport_data = {}

# Function to add a new airport
def add_airport():
    icao_code = input("Enter the ICAO code of the airport: ").upper().strip()
    if icao_code in airport_data:
        print("This airport already exists.")
    else:
        airport_name = input("Enter the name of the airport: ").strip()
        airport_data[icao_code] = airport_name
        print("Airport added successfully.")
def fetch_airport():
    icao_code = input("Enter the ICAO code of the airport to fetch: ").upper().strip()
    if icao_code in airport_data:
        print(f"The name of the airport with ICAO code {icao_code} is: {airport_data[icao_code]}")
    else:
        print("Airport not found.")
        choice = input("Choose an option (1, 2, or 3): ").strip()

        if choice == "1":
            add_airport()
        elif choice == "2":
            fetch_airport()
        elif choice == "3":
            "break"

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

