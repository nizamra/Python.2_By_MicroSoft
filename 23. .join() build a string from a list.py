#.join() build a string from a list
#.join() is a method applied to a separator string and iterates through its argument
tip_words = ['Notebooks', 'can', 'be', 'exported', 'as', '.pdf'] 

" ".join(tip_words)
#a space (" ") is the separator that gets injected between the objects in the argument (the list "tip_words")

#Examples
#.join()
# [ ] review and run example
tip_words = ['Notebooks', 'can', 'be', 'exported', 'as', '.pdf'] 

# join tip_words objects with spaces
print(" ".join(tip_words))
# [ ] review and run example
no_space = ""
letters = ["P", "y", "t", "h", "o", "n"]
print(no_space.join(letters))
# [ ] review and run example - .join() iterates through sequences
dash = "-"
space = " "
word = "Iteration"
ellipises = "..."

dash_join = dash.join(word)
print(dash_join)
print(space.join(word))
print(ellipises.join(word))