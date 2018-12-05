days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday"
, "Thursday", "Friday", "Saturday"]
#print the days in the list at odd indexes 1,3,5
print (days_of_week[1],days_of_week[3],days_of_week[5])
day = days_of_week[5]
#Make up  new day - insert a new day into the middle of days_of_week between Wed - Thurs
days_of_week.insert(4,"newday")
#modified week is too long - pop() the last index of days_of_week & print .pop() value
days_of_week
for x in range(3):
    print(days_of_week.pop())
    print("days_of_week after poping", days_of_week)
#delete (del) the new day added to the middle of the week 
del days_of_week[4]



phone_letters = [" "," ","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
def let_to_num():
    letter=input ("a single letter, space or empty string of your choice: ")
    key=0
    while key < 10:
        if letter in phone_letters[key]:
            return key
        else:
            key = key + 1
    return "Not Found"

#Bonus: create a special case to check if empty string ("") was submitted
#the problem is that an empty string will be found in all strings as
#if "" in "ABC": 
#is True, and is true for any phone_letters, but should return 1



#Challenge: reverse a string
#using
#while
#.pop()
#insert()
#pop() the first item in the list and add to the beginning of a new string that will be reversed
# [ ] Challenge: write the code for "reverse a string" reversing some_numbers   
#some_numbers =[1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77]
some_numbers =[1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77]
reversed=[]
while some_numbers:
    reversed.insert(42,some_numbers.pop())
reversed



all_animals=["cat","goat","cat"]
def program_flow():
    print("look at all the animals ", all_animals)
    userinput=input("enter the name of an animal: ")
    if all_animals=='':
        print("goodbey!")
    elif userinput.lower()=="quit":
        print("goodbey!")
    else:
        result=material(userinput)
    print(result  ,"\n look at all the animals ", all_animals)

def material(userinput):
    if userinput in all_animals:
        all_animals.remove(userinput)
        return "1 instance of",userinput,"removed from list"
    elif userinput=="":
        return all_animals.pop(),"popped from list"
    else:
        all_animals.insert(712,userinput)
        return "1 instance of",userinput,"appended to list"
 


animal_list = ["cat", "goat", "cat"] 
animal_pop = "" 
def list_o_matic(): 
    while animal_list: 
        print("look at all the animals", animal_list)
        animal_entry = input("enter the name of an animal: ") 
        if animal_entry == "": 
            animal_pop = animal_list.pop() 
            print(animal_pop, "popped from list") 
        elif animal_entry in animal_list: 
            animal_list.remove(animal_entry) 
            print("1 instance of", animal_entry, "removed from list") 
        else: 
            if animal_entry.lower() == "quit": 
                break 
            else: 
                animal_list.append(animal_entry) 
                print("1 instance of", animal_entry, "appended to list") 
    print("Goodbye!") 
    return 
list_o_matic()