""" Практическое задание по 1 уроку курса "Основы языка Python"""

# Блок выполняет расчёт прибыли на одного сотрудника в фирме

print("Введите значение выручки")
proceed = float(input() ) # Ввод пользователем значения выручки
print("Введите значение издержек фирмы")
costs = input()  # Ввод пользователем значения издержек
fin_result = float(proceed) - float(costs)  # Вычисление финансового результата фирмы
if fin_result > 0:
    print(('Прибыль составляет ', fin_result), 'рентабельность ', format(fin_result / proceed, '.2f'))
    print("Введите количесвто сотрудников")
    num_workers = int(input())  # Ввод количества сотрудников фирмы
    profit_worker = fin_result / num_workers
    print('Прибыль фирмы в расчете на  сотрудника составляет', format(profit_worker, '.2f'))
else:
    print('Убыток составляет', fin_result)