position = [0,0]
facing = 90

with open("./instructions.txt") as fp:
    for line in fp:
        instruction,*distance = line.rstrip()
        distance = int("".join(distance))
        if instruction == "N":
            position[1] += distance
        elif instruction == "S":
            position[1] -= distance
        elif instruction == "E":
            position[0] += distance
        elif instruction == "W":
            position[0] -= distance
        elif instruction == "R":
            facing = (facing + distance) % 360
        elif instruction == "L":
            newPos = facing - distance
            if distance < 0:
                newPos = 360 - newPos
            facing = newPos % 360
        elif instruction == "F":
            newFacing = abs(facing / 90)
            if newFacing == 0:
                position[1]+= distance
            elif newFacing == 1:
                position[0]+= distance
            elif newFacing == 2:
                position[1]-= distance
            elif newFacing == 3:
                position[0]-= distance
print("task 1",sum(map(lambda x: abs(x),position)))

shipPos = [0,0]
waypointPos = [10,1]

with open("./instructions.txt") as fp:
    for line in fp:
        instruction, *distance = line.rstrip()
        distance = int("".join(distance))
        if instruction == "N":
            waypointPos[1] += distance
        elif instruction == "S":
            waypointPos[1] -= distance
        elif instruction == "E":
            waypointPos[0] += distance
        elif instruction == "W":
            waypointPos[0] -= distance
        elif instruction == "R":
            if distance == 180:
                waypointPos = list(map(lambda x: x * -1, waypointPos))
            elif distance % 360 ==0:
                continue
            else:
                for i in range(int(distance/90)):
                    ew, ns = waypointPos
                    waypointPos=[ns,ew * -1]
        elif instruction == "L":
            if distance == 180:
                waypointPos = list(map(lambda x: x * -1,waypointPos))
            elif distance % 360 == 0:
                continue
            else:

                for i in range(int(distance/90)):
                    ew, ns = waypointPos
                    waypointPos = [ns * -1, ew]
        elif instruction == "F":
            shipPos = [shipPos[0]+ waypointPos[0] * distance, shipPos[1] + waypointPos[1] * distance]

print("task 2", sum(map(lambda x: abs(x), shipPos)))

