from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.BLACK)
print(Back.GREEN)
what = input(("Что делаем?( +, -, *, /): "))
if what == "+" or what == "-" or what == "*" or what == "/":
    print(Back.YELLOW)
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(Back.CYAN)
    if what == "+":
        c = a + b 
        print("Результат: " + str(c))
    elif what == "-":
        c = a - b 
        print("Результат: " + str(c))
    elif what == "*":
        c = a * b 
        print("Результат: " + str(c))
    elif what == "/":
        c = a / b 
        print("Результат: " + str(c))
    
else:
    print(Back.RED)
    print("Некорректный ввод")
input()