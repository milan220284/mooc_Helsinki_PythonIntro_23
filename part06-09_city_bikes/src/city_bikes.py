# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    lines = []
    with open(filename) as new_file:
        for line in new_file:
            new_line = line.strip().split(';')
            lines.append(new_line)
    stations_dict = {}
    for line in lines[1:]:
        stations_dict[line[3]] = (float(line[0]), float(line[1]))
    return stations_dict


def distance(stations: dict, station1: str, station2: str):
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km


def greatest_distance(stations: dict):
    greatest = 0
    greatest_1 = None
    greatest_2 = None

    for station1 in stations:
        for station2 in stations:
            tmp = distance(stations, station1, station2)
            if tmp > greatest:
                greatest = tmp
                greatest_1 = station1
                greatest_2 = station2
    return (greatest_1, greatest_2, greatest)


