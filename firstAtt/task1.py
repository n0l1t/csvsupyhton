# 25
# Реализовать функцию:
# которая создаст новый список элементов из элементов первого списка,
# каждый из которых повторяется такое кол-во раз, которое данный элемент встречается во втором списке, например:
# ({ 5, 3, 1, 2, 3, 3, 7, 4, 8 }, { 5, 3, 7, 3, 7, 2, 2, 8, 7 }) → { 5, 3, 3, 2, 2, 3, 3, 3, 3, 7, 7, 7, 8 }

def listcreator(firstList, secondList):
    outputFile = open('firstAtt/results/outputTask1', 'w+')
    i = 0
    j = 0
    while i < len(firstList):
        while j < len(secondList):
            if (firstList[i] == secondList[j]):
                outputFile.write(str(secondList[j]))
            j += 1
        i += 1
        j = 0
    outputFile.close


fList = []
sList = []

with open('firstAtt/input/inputTask1') as file:
    for line in file:
        for x in line.split():
            fList.append(int(x))
        break
    for line in file:
        for x in line.split():
            sList.append(int(x))
        break

listcreator(firstList=fList, secondList=sList)
