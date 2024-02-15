# Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
#
# На ввод могут подаваться и повторяющиеся числа.

# Sample Input 1:
#
# 8
# 2
# 14
# Sample Output 1:
#
# 14
# 2
# 8
# Sample Input 2:
#
# 23
# 23
# 21
# Sample Output 2:
#
# 23
# 21
# 23

# put your python code here
a = int(input())
b = int(input())
c = int(input())

max = a

if b <= max and c <= max:
    if b <= c:
        print(max,'\n', b, '\n', c)
    else:
        print(max,'\n', c, '\n', b)
else:
    max = b
    if a <= max and c <= max:
        if a <= c:
            print(max,'\n', a, '\n', c)
        else:
            print(max,'\n', c, '\n', a)
    else:
        max = c
        if a <= max and b <= max:
            if a <= b:
                print(max,'\n', a, '\n', b)
            else:
                print(max,'\n', b, '\n', a)