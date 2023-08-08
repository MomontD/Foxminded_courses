import os

import sys

from dataclasses import dataclass

from datetime import datetime, timedelta

import argparse


# Створюємо модель класу для кожного racer
@dataclass
class RacerData:

    nik_name: str = None
    name: str = None
    team: str = None
    start_time = None
    end_time = None

    # Property класу для визначення та роботи з result_time
    @property
    def result_time(self):

        if self.end_time is not None and self.start_time is not None:

            result_time = self.end_time - self.start_time

            if result_time > timedelta(minutes=5) or result_time < timedelta(days=0):
                return None
            else:
                return result_time

    # Створюємо ще одну динамічну змінну result_time_str яка буде містити result_time типу str
    @property
    def result_time_str(self):
        if self.result_time is not None:
            return str(self.result_time)
        else:
            return "You have incorrect data in log files.Difference can't be more 1 day or 5 min"


# Ф-я для читання аргументів
def cli_parser():
    parser = argparse.ArgumentParser(description='Python CLI для звіту про водіїв.')
    parser.add_argument('--folder', help='Шлях до папки з файлами водіїв.')
    parser.add_argument('--asc', help='Сортувати список водіїв за зростанням (за замовчуванням).')
    parser.add_argument('--desc', help='Сортувати список водіїв за спаданням.')
    parser.add_argument('--driver', help='Ім\'я водія для отримання статистики.')

    return parser.parse_args()


# Ф-я читання файлу, добавлено кодування utf-8 для таких імен як 'Kimi Räikkönen'
def read_file(file_name, folder):

    file_path = os.path.join(folder, file_name)

    try:
        with open(file_path, "r", encoding='utf-8') as file:
            content = file.read().splitlines()

    except FileNotFoundError:
        raise ValueError('Error: File missing or not found!')

    except OSError:
        raise ValueError("Can't read the file")

    except Exception as error:
        raise ValueError(f"Unexpected error: {error}")

    return content


def build_report(folder):

    # Зчитуємо дані з log файлів
    abbreviations = read_file("abbreviations.txt", folder)
    start_log = read_file("start.log", folder)
    end_log = read_file("end.log", folder)

    # Словник водіїв, format => dict = {'nik_name': RacerData}
    racers_dict = {}

    # Ф-я перетворення string_time у формат часу (для арифметичних операцій)
    def get_time(str_time):

        return datetime.strptime(str_time.strip(), '%H:%M:%S.%f').time()

    # Ф-я перетворення string_date у формат часу (для арифметичних операцій)
    def get_date(str_date):

        return datetime.strptime(str_date[3:].strip(), '%Y-%m-%d').date()

    '''
    Створюємо профіль racer, заповнюємо даними (nik_name, name, team) з файлу розшифровки 
    та додаємо в словник racers_dict 
    Надалі звірка даних з інших файлів буде проводитись на основі цих даних.
    '''
    for element in abbreviations:
        nik_name, name, team = element.split('_')
        racer = RacerData(nik_name=nik_name, name=name, team=team)
        racers_dict[nik_name] = racer

    # Заповнюємо профіль racer даними з start_log
    for element in start_log:
        nik_name = element[:3]
        date, start_time = element.split('_')
        racers_dict[nik_name].start_time = datetime.combine(get_date(date), get_time(start_time))

    # Заповнюємо профіль racer даними з end_log
    for element in end_log:
        nik_name = element[:3]
        date, end_time = element.split('_')
        racers_dict[nik_name].end_time = datetime.combine(get_date(date), get_time(end_time))

    '''
    Обраховуємо за допомого ф-ї calculate_result_time результуючий час (час за який гонщик проїхав коло).
    + Проводимо перевірку на валідність отриманого часу :
        Якщо час більше 5 хв. або мінусовий або більше 1 дня або мінусивий записуємо в профіль
        відповідне повідомлення  з помилкою.
    '''

    return racers_dict


# Ф-я виводу report
def print_report(racers_dict, desc=False):

    # Перетворюємо dict в list => dict{'nik_name' : RacerData} => list[RacerData]
    list_racers = list(racers_dict.values())
    # 1. Сортуємо список
    list_racers = sorted(list_racers, key=lambda person: person.result_time if isinstance(
        person.result_time, timedelta) else timedelta.max, reverse=desc)

    # 2. Виводимо список
    for index, racer in enumerate(list_racers):

        if racer.result_time_str is not None:
            if index == 15:
                print('-' * 66)
            print("{:<20} {:<30} {:>10}".format(racer.name, racer.team, racer.result_time_str))

    return list_racers


# Пошук статистичних даних racer за вказаним аргументом (імя racer)
def driver_statistics(racers_dict, driver):

    current_driver = None

    list_racers = list(racers_dict.items())

    for racer in list_racers:

        if racer.name == driver:

            current_driver = "{:<20} {:<30} {:>10}".format(racer.name, racer.team, racer.result_time)

    if current_driver:
        print(current_driver)
    else:
        print('Can\'t find driver : ', driver)


def main(folder='logs', desc=False, driver=False):

    racers_data = build_report(folder)

    if driver:

        driver_statistics(racers_data, driver)

    else:

        print_report(racers_data, desc)


if __name__ == '__main__':

    args = cli_parser()

    '''
    Перевірка аргументів командного рядка
    
    1. Якщо вказана тільки папка з log файлами і невказані аргументи - обробляємо файли в папці і виводимо 
       відсоротовану статистику по asc
    2. Якщо вказана папка з log файлами і аргумент asc - обробляємо файли в папці і виводимо 
       відсоротовану статистику по asc
    '''
    if (args.folder and args.asc) or (args.folder and not args.asc and not args.desc and not args.driver):

        main(args.folder)

    # Якщо в аргументах вказано folder та desc - обробляємо файли в папці і виводимо відсоротовану статистику по desc
    if args.folder and args.desc:

        option_desc = True
        main(args.folder, option_desc)

    # Якщо в аргументах вказано folder та driver - обробляємо файли в папці s виводимо статистику по driver
    if args.folder and args.driver:

        option_desc = False
        main(args.folder, option_desc, args.driver)

    # Якщо ніяких аргументів не вказано оброляємо по замовчуванню папку log та виводимо відсоротовану статистику по asc
    if len(sys.argv) == 1:
        main()
