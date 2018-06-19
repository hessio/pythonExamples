N = int(input())
q = [0] * N
for i in range(0, N):
    q[i] = int(input())
for j in range(0, N):
    if q[j] % 2 == 0:
        print(q[j], "is even")
    elif q[j] % 2 != 0:
        print(q[j], "is odd")
