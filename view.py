def get_op():
    op = int(input("1-import.\n 2 - export.\n 3- delete_person.\n 4 - change_person.\n 5 - exit.\n "))
    return op


def get_data():
    name = input("ИМЯ: ")
    surname = input('фамиля: ')
    telephone = input("телефон: ")
    data_str = name + " " + surname + " " + telephone + "\n"
    return data_str


def find_person():
    data_str = input("Введи параметр: ")
    return data_str
