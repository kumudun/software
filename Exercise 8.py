
# exercise 1

import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database = 'flight_game',
    user = 'kumud',
    password = 'Finland@123',
    autocommit = True
)

def get_airport_by_icao(icao):
    sql = f"SELECT name,municipality FROM airport WHERE ident = %s"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchall()
    return result

code = input("Enter icao code: ")
airport = get_airport_by_icao(code)
if airport is None:
    print("No airport Found")
else:
    print(f'{airport["name"]} is located in {airport["municipality"]}')

# exercise 2

def find_airport_by_country(country):
    sql = "SELECT type,COUNT (*)FROM airport WHERE iso_country = '" + country + "'" + "GROUP BY type"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount == 0:
        for row in result:
            print(f"Airport type {row[3]},there are {row[4]} of them")
        else:
            print("No airport found")
        return
    type = input("Enter country name: ")
    find_airport_by_country(type)

# exercise 3

cursor = connection.cursor()
icao_code1 = input("Enter icao code of the first airport: ")
icao_code2 = input("Enter icao code of the second airport: ")
command = f"SELECT ident,latitude_deg,longitude_deg FROM airport WHERE ident = "icao_code1"
cursor.execute(command)
location1 = cursor.fetchall()
command = f"SELECT ident,latitude_deg,longitude_deg FROM airport WHERE ident = "icao_code2"
location2 = cursor.fetchall()
if len(location1) == 0 or len(location2)==0:
    print("One or both of the airport are not found")
else:
    airport_name = location1[0][0]
    airpot1_coo = location1[0][1],location1[0][2]

    airport_name2 = location2[0][0]
    airpot2_coo = location2[0][1],location2[0][2]

    distance_result = distance_calculator.distance(location1[0][1], location2[0][2])
    print(f"The distance between {location1[0][0]} and {location2[0][0]} is {distance_result}")










