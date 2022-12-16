"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.
Ввод: значение типа <str>
Вывод: значение числового типа данных
"""
import re
 
 
actions = {
  "^": lambda x, y: str(float(x)**float(y)),
  "*": lambda x, y: str(float(x) * float(y)),
  "/": lambda x, y: str(float(x) / float(y)),
  "+": lambda x, y: str(float(x) + float(y)),
  "-": lambda x, y: str(float(x) - float(y))
}
 
priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
 
 
def my_eval(expresion: str) -> str:
 
    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))
 
    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))
 
    return expresion
 
 
exp = "(1 + 4) * (5 * (10 - 2)) / 5"

# И сравним с eval()

print(my_eval(exp), eval(exp))
