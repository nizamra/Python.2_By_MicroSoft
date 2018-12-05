#Task 1
#Order the Rainbow
#Open the rainbow file then put in a list and print in alphabetical order
#Download and open the file.
#Download list of rainbow colors, as rainbow.txt, using curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow
#Open rainbow.txt in read mode using a variable: rainbow_file
#Read rainbow_file as a list variable: rainbow_colors using .readlines()
#Sort the rainbow_lines list alphabetically.
#Print each line of rainbow_lines by iterating the sorted list.
#Close rainbow_file.

#!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow -o rainbow.txt
rainbow_file= open('rainbow.txt','r')
rainbow_colors=rainbow_file.readlines()
rainbow_colors.sort()
for i in rainbow_colors:
    print(i)
rainbow_file.close()

#Task 2
#The Weather
#Create a program that reads from a file to display city name and average temperature in Celsius.
#use !curl to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv as mean_temp.txt
# [ ] The Weather: import world_mean_team.csv as mean_temp.txt
#Open the file in 'r' mode.
#Read the first line of text into a variable called: headings and print().
#Convert headings to a list using .split(',') which splits on each comma, print() the list.*/
# [ ] The Weather: open file, read/print first line, convert line to list (splitting on comma)
#use a while loop to read the remaining lines from the file
#Assign remaining lines to a city_temp variable.
#Convert the city_temp to a list using .split(',') for each .readline() in the loop.
#Print each city & the highest monthly average temperature.
#Close mean_temps.
#Tips & Hints:
#Use the print output of headings to determine the city_temp indexes to use.
#"month ave: highest high" for Beijing is 30.9 Celsius.
# [ ] The Weather: use while loop to print city and highest monthly average temp in celsius
#!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt
mean_temp_file=open('mean_temp.txt','r')
headings=mean_temp_file.readline()
while headings:
    headings_item=headings.split(',')
    print(headings_item[0],"\t\t",headings_item[2])
    headings=mean_temp_file.readline()
mean_temp_file.close()
#Task 3
#Random pi guessing
#Create random appearing numbers by reading digits of pi Note: only "appears" random

#Download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi as pi.txt
#Set up the project files and initial values
#Open pi.txt in read mode, the file has a single line of text "3.14....".
#Get user name as input and say "hi".
#Use the length of name for variable called seed.
#Use .seek() with the value of seed to set the initial pointer location reading the file.
#Create a variable digit and assign it the value of reading one character from the file.
#Get guess variable value from users input - "enter a single digit guess or "q" to quit".
#Initialize correct and wrong counter variables to 0 (zero).
# [ ] Set up the project files and initial values
#Create a while loop that tests that guess is a digit string
#then in the loop:
#if digit ( read from pi file) is "." read the next character for digit
#else if digit is "\n" increment seed and use seed to set the pointer using .seek()
#else see if guess is equal to digit
#a. if guess equals digit: print "correct" and increment the variable named correct
#b. if guess not equal digit: print "incorrect" and increment the variable named wrong
#end the while loop when user enters any non-digit(s) for guess, like "q".
#Print correct and wrong values within a message to the user.
#Close the pi file.

#!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi -o pi.txt
def guess_the_pi():
    pi_file=open('pi.txt','r')
    user_name=input("please provide your name: ")
    seed=len(user_name)
    pi_file.seek(seed)
    digit=pi_file.read(1)
    guess=input("enter a single digit guess or 'q' to quit: ")
    correct_counter=0
    wrong_counter=0
    while guess.isdigit():
        if digit==".":
            digit.read(seed+1)
        elif digit=="\n":
            seed+=1
            pi_file.seek(seed)
        else:
            if guess==digit:
                print("correct")
                correct_counter+=1
                break
            else:
                print("incorrect")
                wrong_counter+=1
                break
    print ("Hello Dear: ",user_name,"\n You've got correct guesses= ",correct_counter, "\n and wrong guesses= ",wrong_counter)
    pi_file.close()
#THIS DOESENT FUNCTION THE WRIGHT WAY