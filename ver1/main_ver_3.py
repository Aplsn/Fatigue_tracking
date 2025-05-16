import time
from datetime import datetime as dt
import numpy as np
import random
import csv
import os

TASK_NUM = 100


def single_digits_add() -> list[dict[str, str | int]]:
    problems = []
    operation = 'sd_add'
    for _ in range(TASK_NUM):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        problems.append({
            "num1": f"{num1}",
            "num2": f"{num2}",
            "operation": operation,
            "right_ans": num1 + num2,
            "text": f"{num1} + {num2}?"
        })
    return problems


def single_digits_sub() -> list[dict[str, str | int]]:
    problems = []
    operation = 'sd_sub'
    for _ in range(TASK_NUM):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        num1, num2 = max(num1, num2), min(num1, num2)
        problems.append({
            "num1": f"{num1}",
            "num2": f"{num2}",
            "operation": operation,
            "right_ans": num1 - num2,
            "text": f"{num1} - {num2}?"
        })
    return problems


def single_digits_add_last() -> list[dict[str, str | int]]:
    problems = []
    operation = 'sd_last_add'
    for _ in range(TASK_NUM):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        problems.append({
            "num1": f"{num1}",
            "num2": f"{num2}",
            "operation": operation,
            "right_ans": (num1 + num2) % 10,
            "text": f"({num1} + {num2}) % 10?"
        })
    return problems


def single_digits_sub_abs() -> list[dict[str, str | int]]:
    problems = []
    operation = 'sd_abs_sub'
    for _ in range(TASK_NUM):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        problems.append({
            "num1": f"{num1}",
            "num2": f"{num2}",
            "operation": operation,
            "right_ans": abs(num1 - num2),
            "text": f"|{num1} - {num2}|?"
        })
    return problems


def single_digits_mul() -> list[dict[str, str | int]]:
    problems = []
    operation = 'sd_mul'
    for _ in range(TASK_NUM):
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        problems.append({
            "num1": f"{num1}",
            "num2": f"{num2}",
            "operation": operation,
            "right_ans": num1 * num2,
            "text": f"{num1} * {num2}?"
        })
    return problems


def double_didgits_add() -> list[dict[str, str | int]]:
    problems = []
    operation = 'dd_add'
    for _ in range(TASK_NUM):
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        problems.append({
            "num1": f"{num1}",
            "num2": f"{num2}",
            "operation": operation,
            "right_ans": num1 + num2,
            "text": f"{num1} + {num2}?"
        })
    return problems


def double_didgits_sub() -> list[dict[str, str | int]]:
    problems = []
    operation = 'dd_sub'
    for _ in range(TASK_NUM):
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        num1, num2 = max(num1, num2), min(num1, num2)
        problems.append({
            "num1": f"{num1}",
            "num2": f"{num2}",
            "operation": operation,
            "right_ans": num1 - num2,
            "text": f"{num1} - {num2}?"
        })
    return problems


def mix_mul() -> list[dict[str, str | int]]:
    problems = []
    operation = 'mix_mul'
    for _ in range(TASK_NUM):
        num1 = random.randint(10, 99)
        num2 = random.randint(2, 9)
        problems.append({
            "num1": f"{num1}",
            "num2": f"{num2}",
            "operation": operation,
            "right_ans": num1 * num2,
            "text": f"{num1} * {num2}?"
        })
    return problems


def mix_div() -> list[dict[str, str | float]]:
    problems = []
    operation = 'mix_div'
    for _ in range(TASK_NUM):
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        num1, num2 = num1 * num2, num1
        problems.append({
            "num1": f"{num1}",
            "num2": f"{num2}",
            "operation": operation,
            "right_ans": num1 / num2,
            "text": f"{num1} / {num2}?"
        })
    return problems


def mix_mod() -> list[dict[str, str | int]]:
    problems = []
    operation = 'mix_mod'
    for _ in range(TASK_NUM):
        num1 = random.randint(10, 90)
        num2 = random.randint(2, 9)
        problems.append({
            "num1": f"{num1}",
            "num2": f"{num2}",
            "operation": operation,
            "right_ans": num1 % num2,
            "text": f"{num1} mod {num2}?"
        })
    return problems


def wait_answer():
    num = input()
    while (not num.isdigit()) or len(num) > 1:
        num = input("\033[1m !!!Ответ в виде одной цифры!!! \033[0m \n")
    return int(num)


def main():
    time_limit = 60 * 7.0
    level_funcs = [
        single_digits_add_last,
        single_digits_sub_abs,
        # single_digits_mul,
        # double_didgits_add,
        # double_didgits_sub,
        # mix_mul,
        # mix_div,
        # mix_mod
    ]
    problem_pool = []
    for func in level_funcs:
        problem_pool.extend(func())
    problem_pool = np.random.permutation(problem_pool)
    print("""Инструкция\n* При сложении(+) чисел вводите последнюю цифру ответа
* При вычитании(-) вводите ответ по модулю
    \033[1m !!!Ответ всегда одна цифра!!! \033[0m""")
    print('Пройдите тест как можно быстрее')
    username = input("Введите ваше имя: ")
    directory_name = 'answers'
    consent = input("Правила понятны, готов(-а) начать! Напечайтате ответ: Да/Нет\n")
    while consent.lower() != 'да':
        if consent.lower() == 'нет':
            return
        consent = input("Ошибка ввода. Напечайтате ответ: Да/Нет\n")

    if not os.path.exists(directory_name):
        os.mkdir(directory_name)

    t0 = dt.now()
    filename = directory_name + '/' + username + '_' + t0.strftime("%Y-%m-%d_%H-%M-%S") + '_' \
               + 'new_ver.csv'
    counter = 0

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        field = [
            '#',
            'num1',
            'num2',
            'operation',
            'right_ans',
            'user_ans',
            'start_time',
            'end_time',
            'correct_flg']
        writer.writerow(field)
        file.close()

    for i in range(len(problem_pool)):
        start_time = time.monotonic()
        cur_problem = problem_pool[i]
        num1, num2 = cur_problem['num1'], cur_problem['num2']
        print(cur_problem['text'])
        answer = wait_answer()
        end_time = time.monotonic()

        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            field = [
                counter,
                f"{num1}",
                f"{num2}",
                cur_problem['operation'],
                cur_problem['right_ans'],
                answer,
                start_time,
                end_time,
                int(cur_problem['right_ans'] == answer)
            ]
            writer.writerow(field)
            file.close()

        counter += 1


if __name__ == "__main__":
    main()
