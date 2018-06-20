import sys
import operator
ops = ['+', '-']
def main():
    dict_vars = {}
    ans_string=''
    user_input_str = ''
    for line in sys.stdin:
        if len(line) == 0:
            continue
        keyword = str(line.split(' ')[0]).replace('\n', '')
        args = line.split(' ')[1:]
        if keyword == 'def':
            dict_vars[str(args[0])] = int(str(args[1]).replace('\n',''))
        elif keyword == 'clear':
            dict_vars.clear()
        elif keyword == 'calc':
            user_input = line.replace('\n', '').split(' ')
            user_input.remove('=')
            user_input.remove('calc')
            for item in user_input:
                if item in dict_vars:
                    user_input_str += str(dict_vars[item]) + ' '
                else:
                    user_input_str += item + ' '
            set_unknown = False
            for value in user_input:
                ans_string += value + ' '
                if value not in dict_vars and value != '+' and value != '-':
                    set_unknown = True
            check_all_values_present = False
            for item in user_input:
                if item not in dict_vars and item != '-' and item != '+':
                    check_all_values_present = True
            if not set_unknown:
                answer = eval(user_input_str)
                if answer in dict_vars.values():
                    for key,val in dict_vars.items():
                        if val == answer:
                            ans_string += '= ' + key
                else:
                    ans_string += '= unknown'
            else:
                ans_string += '= unknown'
            
            print(ans_string)
            user_input = ''
            answer = 0
            ans_string=''
            user_input_str = ''
            set_unknown = False
    return

if __name__ == '__main__':
    main()
