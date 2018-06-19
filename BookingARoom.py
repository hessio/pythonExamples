import random
r, n = input().split(" ")
N = int(n)
r = int(r)
roomsBooked = [0] * N
i = 0
j = 0
roomFreeFinal = 0
allRooms = [0] * r
for i in range(1, r + 1):
    allRooms[i - 1] = i
i = 0   
while i < N:
    roomsBooked[i] = int(input())
    i = i + 1
roomFree = random.randint(0, r) 
while (0 == 0):
    roomFree = random.randint(0, r)
    if (roomFree not in roomsBooked):
        roomFreeFinal = roomFree
        break
if len(roomsBooked) == len(allRooms):
    for i in range(1, r + 1):
        if allRooms[i - 1] in roomsBooked:
            j = j + 1
if len(roomsBooked) == r and j == len(roomsBooked):
    print("too late")
else:
    print(roomFreeFinal)
