# Baza
# code = '404 not found'
# string = 'some error    message'
# num1 = 1
# randomBool = False
# print(code)
# print('код ответа: ' + code)
# print('если вы видите это сообщение, то страница не найдена ' + code)
################################################################

#Списки lists
# numbers =[10, 20, 30, 40, 50]
# print(numbers[0]) # напечатает 10
# print(numbers[4]) # напечаетет 50
# print(numbers[-1])# напечатает 50
# print(numbers[8]) # будет ошибка
# weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
#totalDays = len(weekdays)  # считаем дни недели в списке (сколько элементов в списке)
#print(totalDays)
#monday = weekdays[1] # выбираем день из списка викдэйс
#print(monday)
################################################################

# Функции
# def sumNumbers(num_1, num_2):               #обьявление функции
#     print('slagaemoe 1  =', num_1)
#     print('slagaemoe 2  =', num_2)
#     result = num_1 + num_2
#     print('summa = ', result)
#     return result
# x = sumNumbers(5,6) # вызов функции
# # print(x)
# def multiply(x,y): #умножение
#     return x*y
# m = multiply(7,9)
# print(m)
#
# def divide (a,b): #деление
#     return a/b
# d = divide(0.15,9)
# print(d)
#
# def sub (q, w): #вычитание
#     return q-w
# s = sub(12,19)
# print(s)
############################################

#Области видимости переменной. Переменные видны или глобально или внутри функции
# globalVar = 1
#
# def printGlobal():
#     print(globalVar)
#
# def printLocal():
#     local = 2
#     print(local)
#
#
# printGlobal()
# printLocal()
###############################################################

#Стек вызовов

# def funcA():
#     print('начали выполнять А')
#     funcB()
#     print('закончили выполянять А')
#
# def funcB():
#     print('начали выполнять B')
#     funcC()
#     print('закончили выполянять B')
#
# def funcC():
#     print('начали выполнять C')
#     funcD()
#     print('закончили выполянять C')
# def funcD():
#     print('начали выполнять D')
#     print('закончили выполянять D')
# funcA()

# def endless(): # рекурсия или стэкоферфлоу. бесконечное выопление функиции без условия выхода
#     print('endless')
#     endless()
#
# endless()





