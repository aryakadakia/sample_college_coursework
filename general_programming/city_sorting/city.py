

# City class and methods (Checkpoint 1)
class City:
    def __init__(self, code, name, region, population, latitude, longitude):
        self.code = str(code)
        self.name = str(name)
        self.region = str(region)
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return str(self.name) + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)


# Reading and parsing files (Checkpoint 2)

in_file = open("world_cities.txt", "r")

city_list = []

for city in in_file:
    city = city.strip()   # strip new line
    city = city.split(",")  # split items
    city = City(str(city[0]), str(city[1]), str(city[2]), int(city[3]), float(city[4]), float(city[5]))
    city_list.append(city)

in_file.close()

# Writing output file (Checkpoint 3)

out_file = open("cities_out.txt", "w")
for i in range(len(city_list)):
    out_file.write("%s\n" % city_list[i])

out_file.close()
