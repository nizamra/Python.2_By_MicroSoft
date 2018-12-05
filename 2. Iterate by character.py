word = "cello"

for x in word:
    print(x)

#######
student_name = "Skye"
new_name = ""

for ltr in student_name:
    if ltr.lower() == "y":
        new_name += ltr.upper()
    else:
        new_name += ltr
print(student_name,"to",new_name)

student_name = "Skye"
for letter in student_name[:3]:
    print(letter)


student_name = "Skye"

# start at "y" (student_name[2]), iterate backwards
for letter in student_name[2::-1]:
    print(letter)

student_name = "iteration"
new_word = ""

for letter in student_name[:3]:
    new_word += letter
print(new_word)


student_name = "iteration"
count = 0
for letter in student_name:
    if letter.lower() == "o":
        print(count)
    count += 1