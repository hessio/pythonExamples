N = int(input())
inputLine = [0] * 3
totalCcst = 0
for i in range(0, N):
    inputLine = input().split(" ")
    r = int(inputLine[0])
    e = int(inputLine[1])
    c = int(inputLine[2])
    totalCost = e - c
    #r is revenue without advertising
    #e is Expected revenue if you do advertise
    #c is cost of advertising
    
    if totalCost > r:
        print("advertise")
    elif totalCost == r:
        print("does not matter")
    else:
        print("do not advertise")
