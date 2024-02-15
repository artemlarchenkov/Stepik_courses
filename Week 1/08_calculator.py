#Напишите простой калькулятор, который считывает с пользовательского ввода 
#три строки: первое число, второе число и операцию, после чего применяет 
#операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

#Поддерживаемые операции: +, -, /, *, mod, pow, div, где
#mod — это взятие остатка от деления,
#pow — возведение в степень,
#div — целочисленное деление.

#Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

#Обратите внимание, что на вход программе приходят вещественные числа.

# put your python code here
first_number = float(input())
second_number = float(input())
operation = input()
if operation == "-":
    print (first_number - second_number)
if operation == "+":
    print (first_number + second_number)
if operation == "*":
    print (first_number * second_number)
if operation == "/":
    if second_number == 0:
        print ("Деление на 0!")
    else: 
        print(first_number / second_number)
if operation == "mod":
    if second_number == 0:
        print ("Деление на 0!")
    else: 
        print (first_number % second_number)
if operation == "div":
    if second_number == 0:
        print ("Деление на 0!")
    else:
        print (first_number // second_number)
if operation == "pow":
    print (first_number ** second_number)



