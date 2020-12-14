from functools import reduce

floorplan = []



def freeSeats(rowIdx, columnIdx,floorSeats):
    free = 0
    for height in range(-1,2):
        for width in range(-1,2):
            if rowIdx + height == -1 or rowIdx + height == len(floorSeats) or columnIdx + width == -1 or columnIdx + width == len(floorSeats[0]):
                free += 1
                continue
            seatAt = floorSeats[rowIdx + height][columnIdx+width]
            if(seatAt == "L" or seatAt == "."):
                free += 1

    return free



changes = 10000
currentFloorplan = floorplan.copy()
iterationCounter = 0
while changes != 0:
    iterationCounter+=1
    changes =0
    newFloorplan = []
    for rowIdx in range(len(floorplan)):
        row = []
        for seatIdx in range(len(currentFloorplan[rowIdx])):
            currentSeat = currentFloorplan[rowIdx][seatIdx]
            if currentSeat == ".":
                row.append(currentSeat)
            else :
                freeSeatCount = freeSeats(rowIdx, seatIdx, currentFloorplan)
                if(currentSeat == "L" and freeSeatCount == 9):
                    changes +=1
                    row.append("#")
                elif(currentSeat == "#" and freeSeatCount < 5):
                    changes +=1
                    row.append("L")
                else:
                    row.append(currentSeat)
        newFloorplan.append(row)
    currentFloorplan=newFloorplan


print("task 1", reduce(lambda x, y: x +
                       len(list(filter(lambda s: s == "#",y))), currentFloorplan,0))


def occupiedSeatsIndefinetely(rowIdx, columnIdx, floorSeats,pauseAt):
    occupied = 0

    for heightStep in range(-1, 2):
        for widthStep in range(-1, 2):
            currentHeight = rowIdx + heightStep
            currentWidth = columnIdx + widthStep
            if(heightStep == 0 and widthStep == 0):
                continue
            found = False
            while currentHeight >= 0 and currentHeight < len(floorSeats) and currentWidth >= 0 and currentWidth < len(floorSeats[0]) and not found:
                if floorSeats[currentHeight][currentWidth] == "L":
                    found = True
                if floorSeats[currentHeight][currentWidth] == "#":
                    occupied +=1
                    found =True
                currentHeight = currentHeight + heightStep
                currentWidth = currentWidth + widthStep

    return occupied

changes = 10000
currentFloorplan = floorplan.copy()
iterationCounter = 0

while changes != 0:
    
    changes = 0
    newFloorplan = []
    for rowIdx in range(len(floorplan)):
        row = []
        for seatIdx in range(len(currentFloorplan[rowIdx])):
            currentSeat = currentFloorplan[rowIdx][seatIdx]
            if currentSeat == ".":
                row.append(currentSeat)
            else:
                occupied = occupiedSeatsIndefinetely(rowIdx, seatIdx, currentFloorplan,iterationCounter)
                if(currentSeat == "L" and occupied == 0):
                    changes += 1
                    row.append("#")
                elif(currentSeat == "#" and occupied >= 5):
                    changes += 1
                    row.append("L")
                else:
                    row.append(currentSeat)
        newFloorplan.append(row)
    currentFloorplan = newFloorplan
    iterationCounter += 1

print("task 2", reduce(lambda x, y: x +
                       len(list(filter(lambda s: s == "#", y))), currentFloorplan, 0))
