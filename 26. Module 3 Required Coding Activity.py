def poem_enter():
    poem=input("enter a poem, verse or sayin: ")
    lespom=poem.split()
    x=len(lespom)
    for xx in range(x):
        if len(lespom[xx]) <= 3:
            lespom[xx] = lespom[xx].lower()
        elif len(lespom[xx]) >=7:
            lespom[xx] = lespom[xx].upper()
    result=word_mixer(lespom)
    for xxx in range(0,len(result),3):
        print(result[xxx],result[xxx+1],result[xxx+2])

def word_mixer(whatever):
    sorted_poem = sorted(whatever)
    new_poem=[]
    while len(sorted_poem)>5:
        new_poem.append(sorted_poem.pop(-5))
        new_poem.append(sorted_poem.pop(0))
        new_poem.append(sorted_poem.pop(-1))
    return new_poem
