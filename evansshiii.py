import string

comparenames = [["Evan","Tyler"],["Carlos","Carlos"],["Craig","Dan"],["Patrick","Alexander"]]

for name in comparenames:

    letters = string.ascii_lowercase
    
    name1 = name[0]
    name2 = name[1]

    if letters.index(name1[0]) > letters.index(name2[0]):
        print(name2)
        print(name1)
    elif letters.index(name1[0]) < letters.index(name2[0]):
        print(name1)
        print(name2)
    else:
        print("You have entered the same name twice, error!")
        break