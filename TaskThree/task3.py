#Задан набор студентов в виде (ФИО, пол, номер курса, средний балл).
#Необходимо на новогодний бал отправить лучших студентов – по одной паре (парень и девушка) с каждого курса
#с лучшей успеваемостью. Если есть несколько студентов с максимальной успеваемостью – выбрать случайным образом
#(именно случайным, т.е. при следующем выборе вполне возможно отобраны будут другие студенты).
#Если какой-то курс полностью состоит из представителей одного пола, то с такого курса на балл никого не отправлять.
from utils import *
from links import *


def couplesercher(arr,l,c):
    out = open(tThree_outfile,'w+')
    bestStudent = []
    for i in range(4):
        bestStudent.append(getBestStudent(arr,'М',str(i+1),l))
        bestStudent.append(getBestStudent(arr,'Ж',str(i+1),l))

    for i in range(len(bestStudent)):
        if(i==0): out.write('1st year couple:'+'\n')
        if(i==2): out.write('2nd year couple:'+'\n')
        if(i==4): out.write('3rd year couple:'+'\n')
        if(i==6): out.write('4th year couple:'+'\n')
        for j in range(3):
            if(bestStudent[i][0]=='None'):
                out.write('Coupe is not found')
                break
            else:
                out.write(str(bestStudent[i][j]+' '))
                if(j==2):
                    out.write('('+bestStudent[i][4]+' '+bestStudent[i][5]+')\n')
    out.close()

with open(tThree_infile_1, 'r') as file:
    l = lines()
    c = columns()
    arr = file.readlines()
    for i in range(l):
        arr[i] = list(map(str, (arr[i].rstrip().split(' ')[:c])))
    arr = arr[:l]

couplesercher(arr,l,c)