""
i = 0
while i < 5:
    j = 0
    while j < i:
        print("*")

        j += 1
    i += 1
    print("")

i = 0
while i < 5:
    j = 0
    while j < 5:
        print("*", end="\t")
        #print("")
        j += 1
    i += 1
print("")
    """
row = 1
while row <= 5:
    lie = 1
    while lie <= 5:
        print("*", end="")
        lie += 1
    row += 1
    print("")
