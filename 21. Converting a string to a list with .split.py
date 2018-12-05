#Converting a string to a list with .split()
#.split() by default, splits a string at spaces (" ") to create a list
tip = "Notebooks can be exported as .pdf"
tip_words = tip.split()

for word in tip_words:
    print(word)
#Examples
# [ ] review and run example
tip = "Notebooks can be exported as .pdf"
tip_words = tip.split()

print("STRING:", tip)
print("LIST:", tip_words, "\n")

for word in tip_words:
    print(word)
# [ ] review and run example
rhyme = "London bridge is falling down"

rhyme_words = rhyme.split()

rhyme_words.reverse()

for word in rhyme_words:
    print(word)