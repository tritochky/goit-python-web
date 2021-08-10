class ViewInterface:
    def iterator(self):
        raise NotImplementedError('Func "iterator" was not implemented')
    
    def greet(self):
        raise NotImplementedError('Func "greet" was not implemented')

    def start_work(self):
        raise NotImplementedError('Func "start_work" was not implemented')

    def get_path_to_willing_file(self):
        raise NotImplementedError(
            'Func "get_path_to_willing_file" was not implemented')

    def report_wrong_path(self):
        raise NotImplementedError(
            'Func "report_wrong_path" was not implemented')

    def get_path_to_new_file(self):
        raise NotImplementedError(
            'Func "get_path_to_new_file" was not implemented')


class ConsoleView(ViewInterface):
    def __init__(self):
        self.esc_e = True
        
    def iterator(self, data, n):
        counter = 0
        result = ""
        for i in data:
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

    def greet(self):
        print(100*'_')
        print('Hello my friend!')

    def start_work(self):
        print('What do you want to do?\nNow you can use commands:\n')
        print('1.  "load" to load AddressBook and NotesBook\n2.  "new" to create new Book\n3.  "exit"/"close" to close application:')
        return str(input())   # возвращает команду

    def get_path_to_willing_file(self):
        print(
            r'Please write the full path to file with addressbook and notebook. Example: "d:\test\book.txt":')
        return str(input())  # возвращает путь к файлу

    def report_wrong_path(self):
        print('Please write right path to file! This file is empty!')

    def get_path_to_new_file(self):
        print(
            r'Please write the full path where to create file. Example: "d:\test\book.txt":')
        return str(input())   # возвращает путь к файлу

    def report_wrong_command(self):
        print('Wrong command.')

    def choose_command(self):
        print(100*'_')
        print(
            '   What do you want to do?\n   Type exact command you want to do, \n   "help" for a list of commands,\n   "exit" to exit\n')
        return str(input())   # возвращает выбранную команду
