import re

from collections import UserList
from datetime import datetime
from .views import ConsoleView


class AddressBook(UserList):

    '''def __str__(self) -> str:
        result = ""
        for i in self.user:
            result += f'|{i["Id"]:<5}| {i["Name"]:<25}| { i["Phones"][0] if len(i["Phones"])>=1 else " ":<15} | {str(i["Birthday"]) if i["Birthday"] else " ":<11}|{i["Address"]if i["Address"] else " ":<30}|  {i["E-mail"]if i["E-mail"] else " ":<30}| {i["Tags"] if i["Tags"] else " ":<15}|\n'
            if len(i["Phones"]) > 1:
                for elem in i["Phones"][1:]:
                    result += f'|     |                          | {elem: <15} |            |                              |                                |                | \n'
            result += f"{145*'_'}\n"
        return result'''

    data = []

    def add_record(self, record):
        self.data.append(record)

    def find_value(self, f_value):
        f_value = f_value.lower()
        result = AddressBook()
        for item in self:
            for value in item.values():
                if (isinstance(value, str)):
                    value = value.lower()
                    if value.find(f_value) != -1:
                        if item not in result:
                            result.append(item)
                            break
                elif value != None:
                    if (isinstance(value, list)):
                        for j in value:
                            j = j.lower()
                            if j.find(f_value) != -1:
                                result.append(item)
                                break
        return result
'''
    def iterator(self, n):
        counter = 0
        result = ""
        for i in self:
            result += f'|{i["Id"]:^5}|{i["Name"]:^23}|{i["Phones"][0] if len(i["Phones"])>=1 else " ":^15}|{str(i["Birthday"]) if i["Birthday"] else " ":^11}|{i["Address"] if i["Address"] else " ":^50}|{i["E-mail"] if i["E-mail"] else " ":^30}|{i["Tags"] if i["Tags"] else " ":^26}|\n'
            if len(i["Phones"]) > 1:
                for elem in i["Phones"][1:]:
                    result += f'|     |                       |{elem: ^15}|           |                                                  |                              |                          | \n'
            result += f"{168*'_'}\n"
            # конец записи строки с описанием 1 контакта
            counter += 1
            if counter == n:
                result = result.rstrip("\n")
                yield result
                result = ""
                counter = 0
        if result:
            result = result.rstrip("\n")
            yield result
'''

class Record:
    def __init__(self, name, id_n, birthday=None, address=None, email=None, tags=None):
        self.id_n = id_n
        self.name = name
        self.phones = []
        self.birthday = birthday
        self.address = address
        self.email = email
        self.tags = tags
        self.user = {'Id': self.id_n,
                     'Name': self.name,
                     'Phones': self.phones,
                     'Birthday': self.birthday,
                     'Address': self.address,
                     'E-mail': self.email,
                     'Tags': self.tags}

    def __str__(self) -> str:
        result = ""
        for i in self.user:
            result += f'|{i["Id"]:^5}|{i["Name"]:^23}|{i["Phones"][0] if len(i["Phones"])>=1 else " ":^15}|{str(i["Birthday"]) if i["Birthday"] else " ":^11}|{i["Address"] if i["Address"] else " ":^50}|{i["E-mail"] if i["E-mail"] else " ":^30}|{i["Tags"] if i["Tags"] else " ":^26}|\n'
            if len(i["Phones"]) > 1:
                for elem in i["Phones"][1:]:
                    result += f'|     |                       |{elem: ^15}|           |                                                  |                              |                          | \n'
            result += f"{168*'_'}\n"
        return result

    def add_address(self, address):
        self.address = address

    def add_email(self, email):
        self.email = email

    def add_id(self, id_n):
        self.id_n = id_n

    def add_phone(self, phone):
        view = ConsoleView()
        phone = str(phone)
        try:
            num = re.fullmatch('[+]?[0-9]{3,12}', phone)
            if num:
                self.phones.append(phone)
        except:
            view.report_wrong_phone()

    def remove_phone(self, phone):
        for i in range(len(self.phones)):
            if self.phones[i].phone == phone:
                self.phones.pop(i)

    def edit_phone(self, phone, new_phone):
        self.remove_phone(phone)
        self.add_phone(new_phone)


class Field:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        phones = []
        self.phones = list()
        self.__phone = phone

    @ property
    def phone(self):
        return self.__phone

    @ phone.setter
    def phone(self, value):
        self.__phone = ''
        view = ConsoleView()
        if re.fullmatch('[+]?[0-9]{3,12}', value):
            self.__phone = value
        else:
            view.report_wrong_phone()

    # def __str__(self):
        # return self.phone
    def __repr__(self):
        return self.phone


class Address(Field):
    def __init__(self, address):
        self.address = address


class Tags(Field):
    def __init__(self, tags):
        self.tags = tags


class Id(Field):
    def __init__(self, id_n):
        self.id_n = id_n


class Email(Field):
    def __init__(self, email):
        self.email = email


class Birthday(Field):
    def __init__(self, value):
        self.__birthday = None
        self.birthday = value

    @ property
    def birthday(self):
        return self.__birthday.strftime('%d.%m.%Y')

    @ birthday.setter
    def birthday(self, birthday):
        view = ConsoleView()
        try:
            self.__birthday = datetime.strptime(birthday, '%d.%m.%Y')
        except Exception:
            view.report_wrong_birthday()
