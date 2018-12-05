#TASK 1
# [ ] print out the "physical states of matter" (matter_states) in 4 sentences using list iteration
# each sentence should be of the format: "Solid - is state of matter #1" 
matter_states = ['solid', 'liquid', 'gas', 'plasma']
x=1
for item in matter_states:
    print(item ," - is state of matter #",x)
    x+=1
# [ ] iterate the list (birds) to see any bird names start with "c" and remove that item from the list
# print the birds list before and after removals
birds = ["turkey", "hawk", "chicken", "dove", "crow"]
birds
for item in birds:
    if item.startswith("c"):
        birds.remove(item)
birds
# the team makes 1pt, 2pt or 3pt baskets
# [ ] print the occurrence of each type of basket(1pt, 2pt, 3pt) & total points using the list baskets
baskets = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]
total=0
for item in baskets:
    total += item
    total
print("ones",baskets.count(1))
print("twos",baskets.count(2))
print("threes",baskets.count(3))
sbaskets=sorted(baskets)



#TASK 2
#iteration with range(stop) & range(start,stop)
# [ ] using range() print "hello" 4 times
for x in range(4):
    print("Hello!")
# [ ] find spell_list length
# [ ] use range() to iterate each half of spell_list  
# [ ] label & print the first and second halves
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
half_1 = int(len(spell_list)/2)
for word in range(half_1):
    print(spell_list[word])
for word in range(half_1,len(spell_list)):
    print(spell_list[word])
# [ ] build a list of numbers from 20 to 29: twenties 
# append each number to twenties list using range(start,stop) iteration
# [ ] print twenties
twenties = []
for word in range(20,30):
    twenties.append(word)
twenties
# [ ] iterate through the numbers populated in the list twenties and add each number to a variable: total
# [ ] print total
total = 0
for ss in range(10):
    total+=twenties[ss]
    total
total
# check your answer above using range(start,stop)
# [ ] iterate each number from 20 to 29 using range()
# [ ] add each number to a variable (total) to calculate the sum
# should match earlier task 
total = 0
for sd in range(20,30):
    total+=sd
    total
total



#TASK 3
#iteration with range(start:stop:skip)
# [ ] create a list of odd numbers (odd_nums) from 1 to 25 using range(start,stop,skip)
# [ ] print odd_nums
# hint: odd numbers are 2 digits apart
for d in range(1,25,2):
    print(d,end=" ")
# [ ] create a Decending list of odd numbers (odd_nums) from 25 to 1 using range(start,stop,skip)
# [ ] print odd_nums,  output should resemble [25, 23, ...]
for d in range(25,-10,-2):
    print(d,end=" ")
# the list, elements, contains the names of the first 20 elements in atomic number order
# [ ] print the even number elements "2 - Helium, 4 - Beryllium,.." in the list with the atomic number
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
 'Potassium', 'Calcium']
x=0
for ie in range(1,len(elements),2):
    x+=2
    print(x,"- ",elements[ie]," , ",end="")
# [ ] the list, elements_40, contains the names of the first 40 elements in atomic number order
# [ ] print the odd number elements "1 - Hydrogen, 3 - Lithium,.." in the list with the atomic number elements_40
elements_40 = ['Hydrogen', \
 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', \
 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', \
 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', \
 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium']
x=1
for ief in range(0,len(elements_40),2):
    print(x,"- ",elements_40[ief]," , ",end="")
    x+=2



#TASK 4
#combine lists with + and .extend()
# [ ] print the combined lists (numbers_1 & numbers_2) using "+" operator
numbers_1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# pythonic casting of a range into a list
numbers_2 = list(range(30,50,2))
print("numbers_1:",numbers_1)
print("numbers_2",numbers_2)
numbers_12=numbers_1+numbers_2
print("combined lists",numbers_12)
# [ ] print the combined element lists (first_row & second_row) using ".extend()" method
first_row = ['Hydrogen', 'Helium']
second_row = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
Rows=[]
Rows.extend(first_row)
Rows.extend(second_row)
print("1st Row:", first_row)
print("2nd Row:", second_row)
print("both Rows:", Rows)
########Project: Combine 3 element rows
#Choose to use "+" or ".extend()" to build output similar to

#The 1st three rows of the Period Table of Elements contain:
['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']

#The row breakdown is
#Row 1: Hydrogen, Helium
#Row 2: Lithium, Beryllium, Boron, Carbon, Nitrogen, Oxygen, Fluorine, Neon
#Row 3: Sodium, Magnesium, Aluminum, Silicon, Phosphorus, Sulfur, Chlorine, Argon
# [ ] create the program: combined 3 element rows 

elem_1 = ['Hydrogen', 'Helium'] 
elem_2 = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
elem_3 = ['Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']
elem_3_Rows=elem_1+elem_2+elem_3
elem_3_Rows
# [ ] .extend() jack_jill with "next_line" string - print the result
jack_jill = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill']
next_line = ['To', 'fetch', 'a', 'pail', 'of', 'water']
jack_jill_2=[]
jack_jill_2.extend(jack_jill)
jack_jill_2.extend(next_line)
jack_jill_2



#TASK 5
#.reverse() : reverse a list in place
# [ ] use .reverse() to print elements starting with "Calcium", "Chlorine",... in reverse order
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
 'Potassium', 'Calcium']
elements.reverse()
elements.sort()
# [ ] reverse order of the list... Then print only words that are 8 characters or longer from the now reversed order
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
spell_list.reverse()
spell_list
for af in spell_list:
    if len(af)>=8:
        print(af, end=" ")



#TASK 6
#.sort() and sorted()
# [ ] sort the list element, so names are in alphabetical order and print elements
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
 'Potassium', 'Calcium']
elements.sort()
elements
# [ ] print the list, numbers, sorted and then below print the original numbers list 
numbers = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]
numbers_sort=sorted(numbers)
numbers_sort
numbers



#TASK 7
#Converting a string to a list with .split()
# [ ] split the string, daily_fact, into a list of word strings: fact_words
# [ ] print each string in fact_words in upper case on it's own line
daily_fact = "Did you know that there are 1.4 billion students in the world?"
fact_words=daily_fact.split()
fact_words
for up in fact_words:
    print(up.upper())
# [ ] convert the string, code_tip, into a list made from splitting on the letter "o"
# [ ] split poem on "b" to create a list: poem_words
# [ ] print poem_words by iterating the list
poem = "The bright brain, has bran!"
poem_list=poem.split("o")
poem_list
poem_words=poem.split("b")
poem_words
for kms in poem_words:
    print (kms,end="*_-")



#TASK 8
#.join()
#build a string from a list
# [ ] print a comma separated string output from the list of Halogen elements using ".join()"
halogens = ['Chlorine', 'Florine', 'Bromine', 'Iodine']
print(",".join(halogens))
# [ ] split the sentence, code_tip, into a words list
# [ ] print the joined words in the list with no spaces in-between
# [ ] Bonus: capitalize each word in the list before .join()
code_tip ="Read code aloud or explain the code step by step to a peer"
code_tip_words=code_tip.split()
code_tip_words
code_tip_words_capitalize=[word.capitalize() for word in code_tip_words]
print("".join(code_tip_words_capitalize))



#TASK 8
#list(string) & print("hello",end=' ')
# [ ] cast the long_word into individual letters list 
# [ ] print each letter on a line
long_word = 'decelerating'
for tt in list(long_word):
    print(tt)
# [ ] use use end= in print to output each string in questions with a "?" and on new lines
questions = ["What's the closest planet to the Sun", "How deep do Dolphins swim", "What time is it"]
for tnt in list(questions):
    print(tnt,end="?\n")
# [ ] print each item in foot bones 
#    - capitalized, both words if two word name
#    - separated by a comma and space
#    - and keeping on a single print line
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]
for tnt in foot_bones:
    tnt.capitalize()
    print(tnt,end=", ")
jand=" ".join(foot_bones)
xxx=[x.capitalize() for x in jand]
# this is not working