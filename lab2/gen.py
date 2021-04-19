import csv
from faker import Faker
from collections import Counter


def datagenerate(records):
    """ Генерация данных сотрудников"""

    headers = ["Full Name", "Position", "Subdivision", "Quarterly valuation", "Salary"]

    subdivision_list = [
        "Канцелярия",
        "Сектор документации",
        "Архив",
        "Экспедиция",
        "Бухгалтерия",
        "Сектор расчетов с персоналом",
        "Сектор материального учета",
        "Сектор налогообложения",
        "Сектор реализации",
        "Юридический отдел",
        "Сектор договорной работы",
        "Сектор претензионной работы",
        "Отдел управления персоналом",
        "Сектор найма и учета персонала",
        "Отдел технического контроля",
        "Сектор входного контроля",
        "Сектор контроля изготовления",
        "Отдел снабжения",
        "Сектор закупок по РФ",
        "Сектор зарубежных закупок",
        "Отдел продаж",
        "Отдел рекламы ",
        "Отдел логистики",
        "Сектор грузоперевозок",
        "Сектор таможенного оформления",
        "Сектор транспортно-складских",
        "Склад № 1 (сбыта)",
        "Склад № 2 (импортных комплектующих)",
        "Склад № 3 (полуфабрикатов)",
        "Склад № 4 (ответственного хранения)",
        "Транспортный отдел",
        "Сектор внутренних перевозок",
        "Сектор внешних перевозок",
        "Сектор аренды автотранспорта ",
        "Отдел главного конструктора",
        "Отдел главного технолога",
        "Отдел компьютерного обеспечения",
        "Цех № 1",
        "Участок № 1",
        "Участок № 2",
        "Цех № 2",
        "Участок № 1",
        "Участок № 2",
        "Цех № 3",
        "Участок № 3",
        "Участок № 3 ",
        "Отдел главного механика",
        "Отдел главного энергетика",
        "Цех № 4 (ремонтный)",
        "Участок № 1",
        "Участок № 2",
        "Хозяйственный отдел"]

    position_list = [
        "Директор",
        "Заведующая",
        "Заместитель директора",
        "Мастер участка",
        "Менеджер",
        "Начальник",
        "Управляющий отделением",
        "Администратор",
        "Аналитик",
        "Аудитор",
        "Аукционист",
        "Бухгалтер",
        "Бухгалтер - ревизор",
        "Диспетчер",
        "Документовед",
        "Инженер",
        "Инспектор",
        "Консультант",
        "Лаборант",
        "Математик",
        "Переводчик",
        "Профконсультант",
        "Психолог",
        "Социолог",
        "Техник",
        "Физиолог",
        "Художник",
        "Экономист",
        "Юрисконсульт"]

    fake = Faker('ru_RU')
    with open("data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for row in range(records):
            writer.writerow({
                "Full Name": fake.name(),
                "Position": fake.random_element(elements=position_list),
                "Subdivision": fake.random_element(elements=subdivision_list),
                "Quarterly valuation": fake.pyint(1, 5),
                "Salary": fake.pyint(40000, 120000, 1000),
            })
    print("Данные успешно сгенерированы \n")


def read_csv():
    """Чтение данных из csv файла"""

    results = []
    with open('data.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
    return results


def get_report():
    """Формирование отчета по шаблону: название отдела, численость, мин. зарплата, мах. зарплата, ср. зарплата"""

    results = read_csv()
    report = []
    subdivisions_copy = []
    for row in results:
        subdivisions_copy.append(row["Subdivision"])
    subdivisions = Counter(subdivisions_copy)

    for key in subdivisions:
        salaries = []
        tmp_list = []
        tmp_list.append(key)
        tmp_list.append(subdivisions[key])

        for row in results:
            if row["Subdivision"] == key:
                salaries.append(int(row["Salary"]))

        tmp_list.append(min(salaries))
        tmp_list.append(max(salaries))
        tmp_list.append(sum(salaries) / len(salaries))
        report.append(tmp_list)
    return report


def show_subdivisions():
    """Вывод на экран всех отделов из файла с сотрудниками компании"""
    results = read_csv()
    subdivisions = set()
    for row in results:
        subdivisions.add(row["Subdivision"])
    for x in subdivisions:
        print(x)
    print()


def save_report():
    """Сохранение отчета в csv файл"""

    file = open('report.csv', 'w')
    with file:
        writer = csv.writer(file)
        writer.writerows(get_report())
    print("Отчет сохранен.\n")


def show_report():
    """Вывод на экран отчета"""
    report = get_report()
    for row in report:
        print(row)
    print()


def menu():
    """Выбор дейсвтия"""

    while True:
        print("1.Сгенерировать новые данные")
        print("2.Вывести все отделы")
        print("3.Вывести сводный отчёт")
        print("4.Сохранить сводный отчёт ")
        print("5.Выход")
        value = input()
        if value == "1":
            datagenerate(100)
        if value == "2":
            show_subdivisions()
        if value == "3":
            show_report()
        if value == "4":
            save_report()
        if value == "5":
            exit()


if __name__ == '__main__':
    menu()