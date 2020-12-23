import sys
rules = {}
sys.setrecursionlimit(1900)  # 10000 is an example, try with different values


def checkRules(toCheck, rules, currentRule=0):
    rule = rules[currentRule]
    if not rule:
        raise Exception("help")
    if type(rule) == list and type(rule[0]) == int:
        for segment in rule:
            toCheck = checkRules(toCheck, rules,segment)
            if toCheck == "":
                1+1
            elif not toCheck:
                return False
        return toCheck
    elif type(rule) == list and type(rule[0] == list):
        firstCheck = checkRules(toCheck, rules, rule[0][0])
        if firstCheck or firstCheck is "":
            for segment in rule[0][1:]:
                firstCheck = checkRules(firstCheck, rules, segment)
                if firstCheck == False:
                    break
            if firstCheck or firstCheck is "":
                return firstCheck
        secondCheck = checkRules(toCheck, rules, rule[1][0])
        if secondCheck or secondCheck == "":
            for segment in rule[1][1:]:
                secondCheck = checkRules(secondCheck, rules, segment)
                if secondCheck == False:
                    break
            if secondCheck or secondCheck == "":
                return secondCheck
        if firstCheck or firstCheck is "":
            return firstCheck
        if secondCheck or secondCheck is "":
            return secondCheck
        return False
    elif type(rule) == str:
        if toCheck == "":
            return False
        elif toCheck[0] == rule:
            return toCheck[1:]
        else:
            return False
    else:
        print("nohing",toCheck, rule)

DoTaskTwo = True
with open("./input.txt") as fp:
    goodCounter = 0
    badCounter = 0
    rulesSegment=True
    for line in fp:
        if line.rstrip() == "":
            if DoTaskTwo:
                rules[8] = [[42], [42, 8]]

                rules[11] = [[42, 31], [42, 11, 31]]
            for line in rules:
                print(line,rules[line])
            rulesSegment = False
            continue
        if rulesSegment:
            # Rules Read fragment
            [rule, refs] = line.rstrip().split(": ")
            if refs[0] == "\"":
                rules[int(rule)] = refs[1]
            elif "|" in refs:
                refs = refs.split("|")
                rules[int(rule)] = [[int(x) for x in ref.split(" ") if x != ""]
                                    for ref in refs]
            else :
                rules[int(rule)] = [int(x) for x in refs.split(" ") if x != " "]
        else :
            res = checkRules(line.rstrip(), rules)
            print(line.rstrip(),res, res == "")
            if(res == ""):
                goodCounter+=1
            else:
                badCounter+=1
            # input("press enter")
            

print(goodCounter,badCounter)




