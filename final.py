def get_names():
    !curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
    elements=open('elements1_20.txt','r')
    elementsst=[]
    elements.seek(0,0)
    for l in range(20):
        elemen=elements.readline().strip().lower()
        elementsst.append(elemen)
    print("list any 5 of the first 20 elements in the Period table")
    elest=[]
    notele=[]
    xx=len(elest)+len(notele)
    while xx<5:
        ele=input("Enter the name of an element: ")
        if ele.lower() in elest:
            print(ele," was already entered")
        elif ele.lower() in elementsst:
            elest.append(ele.lower())
        else:
            notele.append(ele.lower())
        xx=len(elest)+len(notele)
    percentage=len(elest)*20
    print(percentage,'%' ,"correct")
    print("Found: ", elest)
    print("Not Found: ",notele)
    return
 
def Element_Quiz():
    #!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
    elements=open('elements1_20.txt','r')
    elementsst=[]
    elements.seek(0,0)
    for l in range(20):
        elemen=elements.readline().strip().lower()
        elementsst.append(elemen)
    get_names()
    


