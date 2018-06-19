numberOfTerms = int(input())
q = [0] * numberOfTerms
R = 0
placeHolder = [0] * numberOfTerms
for i in range(0, numberOfTerms):
    q[i] = input()
    powerVal = q[i][(int(len(q[i]))- 1)]
    placeHolder[i] = q[i][0:(int(len(q[i]))- 1)]
    R += int(placeHolder[i]) ** int(powerVal)
print(R)
