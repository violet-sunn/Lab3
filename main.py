from prettytable import PrettyTable

#TASK 1
def sortbySurname(inputStr):
    return inputStr[0]


def sortbySpecialn(inputStr):
    return inputStr[-2]

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

students.sort(key=sortbySurname)
students.sort(key=sortbySpecialn)

mytable.add_rows(students)
print(mytable)

#TASK 2
import random
import math

mytable = PrettyTable()
mytable.field_names = ['Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Балл при поступлении', 'Курс', 'Группа',
                       'Средний балл']
aim = []
ism = []

with open('AI_students.txt', 'r') as aif:
  lines0=aif.read()
with open('IS_students.txt', 'r') as isf:
  lines1 = isf.read()

lines0 = lines0.split('\n')
for x in lines0:
    aim.append(x.split())

lines1 = lines1.split('\n')
for x in lines1:
    ism.append(x.split())

students = aim + ism

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

print('Пример: 1/1/2008')
startVKR=input('Введите дату начала защиты ВКР: ')
endVKR=input('Введите дату конца защиты ВКР: ')

if pure_guys==[]:
  print('Студентов 5-го курса в списках нет')
  exit()

import time
def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y', prop)

a=0
b=5
for i in range(num_gr):
    print(f'Дата защиты ВКР:\n{random_date(startVKR, endVKR, random.random())}')
    print(puretable[a:b])
    a+=5
    b+=5