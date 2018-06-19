n = str(input())
r = int((len(n)))
upperString = [0] * r
k = 0
i = 0
g = int(len(n))
while i < g:
    ch = n[i]
    if ch.isupper():
        upperString[k] = ch
        k = k + 1
    i = i + 1
for j in range(0, len(upperString)):
    if 0 in upperString:
        upperString.remove(0)
answerString = ''.join(upperString)
print(answerString)
