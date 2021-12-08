from prettytable import PrettyTable

mytable = PrettyTable()
mytable.field_names = ['Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Балл при поступлении', 'Курс', 'Группа',
                       'Средний балл']
aim = []
ism = []

aif = open('AI_students.txt', 'r')
isf = open('IS_students.txt', 'r')

lines0 = aif.read()
lines1 = isf.read()

lines0 = lines0.split('\n')
for x in lines0:
    aim.append(x.split())

lines1 = lines1.split('\n')
for x in lines1:
    ism.append(x.split())

students = aim + ism


def sortbySurname(inputStr):
    return inputStr[0]


def sortbySpecialn(inputStr):
    return inputStr[-2]


students.sort(key=sortbySurname)
students.sort(key=sortbySpecialn)

mytable.add_rows(students)
#print(mytable)
import random
import math
pure_guys=[]
for x in students:
  if x[-3]=='5':
    del x[4]
    x[-3]=x[-2]
    pure_guys.append(x)
num_gr=math.ceil(len(pure_guys)/5)
num=0
k=0
for x in pure_guys:
    if k==5 and num<num_gr:
        k=0
        num+=1
    if k<5:
        x[-2] = i


"""for x in pure_guys:
    k = 0
    for i in range (num_gr):
        while k<4:
            x[-2]=i
            k+=1
"""
print(pure_guys)
puretable=PrettyTable()
puretable.field_names = ['Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Специальность', 'Группа', 'Средний балл']
