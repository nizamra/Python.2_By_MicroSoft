#.readline(): read files a line at a time
#use .readline() to read a line in a file as a string
#each .readline() moves to the next available line in the file

poem1 = open('poem1.txt', 'r')
poem_line1 = poem1.readline()
poem_line2 = poem1.readline()
poem_line3 = poem1.readline()
print(poem_line1 + poem_line2 + poem_line3)
print(poem1.readline())
poem1.close()

#Task 1
#use readline to get rainbow colors
#import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow as rainbow.txt
#open rainbow.txt as rainbow_file as read-only
#read the first 3 lines into variables: color1, color2, color3
#close rainbow_file
#print the first 3 colors
# [ ] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow as rainbow.txt
# [ ] open rainbow.txt as rainbow_text
# [ ] read the first 3 lines into variables: color1, color2, color3
# [ ] close rainbow.txt
# [ ] print the first 3 colors



















#.readline() in a while loop
#poem_line = poem1.readline()
#Examples
# [ ] review and run example
# open address to file
poem1 = open('poem1.txt', 'r')
# [ ] review and run example - use a while loop to read each line of a file 
#  remove last character ('\n') and print as upper case
poem_line = poem1.readline()
while poem_line:
    print(poem_line.capitalized())
    poem_line = poem1.readline()
while poem_line:
    print(poem_line[:-1].upper())
    poem_line = poem1.readline()
# [ ] review and run example
poem1.close()
#Task 2
#while .readline() rainbow colors
#assumes rainbow.txt has been imported in task 1
#open rainbow.txt as rainbow_file as read-only
#read a color from each line of rainbow_file in a while loop
#print each color capitalized
#close rainbow_file
# [ ] open rainbow.txt as rainbow_text as read-only
# [ ] read the color from lines of rainbow_text in a while loop
# [ ] print each color capitalized as the loop runs
# [ ] close rainbow_text 



















#.readline() with .strip()
#.strip() whitespace
poem1 = open('poem1.txt', 'r')
poem_line = poem1.readline().strip()
while poem_line:
    print(poem_line)
    poem_line = poem1.readline().strip()
poem1.close()
#Task 3
#.readline() with .strip() rainbow colors
#assumes rainbow.tx has been imported in task 1
#open rainbow.txt as rainbow_file as read-only
#read a color from each line of rainbow_file in a while loop
#use .strip to remove the whitespace
#print each color upper case
#close rainbow_file
# [ ] open rainbow.txt as rainbow_text as read-only  
# [ ] read a color from each line of rainbow_text in a while loop  
# use .strip to remove the whitespace '\n' character 
# print each color upper case 




















#.strip() arguments
#color = rainbow_messy.readline().strip('*\n*')
#.strip('*\n') removes leading and trailing * and \n
#Examples
# [ ] review and run example: import rainbow_messy.txt
#!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow_messy -o rainbow_messy.txt
# [ ] review and run example: open file read only
rainbow_messy = open('rainbow_messy.txt', 'r')
# [ ] review and run example: .readline() without .strip()
color = rainbow_messy.readline()
while color:
    print(color)
    color = rainbow_messy.readline()
# [ ] review and run example: strip "*" and newline ('\n')
rainbow_messy = open('rainbow_messy.txt', 'r')
color = rainbow_messy.readline().strip('*\n')
while color:
    print(color)
    color = rainbow_messy.readline().strip('*\n')
rainbow_messy.close()
#Task 4
#.strip() with arguments
#run import of cities_messy.txt below at least once this notebook session
#run open cities_messy.txt below before each test of the while loop cell
#edit while loop to strip the colon ':' , newline and spaces
#close cities_messy
# [ ] import the file
#!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities_messy -o cities_messy.txt
# [ ] run to read the file into memory
cities_messy = open('cities_messy.txt', 'r')
# [ ] edit the code to remove leading or trailing colon, newline and space characters
line = cities_messy.readline()
while line:
    print(line)
    line = cities_messy.readline()
#Task 5
#.strip() parentheses from poem2_messy
#import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2_messy as poem2_messy.txt
#open poem2_messy.txt as poem2_messy in read mode
#edit while loop to strip the leading and trailing parentheses & print the poem without blank lines
#close poem2_messy
# [ ] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2_messy as poem2_messy.txt
# [ ] open poem2_messy.txt as poem2_messy in read mode
# [ ] edit while loop to strip the leading and trailing parentheses, and newlines
# [ ] print the poem 
#line = poem2_messy.readline()
#while line:
#    print(line)
#    line = poem2_messy.readline()