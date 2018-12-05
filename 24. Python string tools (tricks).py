#Cast a string to a list of characters
hello_letters = list("Hello")
#print to the same line with multiple print statements (end=)
#or insert any character as an end in print("String", end="+")

print('Hello', end = '')
print('world')
#Examples
# [ ] review and run example
hello_letters = list("Hello")
print(hello_letters)
# [ ] review and run example
# cast sting to list
word_letters = list("concatenates")

# .join() concatenates the list
# print on same line setting the end character
print('~'.join(word_letters))
# [ ] review and run example
print("Hello ", end = '')
print("world")
# [ ] review and run example
# This  is the default print end
print("Hello World!", end="\n")
print('still something to learn about print()')
# [ ] review and run example
# end inserts any valid str character: A-z, 0-9,!,@,*,\n,\t or ''(empty string)...
for letter in "Concatenation":
    print(letter, end='*')


tip = 'Strings are a sequence of characters'
tip_list = tip.split()
tip_list

wisdom_list = ["mistakes", "are", "a", "part", "of", "learning"]
wisdom_string = "()".join(wisdom_list)
print(wisdom_string)

code_tip = "-PythonO-usesO-spacesO-forO-indentation"
tip_words = code_tip.split('O')
print(tip_words)