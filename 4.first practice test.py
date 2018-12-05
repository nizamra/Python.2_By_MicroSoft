def words_after_g():
    quote=input("enter a quote here: ")
    word=""
    for x in quote:
        if x.isalpha():
            word+=x
        elif x.isalpha() == False:
            if word.lower() >= "h":
                print(word.upper())
                word=""
            else:
                word=""
    if word.lower() >= "h":
        print(word.upper())



quote = "they stumble who run fast"

start = 0
space_index = quote.find(" ")
while space_index != -1:
    print(quote[start:space_index])
    start = space_index + 1
    space_index = quote.find(" ", space_index + 1)
print(quote[start:])



quote = "they stumble who run fast"
start = 0
space_index = quote.find(" ")
while space_index != -1:
        print(quote[start:space_index])
        start=space_index+1
        space_index = quote.find(" ",space_index +1)
print(quote[start:len(quote)]) #For last word