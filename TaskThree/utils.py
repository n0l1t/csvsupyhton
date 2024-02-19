from random import randint

from links import *

def lines():
    with open(tThree_infile_1) as file:
        line = sum(1 for line in file)
    return line


def columns():
    with open(tThree_infile_1) as file:
        for line in file:
            column = ([str(x) for x in line.split()])
            break
    return len(column)


def getBestStudent(arr,sex,year):
    l=lines()
    student=[]
    studentWithSameGrade=[]
    temp = 0.0
    for i in range(l):
        if(arr[i][3] == sex and arr[i][4]==year):
            student.append(arr[i])
    if(student==[]):
        return 'None'
    else:
        for i in range(len(student)):
            if(float(student[i][5])>temp):
                temp=float(student[i][5])
                bestStudent = student[i]
            elif (float(student[i][5])==temp):
                studentWithSameGrade.append(student[i])
    if(len(studentWithSameGrade)>1):
        return studentWithSameGrade[randint(0,len(studentWithSameGrade))-1]
    else:
        return bestStudent


