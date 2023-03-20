import csv
import os.path
import sys
import random
import geopy.distance as geo
from Models.Place import Place
from Models.PlaceDistance import PlaceDistance

places = []

# Entry point of this application
def main():
    argv = sys.argv[1:]
    if len(argv) == 0:
        print('No parameter found. System will parse the places.csv from fixed location.')
        import_places_csv_file('places.csv')
        calculate_great_circle_distance()
    else:
        try:
            argument = int(argv[0])
            print('Parameter found: ' + argv[0] + '')
            import_places_csv_file('places.csv')
            find_random_places_calculate_distance(argument)
        except ValueError:
         print('Invalid parameter. Please make sure you have type valid integer parameter.')

# Import csv file in application from a defined path.
def import_places_csv_file(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            print('-' * 77)
            print("Places list from file: " + filepath)
            print('-' * 77)
            csvreader = csv.reader(file)
            next(csvreader)
            places.clear()
            for row in csvreader:
                place = Place(row[0], float(row[1]), float(row[2]))
                places.append(place)
                print("{: <25} {: >25} {: >25}".format(*[place.name, place.latitude, place.longitude]))
    else:
        print('File path is wrong or file does not exist.')

# Calculate great circle distance between two places imported the places from csv
def calculate_great_circle_distance():
    if len(places) == 0:
        return
    placedistances = []
    for fromplace in places:
        for toplace in places:
            if not check_existing_distance(placedistances, fromplace, toplace):
                distance = round(geo.great_circle((fromplace.latitude, fromplace.longitude),
                                                  (toplace.latitude, toplace.longitude)).kilometers, 1)
                placedistance = PlaceDistance(fromplace, toplace, distance)
                placedistances.append(placedistance)

    print('-' * 77)
    print('Great Circle Distance')
    print('-' * 77)
    placedistances.sort(key=lambda s: s.distance)
    for placedistance in placedistances:
        row = [placedistance.fromplace.name, placedistance.toplace.name, str(placedistance.distance) + ' km']
        print("{: <25} {: <25} {: >25}".format(*row))

    print('-' * 77)
    closestpair = placedistances[0]
    avgdistance = round(geo.distance((closestpair.fromplace.latitude, closestpair.fromplace.longitude),
                                     (closestpair.toplace.latitude, closestpair.toplace.longitude)).kilometers, 1)
    print("Average distance: " + str(
        avgdistance) + ' km.  ' + "Closest pair: " + closestpair.fromplace.name + ' - ' + closestpair.toplace.name + '   ' + str(
        closestpair.distance) + ' km.')
    print('-' * 77)

# Check if distance is already calculated between two places.
def check_existing_distance(placedistances, fromplace, toplace):
    if len(places)==1:
        return False
    if fromplace is toplace:
        return True
    for placedistance in placedistances:
        if (fromplace.name == placedistance.fromplace.name or fromplace.name == placedistance.toplace.name) \
                and (toplace.name == placedistance.fromplace.name or toplace.name == placedistance.toplace.name):
            return True

    return False


# Find random places within places imported from csv by passing n integer arguments.
# Calculate great circle distance between two places from random places
def find_random_places_calculate_distance(argument):
    count=len(places)
    if argument > count:
        print("Invalid parameter. Random input should be exceed more than " + str(count))
        return

    randomplaces = []
    for i in range(argument):
        rand=random.randint(i, argument)
        randomplaces.append(places[rand])

    print('-' * 77)
    print("Randomly selected places")
    print('-' * 77)
    places.clear()
    for place in randomplaces:
      places.append(place)
      print("{: <25} {: >25} {: >25}".format(*[place.name, place.latitude, place.longitude]))

    calculate_great_circle_distance()
