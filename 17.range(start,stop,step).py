#The range(stop) function creates a sequence
#range runs from 0 through the integer before stop
for count in range(10):
  print(count)
# review and run example
digits = range(10)
print("digits =", list(digits), "\n")

for count in digits:
    print(count)
# [ ] review and run example
sub_total = 0
for item in range(10):
    sub_total += item
    print("sub_total:", sub_total)
print("Total =", sub_total)
# [ ] review and run example
# print the first half of a spelling list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

# find length of 1st half of list (must be int)
half_1 = int(len(spell_list)/2)

for word in range(half_1):
    print(spell_list[word])



#The range(start,stop) function creates a sequence
#using 2 arguments with range(start,stop)
#start: starting integer value of a range loop
#stop: stopping integer (second argument), does not process stop number
for count in range(5,10):
  print(count)
#range runs from start integer through the integer before stop
for count in range(5,10):
  print(count)
# [ ] review and run example
sub_total = 0
temp = 0
for item in range(5, 11):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=",sub_total)
print("Total =", sub_total)
# [ ] review and run example

spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

# find length list 
spell_len = len(spell_list)
# find lenght of 1st half (aka - start of 2nd half)
half_1 = int(spell_len/2)

# print 2nd half list
for word in range(half_1,spell_len):
    print(spell_list[word])



#range(start,stop,step)
#The range(start,stop,step) function creates a sequence
#using 3 arguments with range(start,stop,step)
#start: starting integer value of a range loop
#stop: stopping integer (second argument), does not process stop number
#step: skip value for each loop
for count in range(25,101,25):
  print(count)
# [ ] review and run example
sub_total = 0
temp = 0
for item in range(25,46,5):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=",sub_total)
print("Total =", sub_total)
# [ ] review and run example printing the 1st and then every other word in spell_list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

for index in range(0,len(spell_list),2):
    print(spell_list[index])
# [ ] review and run example casting range to list
odd_list = list(range(1,20,2))
print(odd_list)




numbers = ""
for x in range(7):
    numbers += str(x)
print(numbers)



numbers = ""
for x in range(2,8,2):
    numbers += str(x)
print(numbers)



numbers = ""
for x in range(0,5,2):
    numbers += str(x)
print(numbers)