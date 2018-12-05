#Opening a Local File in read mode
#poem_file = open('poem1.txt', 'r') 
#MODE                	Description
#'r'	                read only mode
#'w'                 	write - overwrites file with same name
#'r+'                	read and write mode
#'a'                 	opens for appending to end of file

nizam_file = open('nizampython.txt', 'r')
nizam_contents = nizam_file.read().title()
print(nizam_contents)

poem_file = open('pamelafiles.txt', 'r')
poem_file
#Read a file using .read()
#poem_contents = poem_file.read()
#.read() loads the content of the file into memory as a string, including formatting such as new line (\n)
poem_contents = poem_file.read()
poem_contents
print(poem_contents)
#reading a file with .read(n) where n = number of characters to read
#each time poem_file.read(10) runs, the next 10 characters are read.
#Note: if .read(10) result is = '' (or empty string with no characters),
#it is likely that the end of the file has been reached. Perform a fresh
#.open() to reset read() to the beginning of the file.
poem_file = open('poem1.txt', 'r')
poem_10char = poem_file.read(10)
print(poem_10char)
poem_10char
# reads and displays without storing in a variable
poem_file.read(10)
# reads and stores in variable poem_parts
poem_parts = poem_file.read(10)
print(poem_parts)
poem_parts += poem_file.read(5)
print(poem_parts)
#.read() returns a string
#These strings can be manipulated just like any other string
#Boolean tests such as:
#.upper() .title()
#string slices, e.g.- cities[3:9]
#and string methods can be performed such as:
#.isdigit() .isalpha()
poem_file = open('poem1.txt', 'r')
poem_part = poem_file.read(15).upper()
print(poem_part)
poem_part = poem_file.read(6).title()
print(poem_part)
poem_part = poem_file.read(6)
print(poem_part)
print(poem_part.isalpha(), "isalpha() because of `\\n`")
poem_part
poem_file = open('poem1.txt', 'r')
poem_text = poem_file.read()
print(poem_text[8:26])

#Task 1
#import and open a local file in read mode
#Import a list of cities using curl
#git the list from https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities
#name the list cities.txt
#open cities.txt in read mode using a variable = cities_file
#test that cities_file opened cities.txt with a print statement
#Task 2
#read a file
#Read the file cities.text that was imported in task 1
#import cities.txt and open
#ensure the code was created and run in task 1 to import cities.txt
#create and run code to re-open cities.txt as cities_file
#read() cities_file into a variable called cities
#Test the read() by displaying the string contained in cities
#Test the read() by printing the cities string
#Task 3
#digits of pi
#read a set number of digits with .read(n)
#import, open, read, print
#import digits_of_pi.txt located at https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi
#open as digits_of_pi_text
#read()the first 4 characters of digits_of_pi_text into a variable called pi_digits
#print pi_digits
#add to pi_digits string with string addition
#add next 4 characters from digits_of_pi obtained from read()
#run the cell multiple times to get more digits of pi
# [ ] digits of pi
# 1. import digits_of_pi.txt
# [ ] digits of pi
# 2. open as digits_of_pi_text 
# 3. read() 4 char of digits_of_pi_text to pi_digits variable 
# 4. print pi_digits 
# [ ] digits of pi
# 5. add to pi_digits string with string addition  
#   a. add next 4 characters from digits_of_pi obtained from read()  
#   b. run the cell multiple times to get more digits of *pi*
#Task 4
#City Initials
#Read the file cities.text that was imported in task 1
#ensure the code was created and run in task 1 to import cities.txt
#create and run code to re-open cities.txt as cities_file
#read() cities_file into a variable called cities
#iterate through the characters in cities
#test if .isupper(), if True append the character to a string variable: initials
#else if (elif) character is "\n", if True append the "\n" to initials
#print initials