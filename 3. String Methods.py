work_tip = "save your code"

# number of characters
len(work_tip)

# letter "e" occurrences
work_tip.count("e")

# find the index of the first space . returns -1 if no match found
work_tip.find(" ")

# find the index of "u" searching a slice work_tip[3:6]
work_tip.find("u",3,6)



work_tip = "good code is commented code"
mid_pt = int(len(work_tip)/2)
# print 1st half of sentence
print(work_tip[:mid_pt])
# print the 2nd half of sentence
print(work_tip[mid_pt:])



quote = "they stumble who run fast"
start = 0
space_index = quote.find(" ")
while space_index != -1:
    print(quote[start:space_index])
    start=0+space_index
    space_index=quote.find(" ",space_index+1)
print(quote[start:])
start
space_index




work_tip = "save your code"
print("number of characters in string")
print(len(work_tip),"\n")
print('letter "e" occurrences')
print(work_tip.count("e"),"\n")
print("find the index of the first space")
print(work_tip.find(" "),"\n")
print('find the index of "u" searching a slice work_tip[3:9] -', work_tip[3:9])
print(work_tip.find("u",3,9),"\n")
print('find the index of "e" searching a slice work_tip[4:] -', work_tip[4:])
print(work_tip.find("e",4))
work_tip = "good code has meaningful variable names"
print(work_tip)
# index where first instance of "code" starts
code_here = work_tip.find("code")
print(code_here, '= starting index for "code"')



# if .find("o") has No Match, -1 is returned
print ("work_tip:" , work_tip)
location = work_tip.find("o")

# keeps looping until location = -1 (no "o" found)
while location >= 0:
    print("'o' at index =", location)
    # find("o", location + 1) looks for a "o" after index the first "o" was found
    location = work_tip.find("o", location + 1)
print("no more o's")


planet_name = "Jupiter"
print(planet_name[-7])
print(planet_name[::-1])

wise_words = 'Play it who opens'
print(wise_words[1::3])

def foods():
    food=input("inter your food: ")
    for x in food:
        print(x)



#get user input for first_name
#create an empty string variable: new_name
#iterate through letters in first_name Backwards
#add each letter to new_name as you iterate
#Replace the letter if "e", "t" or "a" with "?" (hint: if, elif, elif, else)
#print new_name
#example: "Alton" = "no?l?"
def names():
    first_name=input("inter your first name please: ")
    new_name=first_name[::-1]
    for x in range(len(new_name)):
        if new_name[x].lower() == "n":
            new_name[x]=x
        elif new_name[x].lower()=="e":
            new_name[x]="x"
        elif new_name[x].lower()=="t":
            new_name[x]="x"
    print(new_name)



# [ ] find and report (print) number of w's, o's + use of word "code"
work_tip = "Good code is commented code"
print("number of w's -", work_tip.count("w"))
print("number of o's -", work_tip.count("o"))
print("the value of 'code's index -", work_tip.find("code"))
# print code_tip
code_tip = "code a conditional decision like you would say it"
print ("code_tip:" , code_tip)
# [ ]  count times letter "i" appears in code_tip string
print("number of i's -", code_tip.count("i"))
# [ ] find and display the index of all the letter i's in code_tip
for x in range(0,len(code_tip)):
    if code_tip[x]=="i":
        print(x)



#Create a program inputs a phrase and prints all of the words that start with h-z
#Sample input:
#enter a 1 sentence quote, non-alpha separate words: Wheresoever you go, go with all your heart
#Sample output:
#WHERESOEVER
#YOU
#WITH
#YOUR
#HEART
#split the words by building a placeholder variable: word
def printice():
    quote=input("enter a quote here: ")
    word=""
    for x in quote:
        if x.isalpha():
            word+=x
        elif word.lower() > "h":
            print(word)
            word=""

#loop each character in the input string
#check if character is a letter
#add a letter to word each loop until a non-alpha char is encountered
#if character is alpha
#add character to word
#non-alpha detected (space, punctuation, digit,...) defines the end of a word and goes to else
#else
#check if word is greater than "g" alphabetically
#print word
#set word = empty string
#or else
#set word = empty string and build the next word
#Hint: use .lower()
# [] create words after "G"



work_tip = "Good code is commented code"
new_string = ""
for y in work_tip:
    if y == " ":
        y = "-"
        new_string = new_string + y
    else:
        new_string = new_string + y
print(new_string)