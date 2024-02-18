# 25
# Написать функцию, которая создаст новый двумерный массив, «повернутый» относительно переданного на 90°.
from links import tTwo_infile, tTwo_outfile
from getarraysize import columns, lines


def arrayreversal(array):
    outputFile = open(tTwo_outfile, 'w+')
    outputFile.close()


arr = [[0] * columns()] * lines()

print(arr)

arrayreversal(arr)
