from random import randint
n = randint(1,100)

print("Guess...")
bingo = False

while bingo == False:
    answer = input()
    if answer < n:
        print("too small")
    if answer > n:
        print("too big")
    if answer == n:
        print("GINGO")
        bingo = True


        

