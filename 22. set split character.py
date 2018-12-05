#.split('-')
#to split on characters other than " " (space), provide .split() a string argument to use as break points
code_tip = "Python-uses-spaces-for-indentation"
tip_words = code_tip.split('-')
#Examples
#.split('-') : split with an argument
# [ ] review and run example
code_tip = "Python-uses-spaces-for-indentation"
tip_words = code_tip.split('-')

print(tip_words)
# [ ] review and run example - study the list print output
code_tip = "Python uses spaces for indentation"

# split on "a"
tip_words = code_tip.split('a')
print(code_tip)
print(tip_words)
# [ ] review and run example
# triple quotes ''' ''' preserve formatting such as spaces and line breaks
big_quote = """Jack and Jill went up the hill
To fetch a pail of water
Jack fell down and broke his crown
And Jill came tumbling after"""

# split on line breaks (\n)
quote_lines = big_quote.split('\n')
print(quote_lines, '\n')

# print the list in reverse with index slicing
for line in quote_lines[::-1]:
    print(line)