#.reverse() : reverse a list in place
cities_1 = ["Dubai", "Mexico City", "São Paulo", "Hyderabad"]

print("regular", cities_1)
cities_1.reverse()
print("reversed", cities_1)
#Examples
# [ ] review and run example
cities_1 = ["Dubai", "Mexico City", "São Paulo", "Hyderabad"]

print("regular", cities_1)
cities_1.reverse()
print("reversed", cities_1)
# [ ] review and run example
all_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("regular list",all_num, "\n")
all_num.reverse()
print("reverse list",all_num, "\n")
num_len = len(all_num)

print("Three Multiple")
for num in all_num:
    if num/3 == int(num/3):
        print(num)
    else:
        pass
    
# [ ] review and run example
# create a list of  numbers by casting a range 
count_list = list(range(21))
print("before list", count_list)

# and reverse
count_list.reverse()
print("after list", count_list)