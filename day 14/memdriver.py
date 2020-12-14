import re
memory = {}
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
with open("./memInstruction.txt") as fp:
    for line in fp:
        line = line.rstrip()
        if(line.startswith("mask")):
            mask = line.rsplit(" = ")[1]
        else:
            [assignment, value] = line.rsplit(" = ")
            assignment = int(re.match(r'mem\[(.*)\]',assignment).group(1))
            value = format(int(value), "b").zfill(len(mask))
            for charIdx in range(len(mask)):
                if(mask[charIdx] == "X"):
                    continue
                else:
                    value = value[:charIdx] + mask[charIdx] + value[charIdx+1:]
            memory[int(assignment)]=int(value,2)


print("task 1", sum(memory.values()))

memory = {}
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
with open("./memInstruction.txt") as fp:
    for line in fp:
        line = line.rstrip()
        if(line.startswith("mask")):
            mask = line.rsplit(" = ")[1]
        else:
            [assignment, value] = line.rsplit(" = ")
            assignment = format(
                int(re.match(r'mem\[(.*)\]', assignment).group(1)), "b").zfill(len(mask))
            value = int(value)
            addresses = []
            for charIdx in range(len(mask)):
                if(charIdx == 0):
                    if(mask[0] == "X"):
                        addresses.append("1")
                        addresses.append("0")
                    elif(mask[0] == "0"):
                        addresses = [assignment[0]]
                    else:
                        addresses = ["1"]
                    continue
                if(mask[charIdx] == "X"):
                    addresses = list(addresses)
                    addressesCp = addresses.copy()
                    addressesCp2 = addresses.copy()
                    ad1 = list(map(lambda address: address +
                              "0", addressesCp))
                    ad2 = list(map(lambda address: address +
                                   "1", addressesCp2))
                    addresses = [*ad1,*ad2]
                elif(mask[charIdx] =="0"):
                    addresses = list(map(lambda address: address +
                                    assignment[charIdx], list(addresses)))
                elif(mask[charIdx == "1"]):
                    addresses = list(map(lambda address: address+"1", list(addresses)))
            addresses = list(addresses)
            for address in addresses:
                memory[int(address,2)]= value

print("task 2", sum(memory.values()))
