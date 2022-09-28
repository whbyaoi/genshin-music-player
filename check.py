import os

from MyMap import DIGIT_TO_KEY

fileName = 'canon.txt'
curDir = os.getcwd()
fileDir = curDir + '/sheets/{}'.format(fileName)
file = open(fileDir, 'r', encoding='utf8')
while line := file.readline():
    if line != '\n':
        sum = 0
        times = []
        stack = ''
        for op in line:
            if op == '=':
                if stack == '':
                    stack += '='
                elif stack[0] == '=':
                    sum += float(stack[1:])
                    times.append(float(stack[1:]))
                    stack = ''
            elif op in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
                if stack == '':
                    pass
                elif stack[0] in ['(', '=']:
                    stack += op
            else:
                pass
        if int(sum) != 4:
            print(sum, times, line)