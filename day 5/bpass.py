def parseSeat(input):
    rowString, columnString = input[:7], input[7:] 
    row = int(rowString.replace("F", "0").replace("B", "1"),2)
    column = int(columnString.replace("L", "0").replace("R","1"),2)
    return row * 8 + column

# Task 1
with open("./boardingpasses.txt") as fp:
    maxId=0
    for line in fp:
        line = line.rstrip()
        maxId = max([maxId,parseSeat(line)])
    print("maxId",maxId)

# Task 2
with open("./boardingpasses.txt") as fp:
    passes = []
    for line in fp:
        line = line.rstrip()
        passes.append(parseSeat(line))
    passes.sort()
    for i in range(len(passes)):
        if passes[i+1] - passes[i] == 2:
            print("My seat id", passes[i]+1)
            break
