#using .seek(0)
#setting the pointer to beginning of file
new_file = open('new_file.txt', 'w+')
new_file.seek(0)
new_contents = new_file.read()
print(new_contents)
#using .seek() to set the read/write pointer to beginning of file
#new_file.seek(0) moves the file read\write pointer to the start of the file
new_file = open('new_file.txt', 'w+')
new_text = new_file.read()
print(new_text)
# [ ] review and run - write to the blank file
new_file.write("This is line #1 with 'w+'\nThis is line #2 with 'w+'\n")
# [ ] review and run example - read and print (Note: the pointer is at the end of the file - result = empty string)  
new_text = new_file.read()
print(new_text)
#Expected: prints empty string above
#pointer was at end of file where there is nothing to read
#seek(0)
#sets the pointer to the beginning of the file, enabling read() to input the entire file contents
# [ ] review and run example - sets pointer to beginning of file
new_file.seek(0)
# [ ] review and run example - now read starts from beginning of file
new_text = new_file.read()
print(new_text)
# # [ ] review and run example - clean up and close file
new_file.close()
#Task 2
#using .seek(0) on a local file in write plus read mode 'w+'
#open outer_planets.txt in 'w+' mode (write plus read)
#open outer_planets.txt in write plus read mode 'w+'
#write four outer planets in earth's solar system (Jupiter, Saturn, Uranus, Neptune) on separate lines
#use .seek() to move the pointer to the start of the file
#use .read() to read the entire file contents
#print the entire file contents and close the file
# [ ] open outer_planets.txt in write mode 'w+' 
# [ ] write four outer planets in earth's solar system (Jupiter, Saturn, Uranus, Neptune) on separate lines
# [ ] use .seek() to move the pointer to the start of the file
# [ ] use .read() to read the entire file contents
# [ ] print the entire file contents and close the file



















#using .seek() offset and whence
#setting the pointer in a file with positive offset values and whence location
new_file.seek(13)
new_contents = new_file.read()
print(new_contents)
new_file.seek(0,2)
#using .seek() to set the read/write pointer in a file
#offset values and whence arguments
#.seek() can set the pointer to a desired index from the beginning of the file
#the example below moves to the character to offset 10 (the 11th character)

new_file.seek(10)
#which is also written with an optional second argument, know as whence ("from where")

new_file.seek(10,0)
#using 0 for whence starts the offset from the beginning of the file

#Note: the offset must be a positive integer in Python 3, so we cannot offset backwards from the end of the file

#file.seek(offset, whence)
#    whence mode	                description
#          0                     points to the beginning of the file
#          1	                    points to the current location
#          2	                    points to the end of the file & offset is always 0
#using whencethe index can be offset from either the beginning, current location or to the end of the file (where there is no offset applied)

#Examples
#seek to a specific location
# [ ] review and run - create, write, read and print a file
tips_file = open('code_tips.txt', 'w+')
tips_file.write('-use simple function and variable names\n-comment code\n-organize code into functions\n')
tips_file.seek(0)
tips_text = tips_file.read()
print(tips_text)
# [ ] review and run example - setting a specific seek() index 
tips_file.seek(13)
# now read starts from 14th character of file
tips_text = tips_file.read()
print(tips_text)
# [ ] review and run example - string slicing on a read of an entire file
# read from the start
tips_file.seek(0)
tips_text = tips_file.read()

# slice from the 14th character to end
print(tips_text[13:])
#Examples
#seek() with optional whence argument
# [ ] review and run example - setting pointer to end of file with whence value = 2
tips_file.seek(0,2)
tips_file.write("-use seek(0,2) to set read/write at end of file\n")

# read from beginning of file - .seek(0,0) is same as .seek(0)
tips_file.seek(0,0)
tips_text = tips_file.read()
print(tips_text)
# [ ] review and run example - point to file beginning and overwrite 1st line
tips_file.seek(0)
tips_file.write('-use simple function and variable names\n'.upper())

# [ ] review and run example - show new file contents
tips_file.seek(0,0)
tips_text = tips_file.read()
print(tips_text)
#Task 3
#seek() with optional whence argument
#open a new file days.txt in write plus read mode 'w+'
#write week days (Monday - Friday) on separate lines
#use .seek() to move the pointer to the start of the file
#use .read() to read the entire file contents
#print the entire file contents and close the file
#use .seek() to move the pointer to the end of the file and write the weekend days (Saturday & Sunday)
#use .seek() to move the pointer to the start of the file
#use .read() to read the entire file contents
#print the entire file contents and close the file
# [ ] open a new file days.txt in write plus read mode 'w+' 
# [ ] write week days (Monday - Friday) on separate lines to the file
# [ ] use .seek() to move the pointer to the start of the file
# [ ] use .read() to read the entire file contents
# [ ] print the entire file contents and close the file
# [ ] use .seek() to move the pointer to the end of the file
# [ ] write the weekend days (Saturday & Sunday)
# [ ] use .seek() to move the pointer to the start of the file
# [ ] use .read() to read the entire file contents
# [ ] print the entire file contents and close the file



















#open a file in a writable mode
#open a file in a writing mode, with: 'w', 'w+', 'r+', 'a', 'a+'
#        MODE	            Description
#        'r'	                read only mode
#        'w'	                write - overwrites file with same name
#        'w+'               	write and read mode - overwrites file with same name
#        'r+'            	read and write mode (no overwrite)
#        'a'	                opens for appending to end of file (no overwrite)
#        'a+'	            opens for appending to end of file (no overwrite) plus read
#warning: 'w' and 'w+' modes will create a new file or overwrite existing files (deleting all file contents)


















#writing to a file opened in additional write modes: 'r+', 'a', 'a+'
#Writing is the same - pointers are different
poem_file = open('poem.txt', 'r+') 
poem_file.write("Hello World!\n")
poem_file = open('poem.txt', 'a+') 
poem_file.write("Goodbye, this is the end of the file\n")


#read mode plus write 'r+' and append modes 'a', 'a+'
#read plus mode 'r+' differs from write modes 'w', 'w+'
#read plus doesn't blank out the file contents with an overwrite
#append modes 'a', 'a+' differ from write modes 'w', 'w+'
#append doesn't blank out the file contents with an overwrite
#append pointer is set to the end of the file for every write
#append plus (a+) is append mode, plus read mode
#                                             'r+', 'a', 'a+'
#                        will not overwrite existing file content creating a blank file
#Examples
#append plus mode a+
# [ ] review and run example - function writes to the open log argument
# loads function into memory but the function is not called
def logger(log):
    log_entry = input("enter log item (enter to quit): ")
    count = 0

    while log_entry:
        count += 1
        log.write(str(count) + ": " + log_entry + "\n")
        log_entry = input("enter log item (enter to quit): ")
        
    return count
    
# [ ] review and run example: makes a blank file  (initialize/reset)

log_file = open('log_file.txt', 'w+')
log_file.close()
# [ ] review and run example - opens the log_file before passing to logger() function call, below
# allows for calls below to run several times appending to the end of log_file

log_file = open('log_file.txt', 'a+')
# [ ] review and run example - calls the above logger() function
# what happens running the cell above (a+) again before running this cell again? 
# what happens if log_file.seek(0) is run before an append?

logger(log_file)    

log_file.seek(0)
log_text = log_file.read()

print()
print(log_text)
log_file.close()







#read plus mode r+
#create a file that has one line: "Count is: x"
#overwrite with new count at the x location (x is an integer)

# [ ] review and run example - create a file with initial count of 0
count_file = open("count_file.txt", "w+")

count_file.write("Count is: 0")
count_file.seek(0)
print(count_file.readline().strip())

count_file.close()
# [ ] review and run example - can rerun this cell
count_file = open("count_file.txt", "r+")

count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

# get the int character(s) after the colon and space, cast and increment
count = int(count_line[10:])+1

# write the incremented value to the file - overwrite before value
count_file.seek(10)
count_file.write(str(count))

count_file.seek(0)
print("\nAFTER\n" + count_file.readline().strip())

count_file.close()
# [ ]  review funtion code for inc_count() funtion that reads file and updates the count
# the file always has 1 line that is The count is: N, where N is an integer
def inc_count(cnt_file):
    cnt_file.seek(0,0)
    cnt_line = cnt_file.readline().strip()
    cnt = int(cnt_line[10:])+1
    cnt_file.seek(10,0)
    cnt_file.write(str(cnt))
    return cnt
# [ ] review and run example with call to function: inc_count() - **Run cell multiple times**
# opens file/prints initial value
count_file = open("count_file.txt", "r+")

count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

# call inc_count() to increase the count 5 times
for i in range(5):
    count = inc_count(count_file)
    count_file.seek(0)
    print("\nAFTER inc_count() call", i+1, "\n" + count_file.readline().strip())

count_file.close()
#Task 4
#append
#Open task4_file.txt in append plus mode ("a+")
#create a for item in range(5): loop, for each loop:
#write to the file: "append #"+ str(item)+"\n"
#use seek() to set the pointer to the beginning of the file
#print the file contents using file .read() method after exiting the loop
#in append mode the file should only write to the end of the file regardless of setting seek() location

# [ ] complete the task  
# Provided Code creates and populates task4_file.txt  
task4_file = open('task4_file.txt', 'w+')
task4_file.write("Line1\nLine2\nLine3\n")
task4_file.close()
# [ ] code here

#Task 5
#read plus (r+) mode
#read the provided code and complete the code as follows:
#Run the provided code below to create/open, print and close task5_file.txt
#Open task5_file.txt in append plus mode ("r+")
#create a   for item in range(1,5): loop, then, during each loop:
#write to the file: "append#" + str(item)+ "\n"
#use .seek(item*18) to set the pointer to 18x's the loop count
#Note: starting the first loop, item is 1 if using range(1,5), seek will be set to 18, 36, 54, 72
#print the file contents using file .read() method after exiting the loop
#"r+" mode will write wherever the pointer is set - such as after a read or from using .seek()
# [ ] complete the task
# Provided Code creates and populates task5_file.txt
task5_file = open('task5_file.txt', 'w+')
task5_file.write("Line---1\nLine---2\nLine---3\nLine---4\nLine---5\nLine---6\nLine---7\nLine---8\nLine---9\nLine--10\n")
task5_file.seek(0)
print("Before:\n"+ task5_file.read()+"\n")
task5_file.close()
# [ ] code here