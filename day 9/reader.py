import copy

baseInstructions = []


def task1():
    scope = []
    with open("./codeStream.txt") as fp:
        for line in fp:
            if len(scope) < 25:
                scope.append(int(line.rstrip()))
            else :
                toCheck = int(line.rstrip())
                found = False
                for i in range(len(scope)):
                    for j in range(len(scope)):
                        if i == j :
                            continue
                        elif scope[i] + scope[j] == toCheck:
                            found = True
                            break;
                    if found:
                        break
                if not found:
                    return toCheck
                scope.append(toCheck)
                scope=scope[1:]

res = task1()
print("task 1",res)

def task2(toFind):
    scope=[]
    with open("./codeStream.txt") as fp:
        for line in fp:
            parsed = int(line.rstrip())
            if parsed == toFind:
                print("Failed")
                break
            else:
                scope.append(parsed)
                if sum(scope) == toFind:
                    return(min(scope)+max(scope))
                while sum(scope) > toFind:
                    scope=scope[1:]



print("task 2",task2(res))
