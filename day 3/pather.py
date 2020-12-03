right = 0
treeCounter = 0
firstTask = False

def goSki(stepsizeLeft, stepsizeDown) :
    right = 0
    treeCounter = 0
    with open("./forest.txt") as fp:
        line = fp.readline().rstrip()
        while line :
            if line[right % len(line)] == "#":
                treeCounter+=1
            right +=stepsizeLeft
            goDown = stepsizeDown
            while goDown != 1:
                fp.readline()
                goDown-=1
            line = fp.readline().rstrip()
    return treeCounter

firstResult = goSki(3,1)
print("First task:", firstResult)
print("Second task:", goSki(1,1) * firstResult * goSki(5,1) * goSki(7,1) * goSki(1,2))