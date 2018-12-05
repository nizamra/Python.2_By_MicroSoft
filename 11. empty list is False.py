#in a conditional an empty list will evaluate False
#This allows creating a while loop that runs until a list is empty

while dog_types: 
#Example
dog_types = ["Lab", "Pug", "Poodle"]

while dog_types: 
    print(dog_types.pop())