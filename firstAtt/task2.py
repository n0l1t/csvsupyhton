# 25
# Написать функцию, которая создаст новый двумерный массив, «повернутый» относительно переданного на 90°.

def arrayreversal(array):
    outputFile = open('/Users/n0rthl1ght/Desktop/вгу/pyhton/firstAtt/results/outputTask2', 'w+')
    outputFile.close()


def getarraysize_lines():
    with open('/Users/n0rthl1ght/Desktop/вгу/pyhton/firstAtt/input/inputTask2') as file:
        line = sum(1 for line in file)
    return line


def getarraysize_columns():
    with open('/Users/n0rthl1ght/Desktop/вгу/pyhton/firstAtt/input/inputTask2') as file:
        for line in file:
            column = ([int(x) for x in line.split()])
            break
    return len(column)


arr = [[0] * getarraysize_columns()] * getarraysize_lines()

arrayreversal(arr)
