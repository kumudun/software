
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

from geopy.distance import geodesic
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database = 'flight_game',
    user = 'kumud',
    password = 'Finland@123',
    autocommit = True
)
cursor = connection.cursor()

if connection.is_connected():
    print("Connected to MariaDB")

def main():
    ICAO_CODE = input("Enter ICAO code: ").upper()
    selectQuery = ("SELECT ap.latitude_deg as la_deg,ap.longitude_deg as lo_deg,c.name as country_name"
                   "FROM airport ap"
                   "join country c on ap.iso_country = c.iso_country"
                   "where ap.ident = %s")
    cursor.execute(selectQuery, (ICAO_CODE,))
    result = cursor.fetchall()

    ICAO_CODE2 =input("Enter ICAO code2: ").upper()
    selectQuery2 = ("SELECT ap.latitude_deg as la_deg,ap.longitude_deg as lo_deg,c.name as country_name"
                    "FROM airport ap"
                    "join country c on ap.iso_country = c.iso_country"
                    "where ap.ident = %s")

    cursor.execute(selectQuery2, (ICAO_CODE2,))
    result = cursor.fetchall()

    location_1_map =""
    location_2_map =""
    location_1_name=""
    location_2_name=""

    if result:
        first_row = result[0]
        latitude_deg=first_row[0]
        longitude_deg=first_row[1]
        location_1_map = first_row[2]

        location_2_map = (latitude_deg, longitude_deg)
    else:
        print(f"No data found for ICAO code {ICAO_CODE}")

    if result:
        first_row = result[0]
        latitude_deg=first_row[0]
        longitude_deg=first_row[1]
        location_1_map = first_row[2]
        location_2_map = (latitude_deg, longitude_deg)
    else:
        print(f"No data found for ICAO code {ICAO_CODE2}")

    if location_1_map != "" location_2_map !="":
        distance = geodesic(location_1_map, location_2_map).kilometers
        print(f"Distance between {location_1_name} and {location_2_name} is {distance:.2f}km.")
    else:
        print("One or both locations are empty,cannot calculate distance.")

        cursor.close()
        connection.close()

    main()













