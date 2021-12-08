from prettytable import PrettyTable
mytable = PrettyTable()
mytable.field_names = ['Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Балл при поступлении', 'Курс', 'Группа', 'Средний балл']
aim=[]
ism=[]

aif=open('AI_students.txt','r')
isf=open('IS_students.txt','r')

lines0=aif.read()
lines1=isf.read()

lines0=lines0.split('\n')
for x in lines0:
  aim.append(x.split())

lines1=lines1.split('\n')
for x in lines1:
  ism.append(x.split())

students=aim+ism
def sortbySurname(inputStr):
  return inputStr[0]
def sortbySpecialn(inputStr):
  return inputStr[-2]

students.sort(key = sortbySurname)
students.sort(key = sortbySpecialn)

mytable.add_rows(students)
print(mytable)