import operator

m=int(input())
ops = { "+": operator.add, "-": operator.sub, "/": operator.floordiv, "*": operator.mul }
dict_of_symbs = {0: '+', 1: '-', 2: '/', 3: '*'}
list_of_inputs = []
for i in range(0, m):
    list_of_inputs.append(int(input()))

summed = 0
def find_the_correct_symbols(number_input):
    summed = 0
    first = 0
    second = 0
    third = 0
    second_count = 0
    first_count = 0
    for i in range(1, 65):
        summed = 0
        summed = int(eval('4 ' + str(dict_of_symbs[first]) + ' 4 ' + str( dict_of_symbs[second]) + ' 4 ' + str(dict_of_symbs[third]) + ' 4'))
        #print(summed)
        if summed == number_input:
            return '4 ' + str(dict_of_symbs[first]) + ' 4 ' + str(dict_of_symbs[second]) + ' 4 ' + str(dict_of_symbs[third]) + ' 4 = ' + str(int(summed))
        third=(third+1)%4
        first_count += 1
        second_count += 1
        if second_count % 4 == 0:
            second = (second+1)%4
            second_count = 0
        if first_count % 16 == 0:
            first += 1
            first_count = 0
    return 'no solution'

if __name__ == '__main__':
    for i in list_of_inputs:
        print(find_the_correct_symbols(i)) 
