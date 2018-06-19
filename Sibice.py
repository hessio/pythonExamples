N,W,H = input().split(" ")
w = int(W)
h = int(H)
number = int(N)
responses = [0] * number 
for j in range(0, number):
    responses[j] = (int(input()))

for i in range(0,number):
    lenght = responses[i]
    if lenght*lenght <= w*w + h*h: 
        print("DA")
    else:
        print("NE")
