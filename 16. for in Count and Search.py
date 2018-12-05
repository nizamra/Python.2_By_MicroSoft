# iterates the "cities" list, count & sum letter "a" in each city name

cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
search_letter = "a"
total = 0

for city_name in cities:
    total += city_name.lower().count(search_letter)

print("The total # of \"" + search_letter + "\" found in the list is", total)



# city_search function has a default list of cities to search
def city_search(search_item, cities = ["New York", "Shanghai", "Munich", "Tokyo"] ):
    for city in cities:
        if city.lower() == search_item.lower():
            return True
        else:
            # go to the next item
            pass
    # no more items in list
    return False

# a list of cities
visited_cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]

search = input("enter a city visited: ")

# Search the default city list
print(search, "in default cities is", city_search(search))

# search the list visited_cities using 2nd argument
print(search, "in visited_cites list is", city_search(search,visited_cities))