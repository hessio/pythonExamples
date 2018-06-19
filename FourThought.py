operators = ['+', '-', '*', '//']

values = {}

for a in operators:
    for b in operators:
        for c in operators:
            value_string = '4{:s}4{:s}4{:s}4'.format(a,b,c)
            val = eval(value_string)
            values[val] = value_string.replace('//', '/') + ' = {:d}'.format(val)

for i in range(0, int(input())):
    user = int(input())
    if user < -60 or user > 256 or user not in values:
        print('no solution')
    else:
        print(values[user])
