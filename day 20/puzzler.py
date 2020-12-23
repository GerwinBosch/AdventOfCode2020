from functools import reduce

puzzlepieces={}
with open("./puzzle.txt") as fp:
    currentPiece=[]
    pieceId = 0
    for line in fp:
        if line.rstrip() == "":
            puzzlepieces[pieceId] = currentPiece
            pieceId = 0
            currentPiece=[]
        elif line.startswith("Tile"):
            pieceId = line[5:9]
        else:
            currentPiece.append(line.strip())
    puzzlepieces[pieceId] = currentPiece

def flipHorizontal(piece):
    return list(map(lambda x: "".join(reversed(x)), piece))
def flipVertical(piece):
    return list(reversed(piece))

def rotateRight(piece):
    newPiece = []
    for i in range(len(piece)):
        newRow =[]
        for j in range(len(piece)-1, -1,-1):
            newRow.append(piece[j][i])
        newPiece.append("".join(newRow))
    return newPiece

def printPiece(piece):
    for line in piece:
        print(line)

def comparePiecesFlipped(pieceA,pieceB):
    # Compare start
    check = comparePiecesAround(pieceA,pieceB)
    if(check):
        return check
    # Compare B H-Flip
    pieceB = flipHorizontal(pieceB)
    check = comparePiecesAround(pieceA, pieceB)
    # Horizontal + Vertical == 2 x right turn
    # Compare B V-Flip
    pieceB = flipHorizontal(pieceB)
    pieceB = flipVertical(pieceB)
    check = comparePiecesAround(pieceA, pieceB)
    if(check):
        return check
    return False

def comparePiecesAround(pieceA,pieceB):
    # Compare start
    check = comparePiecesStatic(pieceA, pieceB)
    if(check):
        return check
    # Compare B at 90
    pieceB = rotateRight(pieceB)
    check = comparePiecesStatic(pieceA, pieceB)
    if(check):
        return check
    # Compare B at 180
    pieceB = rotateRight(pieceB)
    check = comparePiecesStatic(pieceA, pieceB)
    if(check):
        return check
    # Compare B at 270
    pieceB = rotateRight(pieceB)
    check = comparePiecesStatic(pieceA, pieceB)
    if(check):
        return check
    return False

def comparePiecesStatic(pieceA, pieceB):
    # Check top and bottom
    if pieceA[0] == pieceB[-1] or pieceA[-1] == pieceB[0]:
        return True
    # Check left and right (Rotate for ease)
    pieceA = rotateRight(pieceA)
    pieceB = rotateRight(pieceB)
    if pieceA[0] == pieceB[-1] or pieceA[-1] == pieceB[0]:
        return True
    return False
    


matchesDict = {}
for pieceA in puzzlepieces:
    print("comparing",pieceA)
    matches = []
    for pieceB in puzzlepieces:
        if pieceA == pieceB:
            continue
        if(comparePiecesFlipped(puzzlepieces[pieceA], puzzlepieces[pieceB])):
            matches.append(pieceB)
    matchesDict[pieceA] = matches

print(len(matchesDict))