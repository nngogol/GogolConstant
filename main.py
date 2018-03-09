# 1+(               ):2+(               )
# 1+(3+(   ):4+(   )):2+(5+(   ):6+(   ))

import re

nextNum = 3
template = '(1+())/(2+())'

def getBrIndexes(pattern):

    return [m.start() for m in re.finditer('\(\)', pattern)]

def worker():
    global nextNum
    global template
   
    pairs = []
    for br in getBrIndexes(template):
        new_part = f'(({nextNum}+())/({nextNum+1}+()))'
        nextNum+=2

        pairs.append( (br, new_part) )

    for index, pattern in reversed(pairs):
        template = template[:index] + pattern + template[index+2:]


# basic test
# worker()
# template = template.replace('()', '0')
# print(template)
# print(eval(template))

def main():
    for level in range(1,10):

        global nextNum
        global template

        # clear and setup
        nextNum = 3
        template = '(1+())/(2+())'

        # inserting...
        for _ in range(level):
            worker()
        
        # finish
        template = template.replace('()', '0')

        # output
        print('--------')
        print(f'level = {  level}')
        print(f'len = {    len(template)}')
        print(f'result = { str(eval(template))}')

if __name__ == '__main__':
    main()
