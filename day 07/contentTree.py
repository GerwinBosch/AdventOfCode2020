# From : a
# To : B
#  Weight : number

def trimBag(bag):
    return " ".join(bag.split(" ")[0:2])
# Task 1
mapper = []
with open("./rules.txt") as fp:
    for line in fp:
        line = line.rstrip()[:-1]
        preCleanSubject, contains = line.split("contain")
        contains = contains.split(',')
        subject = trimBag(preCleanSubject)
        for entry in contains:
            try :
                mapper.append((subject, trimBag(entry[3:-1]), int(entry[1], 10)))
            except :
                mapper.append((subject, None, 1))
toFind ="shiny gold"
canContainGoldBag = []

def containsGoldBag(startNode,toFind, entries):
    subList = list(filter(lambda entry: entry[0]==startNode, entries))
    added = False
    for (subject, to, weight) in subList:
        if subject in canContainGoldBag:
            added = True
        elif to == toFind:
            added = True
            canContainGoldBag.append(subject)
        else :
            added= added or containsGoldBag(to, toFind, entries)
            if(added):
                canContainGoldBag.append(subject)
    return added


def getGold(startNode, entries):
    added = 0
    subList = list(filter(lambda entry: entry[0] == startNode, entries))
    for (fro, to, weight) in subList:
        if to == None:
            added +=0
        else:
            added += weight + weight * getGold(to,entries)
        print(fro, added)
    return added
print(getGold(toFind, mapper))
