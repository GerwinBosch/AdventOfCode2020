initialNumbers = [15, 5, 1, 4, 7, 0]
while(len(initialNumbers)) != 2020:
    toCheck = initialNumbers[-1]
    if(initialNumbers.count(toCheck) == 1):
        initialNumbers.append(0)
    else :
        for i in range(len(initialNumbers)-2,-1,-1):
            if i == len(initialNumbers):
                continue
            elif(initialNumbers[i] == toCheck):
                initialNumbers.append(len(initialNumbers)-1-i)
                break
print("task 1", initialNumbers[-1])
countIdx ={
    15:1,
    5:2,
    1:3,
    4:4,
    7:5,
    0:6
}
lastNumber = 0
turnCounter = 7
while turnCounter != 30000000:
    if lastNumber in countIdx:
        prev = countIdx[lastNumber]
        countIdx[lastNumber] = turnCounter
        lastNumber=turnCounter - prev
    else:
        countIdx[lastNumber]=turnCounter
        lastNumber = 0
    turnCounter += 1
print("task 2", lastNumber)
