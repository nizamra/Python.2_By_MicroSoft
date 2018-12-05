#.remove(object) removes the 1st item that matches
#dog_types.remove("Pug")
#ValueError occurs if the object is not available to be removed
dog_types = ["Lab", "Pug", "Poodle"]
if "Pug" in dog_types:
    dog_types.remove("Pug")
else:
    print("no Pug found")
print(dog_types)



dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]
print(dogs)
while "Poodle" in dogs:
    dogs.remove("Poodle")
    print(dogs)