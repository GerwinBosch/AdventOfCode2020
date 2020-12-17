cube = [[[
    [".", ".", "#", ".", ".", "#", "#", "."],
    ["#", ".", ".", ".", ".", ".", "#", "#"],
    ["#", "#", ".", "#", ".", "#", ".", "#"],
    [".", ".", "#", ".", ".", ".", "#", "."],
    [".", "#", "#", "#", ".", ".", ".", "."],
    ["#", "#", "#", "#", "#", "#", ".", "."],
    [".", "#", "#", "#", ".", ".", "#", "."],
    [".", ".", "#", ".", ".", "#", "#", "."],
]]]
# cube = [[[[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]]]

iteration = 0


def countActiveNeightBours(z, y, x, w, cube):
    activeCount = 0
    for zAxis in range(-1, 2):
        if(z+zAxis < 0 or z+zAxis >= len(cube)):
            continue
        for yAxis in range(-1, 2):
            if(y+yAxis < 0 or y+yAxis >= len(cube[0])):
                continue
            for xAxis in range(-1, 2):
                if(x+xAxis < 0 or x+xAxis >= len(cube[0][0])):
                    continue
                for wAxis in range(-1, 2):
                    if(zAxis == 0 and yAxis == 0 and xAxis == 0 and wAxis == 0):
                        continue
                    if(w+wAxis < 0 or w+wAxis >= len(cube[0][0][0])):
                        continue
                    if(cube[z+zAxis][y+yAxis][x+xAxis][w+wAxis] == "#"):
                        activeCount += 1
    return activeCount


while iteration < 6:
    print("iteration", iteration)
    # Initial expansion
    zLength = len(cube)
    ylength = len(cube[0])
    xlength = len(cube[0][0])
    wlength = len(cube[0][0][0])
    nX = xlength+2
    nY = ylength+2
    nW = wlength+2
    # First iteration only grows in z dimension
    for zSliceIdx in range(zLength):
        for ySlizeIdx in range(ylength):
            for xSliceIdx in range(xlength):
                cube[zSliceIdx][ySlizeIdx][xSliceIdx] = [
                    ".", *cube[zSliceIdx][ySlizeIdx][xSliceIdx], "."]

            cube[zSliceIdx][ySlizeIdx] = [["."] * nW,*cube[zSliceIdx][ySlizeIdx], ["."]*nW]

        cube[zSliceIdx] = [[["."]*nW]*nX,*cube[zSliceIdx],[["."]*nW]* nX]
    cube = [[[["."]*nW]*nX]*nY, *cube, [[["."]*nW]*nX]*nY]

    cube = [[[["#" if cube[zSlice][ySlice][xSlice][w] == "#" and (countActiveNeightBours(zSlice, ySlice, xSlice, w, cube) == 2 or countActiveNeightBours(zSlice, ySlice, xSlice, w, cube) == 3) else "." if cube[zSlice][ySlice][xSlice][w] == "#" else "#" if cube[zSlice][ySlice][xSlice][w] == "." and countActiveNeightBours(zSlice, ySlice, xSlice, w, cube) == 3 else cube[zSlice][ySlice][xSlice][w]for w in range(len(cube[0][0][0]))] for xSlice in range(len(cube[0][0]))] for ySlice in range(
        len(cube[0]))] for zSlice in range(len(cube))]
    iteration += 1

activeCount = [w for z in cube for y in z for x in y for w in x].count("#")
print(activeCount)
