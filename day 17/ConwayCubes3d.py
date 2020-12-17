cube = [[
    [".", ".", "#", ".", ".", "#", "#", "."],
    ["#", ".", ".", ".", ".", ".", "#", "#"],
    ["#", "#", ".", "#", ".", "#", ".", "#"],
    [".", ".", "#", ".", ".", ".", "#", "."],
    [".", "#", "#", "#", ".", ".", ".", "."],
    ["#", "#", "#", "#", "#", "#", ".", "."],
    [".", "#", "#", "#", ".", ".", "#", "."],
    [".", ".", "#", ".", ".", "#", "#", "."],
]]
# cube = [[[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]]

iteration = 0


def countActiveNeightBours(z, y, x, cube):
    activeCount = 0
    for zAxis in range(-1, 2):
        if(z+zAxis < 0 or z+zAxis >= len(cube)):
            continue
        for yAxis in range(-1, 2):
            if(y+yAxis < 0 or y+yAxis >= len(cube[0])):
                continue
            for xAxis in range(-1, 2):
                if(zAxis == 0 and yAxis == 0 and xAxis == 0):
                    continue
                if(x+xAxis < 0 or x+xAxis >= len(cube[0][0])):
                    continue
                if(cube[z+zAxis][y+yAxis][x+xAxis] == "#"):
                    activeCount += 1
    return activeCount


while iteration < 6:
    # Initial expansion
    zLength = len(cube)
    ylength = len(cube[0])
    xlength = len(cube[0][0])
    newXlength = xlength+2
    newYlength = ylength+2
    # First iteration only grows in z dimension
    for zSliceIdx in range(zLength):
        for ySlizeIdx in range(ylength):
            cube[zSliceIdx][ySlizeIdx] = [
                ".", *cube[zSliceIdx][ySlizeIdx], "."]
        cube[zSliceIdx] = [["."] * newXlength,
                           *cube[zSliceIdx], ["."] * newXlength]
    cube = [
        [["."]*(newXlength)]*(newYlength),
        *cube,
        [["."]*(newXlength)]*(newYlength),
    ]
    cube = [[["#" if cube[zSlice][ySlice][x] == "#" and (countActiveNeightBours(zSlice, ySlice, x, cube) == 2 or countActiveNeightBours(zSlice, ySlice, x, cube) == 3) else "." if cube[zSlice][ySlice][x] == "#" else "#" if cube[zSlice][ySlice][x] == "." and countActiveNeightBours(zSlice, ySlice, x, cube) == 3 else cube[zSlice][ySlice][x] for x in range(len(cube[0][0]))] for ySlice in range(
        len(cube[0]))] for zSlice in range(len(cube))]
    iteration += 1

activeCount = [x for z in cube for y in z for x in y].count("#")
print("task 1", activeCount)
