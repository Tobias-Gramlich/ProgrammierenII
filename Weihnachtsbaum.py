import random as rand

for x in range(10):
    Z = 0
    print(" " * round((10 - x)/2), end="")
    while x >= 0:
        rnd = rand.randint(1 , 4)
        if rnd == 1:
            print("o" ,end="")
            Z = Z + 1 
        else:
            print("*", end="")
        x = x - 1
    print("")
for x in range(2):
    print("    ", end="")
    print("**")
print("   ****")
    
