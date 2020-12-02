lineMatrix = []
firstTask = False
with open("./input.txt") as fp:
    line = fp.readline()
    while line :
        lineSegments = line.rstrip().split(" ")
        limits = lineSegments[0].split('-')
        # min max letter password
        lineMatrix.append([int(limits[0]),int(limits[1]), lineSegments[1][0], lineSegments[2] ])
        line = fp.readline()

correctCount = 0
if firstTask :
    for [low,high,letter,password] in lineMatrix:
        count = password.count(letter);
        if low <= count and count <= high:
            correctCount+=1
else :
    for [firstPosition,secondPosition,letter,password] in lineMatrix:
        if password[firstPosition-1] == letter and password[secondPosition-1] != letter:
            correctCount+=1
        elif password[secondPosition-1] == letter and password[firstPosition-1] != letter:
            correctCount+=1

print(correctCount)