DominantAndN = list(input())
if ' ' in DominantAndN:
    DominantAndN.remove(' ')
n = DominantAndN[0]
B = DominantAndN[1]
N = int(n) * 4
totalSum = 0

holderList = [0] * 2
responses = [0] * N
for i in range(0, N):
    responses[i] = input()
    holderList = list(responses[i])
    n = holderList[0]
    if B == holderList[1]:
        if n == 'J':
            totalSum = totalSum + 20
        if n == '9':
            totalSum = totalSum + 14
    if n == 'K':
        totalSum = totalSum + 4
    if n == 'A':
        totalSum = totalSum + 11
    if n == 'Q':
        totalSum = totalSum + 3
    if ((n == 'J') and (B != holderList[1])):
        totalSum = totalSum + 2
    if n == 'T':
        totalSum = totalSum + 10
        
print(totalSum)
                


