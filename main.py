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
    x[-3]=x[-2][:2]
    pure_guys.append(x)

num_gr=math.ceil(len(pure_guys)/5)
newpure_guys=[]
for i in range(len(pure_guys)):
    smth = random.randint(0,len(pure_guys)-1)
    newpure_guys.append(pure_guys[smth])
    del pure_guys[smth]

pure_guys=newpure_guys
num=0
k=0
for x in pure_guys:
    if k==5:
        num+=1
        k=0
    if k<5 and num<num_gr:
        x[-2] = num+1
        k += 1

puretable=PrettyTable()
puretable.field_names = ['Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Специальность', 'Группа', 'Средний балл']
puretable.add_rows(pure_guys)
a=0
b=5
m=20
for i in range(num_gr):
    print(f'Date:{m}.05.2021')
    print(puretable[a:b])
    a+=5
    b+=5
    m+=1
