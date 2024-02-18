# 25
# Написать функцию, которая создаст новый двумерный массив, «повернутый» относительно переданного на 90°.
from links import tTwo_infile, tTwo_outfile
from utils import columns, lines


def arrayreversal(array):
    ax1 = lines()
    ax2 = columns()
    outputFile = open(tTwo_outfile, 'w+')
    resultArray = list(map(list, zip(*array[::-1])))

    for i in range (ax2):
        if i > 0:
            outputFile.write('\n')
        for j in range (ax1):
            outputFile.write(str(resultArray[i][j]) + ' ')
    outputFile.close()


with open(tTwo_infile, 'r') as file:
    ax1 = lines()
    ax2 = columns()
    arr = file.readlines()
    for i in range(ax1):
        arr[i] = list(map(int, (arr[i].rstrip().split(' ')[:ax2])))
    arr = arr[:ax1]

arrayreversal(arr)
