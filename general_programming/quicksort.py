city_list = []
cities = open("cities_out.txt", "r")

for city in cities:
    city = city.strip()
    split = city.split(",")
    city_list.append(split)

cities.close()


def partition(list, p, r, compare_func):
    pivot = list[r]
    i = p - 1
    j = p
    while j <= r:
        if compare_func(list[j], pivot):
            i = i + 1
            (list[i], list[j]) = (list[j], list[i])
        j = j + 1
    return i


def quick_sort(list, p, r, compare_func):
    if p < r:
        q = partition(list, p, r, compare_func)
        quick_sort(list, p, q-1, compare_func)
        quick_sort(list, q+1, r, compare_func)


def sort(list, compare_func):
    quick_sort(list, 0, len(city_list)-1,compare_func)
    return list[::-1]