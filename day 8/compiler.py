import copy

baseInstructions = []
with open("./instructions.txt") as fp:
    for line in fp:
        baseInstructions.append(line.rsplit())

def runDebugger(instructions) :
    currentInstruction = 0
    accumilator = 0
    linesDone = []
    while(currentInstruction < len(instructions)):
        [command, change] = instructions[currentInstruction]
        
        if currentInstruction in linesDone :
            raise Exception("Killed at accumilator", accumilator,currentInstruction)
        linesDone.append(currentInstruction)
        if command == "nop":
            currentInstruction +=1
        elif command == "acc":
            accumilator += int(change)
            currentInstruction +=1
        elif command == "jmp":
            currentInstruction += int(change)

    return accumilator

try:
    runDebugger(baseInstructions)
except Exception as res:
    print("Task 1", res)


foundItem = False

currentReplace =0 
while (foundItem == False) :
    instructions = copy.deepcopy(baseInstructions)
    localReplace =0
    for instrIdx in range(len(instructions)):
        if instructions[instrIdx][0] == "nop" or instructions[instrIdx][0] == "jmp":
            if localReplace == currentReplace :
                if instructions[instrIdx][0] == "nop":
                    instructions[instrIdx][0] = "jmp"
                    break
                elif instructions[instrIdx][0] == "jmp":
                    instructions[instrIdx][0] = "nop"
                    break
            localReplace+=1
    try :
        print("End accumilator",runDebugger(instructions))
        foundItem = True
        break
    except Exception as res:
        currentReplace +=1
