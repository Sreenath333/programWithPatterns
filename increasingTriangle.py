


# Right-side faced triangle

n = 5

for i in range(n):
    for j in range(i+1):
        print("_", end='  ')
    print()


#This is also one of pattern printing method
#but this will print only the n-1 value ex: (n=5) 5-1= 4


for j in range(n):
    print(j * "*  ")
