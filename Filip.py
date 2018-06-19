A, B = input().split(" ")
aReversed = A[::-1]
bReversed = B[::-1]
#print(aReversed, bReversed)
firstNum = int(aReversed)
secondNum = int(bReversed)

if firstNum > secondNum:
    print(firstNum)
elif secondNum > firstNum:
    print(secondNum)
