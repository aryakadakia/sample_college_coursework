from quicksort import *


def compare_string(city_1, city_2):
    return str.lower(city_1[0]) <= str.lower(city_2[0])


def compare_population(city_1, city_2):
    return float(city_2[1]) <= float(city_1[1])


def compare_latitudes(city_1,city_2):
    return float(city_2[2]) >= float(city_1[2])


sort(city_list, compare_population)
out_file = open("cities_population.txt", "w")
for i in range(len(city_list)):
    out_file.write(str(city_list[i][0]) + "," + str(city_list[i][1]) + "," + str(city_list[i][2]) + "," + str(city_list[i][3]) + "\n")
out_file.close()

sort(city_list, compare_latitudes)
out_file = open("cities_latitude.txt", "w")
for i in range(len(city_list)):
    out_file.write(str(city_list[i][0]) + "," + str(city_list[i][1]) + "," + str(city_list[i][2]) + "," + str(city_list[i][3]) + "\n")
out_file.close()

sort(city_list, compare_string)
out_file = open("cities_alpha.txt", "w")
for i in range(len(city_list)):
    out_file.write(str(city_list[i][0]) + "," + str(city_list[i][1]) + "," + str(city_list[i][2]) + "," + str(city_list[i][3]) + "\n")
out_file.close()