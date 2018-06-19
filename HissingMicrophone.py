string = str(input())
flag = 0
for i in range(1, len(string)):
    if string[i] == 's' and string[i - 1] == 's':
        flag = 1
if flag == 1:
    print("hiss")
else:
    print("no hiss")
