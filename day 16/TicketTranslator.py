from functools import reduce

validNumber = {}
myTicket = []
otherTickets = []
with open("./input.txt") as fp:
    currentSegment = 0
    for line in fp:
        if(line.rstrip() == ""):
            currentSegment+=1
            continue
        if(currentSegment == 0):
            [rule, ranges] = line.strip().split(":")
            validNumber[rule.strip()] =  list(
                map(lambda x: [int(s) for s in x.strip().split("-")], ranges.split(" or ")))
        elif(currentSegment == 1):
            if(line.rstrip() == "your ticket:"):
                continue
            myTicket=[int(s) for s in line.strip().split(',')]
        elif(currentSegment == 2):
            if(line.rstrip() == "nearby tickets:"):
                continue
            otherTickets.append([int(s) for s in line.strip().split(',')])

errorRate = 0
errorTickets = []
for ticket in otherTickets:
    for ticketNumber in ticket:
        valid = False
        for ranges in validNumber.values():
            if(ticketNumber >= ranges[0][0] and ticketNumber <= ranges[0][1]) or (ticketNumber >= ranges[1][0] and ticketNumber <= ranges[1][1]):
                valid = True
                break;
        if not valid:
            errorRate+=ticketNumber
            errorTickets.append(ticket)
print("task 1",errorRate)
for ticket in errorTickets:
    otherTickets.remove(ticket)

validIdx ={}
for key in validNumber.keys():
    validIdx[key] = list(range(len(myTicket)))

for ticket in otherTickets:
    for ticketNumberIdx in range(len(ticket)):
        isValidIn = list(map(lambda rule: (ticket[ticketNumberIdx] >= rule[1][0][0] and ticket[ticketNumberIdx] <= rule[1][0][1]) or (
            ticket[ticketNumberIdx] >= rule[1][1][0] and ticket[ticketNumberIdx] <= rule[1][1][1]), validNumber.items()))
        for ruleToCheckIdx in range(len(isValidIn)):
            if not isValidIn[ruleToCheckIdx]:
                validIdx[list(validNumber.keys())[ruleToCheckIdx]].remove(ticketNumberIdx)

items = list(validIdx.items())
items.sort(key=lambda x: len(x[1]))
for item in items:
    if not len(item[1]) == 1:
        raise Exception("List was longer then expected")
    else:
        for subItem in items:
            if(len(subItem[1]) == 1):
                continue
            subItem[1].remove(item[1][0])

items=dict(items)
myTicket = dict(map(lambda key: [key, myTicket[items[key][0]]], validNumber.keys()))
departureKeys = filter(lambda x: x.startswith("departure") ,myTicket.keys())

print("Task 2", reduce(lambda acc,val: acc*val,map(lambda x: myTicket[x],departureKeys)))
