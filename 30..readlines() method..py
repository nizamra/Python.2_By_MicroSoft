#.readlines()
#File read as a list with .readlines()
#converts the lines of a file into a list of strings
#!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt
poem1 = open('poem1.txt', 'r')
poem_lines = poem1.readlines()
poem_lines
for line in poem_lines:
    print(line)
#Task 1
#.readlines()
#open the cities file as a list
#Import a list of cities using curl
#git the list from https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities
#name the list cities.txt
#Open cities.txt in read mode using a variable: cities_file
#Read cities_file as a list variable: cities_lines using .readlines()
#Print each line of cities_lines by iterating the list
# [ ] import cities
# [ ] open cities.txt as cities_file and read the file as a list: cities_lines
# [ ] use list iteration to print each city in cities_lines list


















#working with lists from .readlines()
#remove newline characters from lists created using .readlines()
for line in poem_lines:
    poem_lines[count] = line[:-1]
    count += 1
#line[:-1] sets the end point at the last character of the string, the result is the '\n' (newline) character is omitted

poem1 = open('poem1.txt', 'r')
poem_lines = poem1.readlines()
print(poem_lines)
for line in poem_lines:
    print(line)

count = 0
for line in poem_lines:
    poem_lines[count] = line[:-1]
    count += 1
print(poem_lines)

for line in poem_lines:
    print(line)

#Task 2
#remove newline characters from cities lists created using .readlines()
#This task assumes that cites.txt has been imported in Task 1 above
#In task 1, the cities were printed with a blank line between each city - this task removes the blank lines
# [ ] re-open file and read file as a list of strings 
# [ ] open cities.txt as cities_file and read the file as a list: cities_lines
# [ ] remove the last character, "\n", of each cities_lines list item
# [ ] print each list item in cities_lines
#for line in cities_lines:
#    print(line)


















#.close()
#File .close() method frees resources
#file.close() method removes the reference created from file open() function
poem1.close()

poem1 = open('poem1.txt', 'r')
poem_lines = poem1.readlines()
print(poem_lines)
poem1.close()

#Task 3
#File .close()
#write each item in it's own cell
#open cities.txt as cities_file
#read the lines as cities_lines
#print the cities that start with the letter "D" or greater
#close cities_file
#test that file is closed
# [ ] open cities.txt as cities_file
# [ ] read the lines as cities_lines
# [ ] print the cities that start with the letter "D" or greater
# [ ] test that file is closed
# [ ] close cities_file


#Task 4
#readlines() poem2
#write each item in its own cell
#import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2.txt as poem2.txt
#open poem2.txt as poem2_file in read mode
#create a list of strings, called poem2_lines, from each line of poem2_text (use .readlines())
#remove the newline character for each list item in poem2_lines
#print the poem2 lines in reverse order
# [ ] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2.txt as poem2.txt
# [ ] open poem2.txt as poem2_text in read mode
# [ ] create a list of strings, called poem2_lines, from each line of poem2_text
# [ ] remove the newline character for each list item in poem2_lines
# [ ] print the poem2 lines in reverse order