list = []

with open("./numbers.txt") as fp:
    line = fp.readline()
    while line :
        list.append(int(line.rstrip()))
        line = fp.readline()

# for entry in list:
#     for otherEntry in list:
#         if entry + otherEntry == 2020:
#             print(entry * otherEntry)
#     # Might as well remove the one we're checking for
#     list.pop(0)

# ? Part 2
for entry in list:
    for otherEntry in list:
        for thirdEntry in list:
            
            if entry + otherEntry + thirdEntry == 2020:
                print(entry * otherEntry * thirdEntry)
    # Might as well remove the one we're checking for
    list.pop(0)

