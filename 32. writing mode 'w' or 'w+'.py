#writing to a file opened in write mode 'w' or 'w+'
poem_file = open('panda.txt', 'w')
for x in range(11000):
    poem_file.write("Hello World!\n")  
poem_file.close()
#write mode: 'w'
#write mode plus read: 'w+'
#'w' and 'w+' modes will create a new file or overwrite existing files
#All previous data will be lost
#Examples
# [ ] review and run example
# - creates a new local file or overwrites the local file (makes it blank)
new_file = open('new_file.txt', 'w')
# [ ] review and run example to write some text to the file
new_file.write("This is line #1 with 'w'\nThis is line #2 with 'w'\nThis is line #3 withn 'w'!\n")
# [ ] review and run example
# - close file and re-open in read mode 
# - head pointer is at start of file
new_file.close()
new_file = open('new_file.txt', 'r')
# [ ] review and run example to see what was written to the file
new_text = new_file.read()
print(new_text)

new_file.close()
#'w+' means the file is in write plus read mode
#after any write, the pointer is at the end of text that has been written
#to read the entire file, the pointer needs to be at the beginning of the file - see .seek() below to set the file pointer
#Task 1
#create a local file
#open in 'w' mode
#open inner_planets.txt in write mode 'w' to create a local file
#write the first four planets from the sun in earth's solar system (Mercury, Venus, Earth, Mars) on separate lines
#close the file and re-open in read mode 'r'
#use .read() to read the entire file contents
#print the entire file contents
# [ ] open planets.txt in write mode
# [ ] write Mercury, Venus, Earth, Mars on separate lines
# [ ] close the file and re-open in read mode
# [ ] use .read() to read the entire file contents
# [ ] print the entire file contents and close the file