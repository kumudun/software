import geopy
# exercise 1

import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database = 'flight_game',
    user = 'root',
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

from geopy.distance import geodesic
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database = 'flight_game',
    user = 'root',
    password = 'Finland@123',
    autocommit = True
)

def get_airport_coordinates_by_icao_code(icao_code):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao_code}'"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

icao_code_1 = input("Enter icao code for airport 1: ")
coordinate_1 = get_airport_coordinates_by_icao_code(icao_code_1)
icao_code_2 = input("Enter icao code for airport 2: ")
coordinate_2 = get_airport_coordinates_by_icao_code(icao_code_2)
print(f"The distant betwween 2 airport is {geopy.distance.geodesic(coordinate_1, coordinate_2).km:.0f}km")


























