spam = ['apples','bananas','tofu','cats']
cheese = ['peas','bananas','tofu','cats']


for i in range(0, len(spam)):

    if i < len(spam) -1 :
        print(spam[i], end=', ')
    elif i == len(spam) -1 :
        print ("and " +  spam[i])

for i in range(len(cheese)):
    if i < len(cheese) -1:
        print(cheese[i], end=', ')
    else:
        print ("and ", cheese[i])
