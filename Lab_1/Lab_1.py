import numpy
import random
sum=0
sr=0
mas1=[]
mas2=[]
med=0
pr=1
#  Сумма от 0 до 88888888
for x in range(88888889):
    sum+=x
    mas1.append(x)
# Произвдение чисел
k=int(input('Введите сколько чисел вы хотите перемножить: '))
for x in range(k):
    ch=random.randint(0,1001)
    mas2.append(ch)
    pr*=ch
mas2.sort()
l=len(mas2)
if(l%2==0):
    med=(mas2[l//2]+mas2[(l//2)-1])/2
else:
    med=mas2[l//2]
sr=numpy.average(mas1)
print(l//2)
print("Сумма ряда 88888888:",sum)
print("Среднее ряда 88888888:",sr)
print("Случайные числа от 0 до 1000:",mas2)
print("Медиана случайных чисел:",med)
print("Произведение случайных чисел:",pr)
