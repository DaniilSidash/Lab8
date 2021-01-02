#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Решить индивидуальное задание лабораторной работы 6, оформив каждую команду в виде
#отдельной функции

# Использовать словарь, содержащий следующие ключи: название пункта назначения рейса;
# номер рейса; тип самолета. Написать программу, выполняющую следующие действия: ввод
# с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть размещены в алфавитном порядке по названиям пунктов назначения; вывод на экран
# пунктов назначения и номеров рейсов, обслуживаемых самолетом, тип которого введен с
# клавиатуры; если таких рейсов нет, выдать на дисплей соответствующее сообщение

import sys


def add(airplanes,name, type, num):
    airplane = {
        'name': name,
        'type': type,
        'num': num,
    }

    airplanes.append(airplane)
    if len(airplanes) > 1:
        airplanes.sort(key=lambda item: item.get('type', ''))


def list(airplanes):
    table = []
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    table.append(line)
    table.append(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "№",
            "Пункт назначения рейса",
            "Тип самолета",
            "Номер рейса"
        )
    )
    table.append(line)

    for idx, airplane in enumerate(airplanes, 1):
        table.append(
            '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                idx,
               airplane.get('name', ''),
               airplane.get('type', ''),
               airplane.get('num', 0)
            )
        )

    table.append(line)

    return '\n'.join(table)


def select(airplane, period):

    result = []
    for airplane in airplanes:
        if period == airplane.get('name'):
            result.append(airplane)

    return result


if __name__ == '__main__':
    airplanes = []

    while True:
        command = input(">>> ")

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Пункт назначения рейса ")
            type = input("Тип самолета ")
            num = input("Номер рейса")

            add(airplanes, name, type, num)

        elif command == 'list':
            print(list(airplanes))

        elif command.startswith('select '):
            parts = command.split(maxsplit=1)
            selected = select(airplanes, parts[1])
            count = 0
            if selected:
                for idx, airplane in enumerate(selected, 1):
                    print(
                        '{:>4}: {}, Тип самолета - {}, Номер рейса - {}'.format(count, airplane.get('name', ''),
                                                                                       airplane.get('type', ''),
                                                                                       airplane.get('num', ''))
                    )
            else:
                print("Рейс с таким названием не найден.")

        elif command == 'help':
            print("Список команд:\n")
            print("add - Добавить рейс;")
            print("list - Вывести список рейсов;")
            print("select <Рейс> - Вывести всю информацию  о рейсе;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)