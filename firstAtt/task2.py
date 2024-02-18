# 25
# Написать функцию, которая создаст новый двумерный массив, «повернутый» относительно переданного на 90°.
from links import tTwo_infile, tTwo_outfile


def arrayreversal(array):
    outputFile = open(tTwo_outfile, 'w+')
    outputFile.close()


def getarraysize_lines():
    with open(tTwo_infile) as file:
        line = sum(1 for line in file)
    return line


def getarraysize_columns():
    with open(tTwo_infile) as file:
        for line in file:
            column = ([int(x) for x in line.split()])
            break
    return len(column)


arr = [[0] * getarraysize_columns()] * getarraysize_lines()

arrayreversal(arr)
