#Combine Lists
#+ list addition
#.extend() list method
#combine lists with + and .extend()
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
wish_cities = ["Reykjavík", "Moscow", "Beijing", "Lamu"]
# combine in a new list
all_cities = visited_cities + wish_cities

# add a list to an existing list
visited_cities.extend(wish_cities)
#Examples
# [ ] review and run example
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
wish_cities = ["Reykjavík", "Moscow", "Beijing", "Lamu"]

# .extend() 
# extending visited_cities list (IN PLACE) by concatenating wish_cities
visited_cities.extend(wish_cities)
print("ALL CITIES",visited_cities)
# [ ] review and run example
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
wish_cities = ["Reykjavík", "Moscow", "Beijing", "Lamu"]

# (+) Addition operator for lists creates a (NEW) combined List
all_cities = visited_cities + wish_cities

print("ALL CITIES")
for city in all_cities:
    print(city)
# [ ] review and run example
team_a = [0,2,2,2,4,4,4,5,6,6,6]
team_b = [0,0,0,1,1,2,3,3,3,6,8]
print("Team A:", team_a, "\nTeam B:",team_b)

# (+) Addition operator 
team_totals = team_a + team_b
print("Team Totals", team_totals)
# [ ] review and run example after running cell above
# .extend() 
team_a.extend(team_b)
print("Team_a extended", team_a)