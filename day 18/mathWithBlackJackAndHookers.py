


def calculateSum(equation):
    currentSum = 0
    currentOperator = None
    subSum = False
    depth = 0
    subSumArr = []
    for i in equation:
        if i == "(" and not subSum:
            subSum = True
        elif i == "(" and subSum:
            depth +=1
            subSumArr = [*subSumArr, i]
        elif i == ")" and depth > 0:
            depth -=1
            subSumArr = [*subSumArr, i]
        elif i == ")" and depth == 0:
            subSum = False
            if currentOperator == "+":
                    currentSum+=calculateSum(subSumArr)
            elif currentOperator == "*":
                currentSum *= calculateSum(subSumArr)
            else :
                currentSum = calculateSum(subSumArr)
            subSumArr=[]
        elif subSum:
            subSumArr=[*subSumArr,i]
        elif i == "+" or i == "*":
            currentOperator = i
        elif currentSum == 0:
            currentSum = int(i)
        else:
            if currentOperator == "+":
                currentSum+=int(i)
            elif currentOperator == "*":
                currentSum*=int(i)
    return currentSum


def calculatePrioPlusSum(equation):
    subSum = True
    depth = 0
    while subSum:
        subSum= False
        # print(equation)
        for i in range(len(equation)):
            if equation[i] == "(" and not subSum:
                subSum = True
                subSumStart=i
            elif equation[i] == "(" and subSum:
                depth += 1
            elif equation[i] == ")" and depth > 0 and subSum:
                depth -= 1
            elif equation[i] == ")" and depth == 0 and subSum:
                equation = [*equation[:subSumStart], str(calculatePrioPlusSum(
                    equation[subSumStart+1:i])), *equation[i+1:]]
                break
    subSum = True
    while subSum:
        subSum = False
        for i in range(len(equation)):
            if equation[i] == "+":
                subSum = True
                equation = [*equation[:i-1], str(int(equation[i-1])+int(equation[i+1])), *equation[i+2:]]
                break
    subSum = True

    while subSum:
        subSum = False
        for i in range(len(equation)):
            if equation[i] == "*":
                subSum = True
                equation = [*equation[:i-1], str(int(equation[i-1])*int(equation[i+1])), *equation[i+2:]]
                break
    return int(equation[0])


with open("./input.txt") as fp:
    print("task 1", sum([calculateSum([x for x in line.rstrip() if x != " "]) for line in fp]))
with open("./input.txt") as fp:
    print("task 2", sum([calculatePrioPlusSum(
        [x for x in line.rstrip() if x != " "]) for line in fp]))
