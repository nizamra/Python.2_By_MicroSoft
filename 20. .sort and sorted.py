#.sort() and sorted()
#.sort() in place
#.sort() - orders a list in place

quiz_scores = [20, 19, 20, 15, 20, 20, 20, 18, 18, 18, 19]
quiz_scores.sort()
#sorted() copy
#sorted() - creates an ordered list copy

game_points = [3, 14, 0, 8, 21, 1, 3, 8]
sorted_points = sorted(game_points)
#Examples
#.sort() and sorted()
# [ ] review and run example
quiz_scores = [20, 19, 20, 15, 20, 20, 20, 18, 18, 18, 19]

# use .sort()
quiz_scores.sort()

print("quiz_scores:", quiz_scores)
# [ ] review and run example
game_points = [3, 14, 0, 8, 21, 1, 3, 8]

# use sorted()
sorted_points = sorted(game_points)

print("game_points:", game_points)
print("sorted_points:", sorted_points)
# [ ] review and run example
cities_1 = ["Dubai", "Mexico City", "São Paulo", "Hyderabad"]

print("Unsorted", cities_1)
cities_1.sort()
print("Sorted", cities_1)