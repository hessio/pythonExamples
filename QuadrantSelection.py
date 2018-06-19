x = int(input())
y = int(input())

if x < 0 and y < 0:
    print(3)
if x > 0 and y < 0:
    print(4)
if y > 0 and x < 0:
    print(2)
if y > 0 and x > 0:
    print(1)
