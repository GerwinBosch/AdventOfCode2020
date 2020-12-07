def parseSeat(input):
    rowString, columnString = input[:7], input[7:]
    row = int(rowString.replace("F", "0").replace("B", "1"), 2)
    column = int(columnString.replace("L", "0").replace("R", "1"), 2)
    return row * 8 + column


# Task 1
with open("./inputData.txt") as fp:
    currentCount = 0
    answeredQuestions = set({})
    for line in fp:
        line = line.rstrip()
        if len(line) == 0:
            currentCount += len(answeredQuestions)
            answeredQuestions = set({})
        else:
            for letter in list(line):
                answeredQuestions.add(letter)
currentCount += len(answeredQuestions)
answeredQuestions = set({})
print("task 1", currentCount)

# Task 2
with open("./inputData.txt") as fp:
    resSet = 0
    questionaire = []
    for line in fp:
        line = line.rstrip()
        if len(line) == 0:
            resSet += len(questionaire[0].intersection(*questionaire[1:]))
            questionaire = []
        else:
            questionaire.append(set(line))
            
resSet += len(questionaire[0].intersection(*questionaire[1:]))

print("Task 2", resSet)
