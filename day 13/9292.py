from functools import reduce
now = 0
lines = []

with open("./schedule.txt") as fp:
    new = int(fp.readline().rstrip())
    lines = fp.readline().rstrip().rsplit(", ")
print(now,lines)

activeLines = map(lambda y: (int(y) - new % int(y), y, (int(y) - new %
                             int(y) )* int(y)), filter(lambda x: x != "x", lines))

print("task 1", min(activeLines)[-1])

def calculateDepart(currentWindow):
    for item in range(len(currentWindow)):
        if currentWindow[item] != 0 and int(currentWindow[item]) - int(currentWindow[0]) != item:
            return False
    return True

# Will eventually work, will take a huge amount of time
# Works for the examples (Processing time atm ~1,5 days)
currentLines = list(map(lambda x: 0 if  (x == "x") else int(x),lines.copy()))
distanceBook = {}
counter = 0
for item in currentLines:
    if(item == 0):
        counter+=1
    else:
        distanceBook[item] = counter
        counter +=1
sortedBySize = list(distanceBook.keys())
sortedBySize.sort()
sortedBySize = list(reversed(sortedBySize))
print(reduce(lambda x,y: x *y,sortedBySize), reduce(lambda x,y: x + distanceBook[y],sortedBySize ))
curr = int(100000000000000 / sortedBySize[0]) * sortedBySize[0]
currInt = distanceBook[sortedBySize[0]]
print(sortedBySize, distanceBook)
while True:
    print(curr)
    valueToCheck = curr-currInt
    # print(valueToCheck)
    for item in range(len(sortedBySize)):
        found = True
        if (valueToCheck + distanceBook[sortedBySize[item]]) % sortedBySize[item] != 0:
            found =False
            break
    if(found):
        print("task 2", curr - currInt)
        break
    curr += sortedBySize[0]


