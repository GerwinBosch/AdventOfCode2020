from functools import reduce

ladapterList = []
with open("./small.txt") as fp:
    for line in fp:
        ladapterList.append(int(line.rstrip()))
ladapterList.sort()


def task_1(adapterList):
    diffCount = {
        1: 1,
        3: 1
    }
    for i in range(1, len(adapterList)):
        diff = adapterList[i] - adapterList[i-1]
        if diff not in diffCount:
            diffCount[diff] = 1
        else:
            diffCount[diff] += 1
    return diffCount[1] * diffCount[3]


result_1 = task_1(ladapterList)
print("task 1", result_1)


def task_2(adapterList, maxPower):
    # possibilites = 0
    # queue = [0]
    # calculatedItems = {max(adapterList)+3:1}
    # adapterList.append(max(adapterList)+3)
    # while not len(queue) == 0:
    #     print(calculatedItems)
    #     currentItem = queue.pop(-1)
    #     nextItems = list(filter(lambda x: x > currentItem and x -
    #                        currentItem <= 3, adapterList))
    #     nextItems.sort()
    #     print(currentItem)
    #     for item in nextItems:
    #         queue.append(item)
    #         queue.sort()

    # return possibilites

    pathDict = {}
    adapterList.append(max(adapterList)+3)
    adapterList.append(0)
    adapterList.sort()
    for adapter in adapterList:
       pathDict[adapter] = list(filter(lambda x: x > adapter and x -
                                       adapter <= 3, adapterList))
    print(pathDict)
    for key in reversed(pathDict.keys()):
        if len(pathDict[key]) ==0 :
            pathDict[key] = 1
            continue
        pathDict[key]=sum(map(lambda x: pathDict[x],pathDict[key]))
    print(pathDict)
    return pathDict[0]
print("task_2", task_2(ladapterList, result_1))
