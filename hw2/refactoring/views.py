from _typeshed import Self
try:
    from .classbook import Name
except:
    from classbook import Name
try:
    from .modals import*
except:
    from modals import*


class ViewInterface:
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

    def greet(self):
        print(100*'_')
        print('')
        print('Hello my friend!')

    def start_work(self):
        print('')
        print('What do you want to do?\nNow you can use commands:\n')
        print('1.  "load" to load AddressBook and NotesBook\n2.  "new" to create new Book\n3.  "exit"/"close" to close application:')
        print('')
        return str(input())   # возвращает команду

    def get_path_to_willing_file(self):
        print('')
        print(
            r'Please write the full path to file with addressbook and notebook. Example: "d:\test\book.txt":')
        print('')
        return str(input())  # возвращает путь к файлу

    def report_wrong_path(self):
        print('')
        print('Please write right path to file! This file is empty!')

    def get_path_to_new_file(self):
        print('')
        print(
            r'Please write the full path where to create file. Example: "d:\test\book.txt":')
        print('')
        return str(input())   # возвращает путь к файлу

    def report_wrong_command(self):
        print('')
        print('Wrong command.')
        print('')

    def choose_command(self):
        print(
            '   Successefully done!\n''\n   What do you want to do now?\n   Type exact command you want to do, \n   "help" for a list of commands,\n   "exit" to exit.\n')
        return str(input())   # возвращает выбранную команду

    def choose_yes_no(self):
        print('If YES type "yes" or "y"\nIf NO type "no" or "n"')

    def correct_wrong_add(self):
        print('')
        print('Maybe you mean "add" command?')
        self.choose_yes_no()
        print('')
        return str(input())

    def correct_wrong_change(self):
        print('')
        print('Maybe you mean "change" command?')
        self.choose_yes_no()
        print('')
        return str(input())

    def correct_wrong_find(self):
        print('')
        print('Maybe you mean "find" command?')
        self.choose_yes_no()
        print('')
        return str(input())

    def correct_wrong_help(self):
        print('')
        print('Maybe you mean "help" command?')
        self.choose_yes_no()
        print('')
        return str(input())

    def correct_wrong_delete(self):
        print('')
        print('Maybe you mean "delete" command?')
        self.choose_yes_no()
        print('')
        return str(input())

    def correct_wrong_birthday(self):
        print('')
        print('Maybe you mean "birthday" command?')
        self.choose_yes_no()
        print('')
        return str(input())

    def correct_wrong_clean(self):
        print('')
        print('Maybe you mean "clean" command?')
        self.choose_yes_no()
        print('')
        return str(input())

    def correct_wrong_show(self):
        print('')
        print('Maybe you mean "show" command?')
        self.choose_yes_no()
        print('')
        return str(input())

    def report_input_error(self):
        print('')
        print('Wrong input! Type exact command you want to do, "exit" to exit or "help" for list of commands.')
        print('')

    def help_func(self):
        print('')
        print(20*'*'+'WORKING WITH ADDRESSBOOK:'+20*'*')
        print('')
        print('*Type "add"      to add new contact.\n*Type "birthday" to see people that have birthday nearest days.\n*Type "change"   to change contact\'s phone, name or birthday.\n*Type "clear"    to clear terminal window.\n*Type "delete"   to delete information that you don\'t need.\n*Type "find"     to see information that you are looking for.\n*Type "show"     to show you all phonebook.\n*Type "save"     to save and exit.\n*Type "exit"     to exit\n')
        print(21*'*'+'WORKING WITH NOTESBOOK:'+21*'*')
        print('')
        print('*Type "add note"    to add new note.\n*Type "delete note" to delete note.\n*Type "edit note"   to edit note.\n*Type "find note"   to look through notes.\n*Type "sort notes"  to sort notes.\n*Type "show notes"  to show your notes.\n')
        print(19*'*'+'WORKING WITH CLEANFOLDER:'+19*'*')
        print('')
        print('*Type "clean"    to clean and structurise folder.\n')
        print(65*'*')
        print('')

    def say(self):
        print('Successfully changed')

    def get_name(self):
        print('Input Name:')
        self.name = Name(str(input()))
        return self.name

    def worn(self):
        print('Not saved')

    def choose_yes_no_exit(self):
        print('"y" (YES) or "n" (NO). Type "exit" to exit')

    def ask_about_phone(self):
        print('Do you want to add phone-number?')
        self.choose_yes_no_exit()
        return str(input())

    def get_phone(self):
        print('Input Phone Number. Example: +380501234567')
        return str(input())

    def report_wrong_phone(self):
        print(
            'Wrong input! Phone may start with + and has from 3 to 12 digits max. Example +380501234567')

    def close(self):
        print('Good Bye, my friend!')

    def report_wrong_input(self):
        print('Wrong input!')

    def ask_about_birthday(self):
        print('Do you want to add Birthday?')
        self.choose_yes_no_exit()
        return str(input())

    def get_birthday(self):
        print('Input Birthday. Expected day.month.year (Example: 25.12.1970). If year of birth is not known, type 1111')
        return str(input())

    def report_wrong_birthday(self):
        print(
            'Wrong format of Birthday. Expected day.month.year. Format: dd.mm.yyyy (Example: 25.12.1970)')

    def ask_about_address(self):
        print('Do you want to add Address?')
        self.choose_yes_no_exit()
        return str(input())

    def get_address(self):
        print('Input Address. Please no more than 50 symbols')
        return str(input())

    def report_wrong_address(self):
        print(
            f'Your Address is {len(self.address)} symbols. Please no more than 50 symbols')

    def ask_aboiut_email(self):
        print('Do you want to add E-mail?')
        self.choose_yes_no_exit()
        return str(input())

    def get_email(self):
        print('Input E-mail. Please no more than 50 symbols')
        return str(input())

    def report_wrong_email(self):
        print(
            f'Your E-mail is {len(self.email)} symbols. Please no more than 50 symbols')

    def report_wrong_format_email(self):
        print(
            'Format is wrong. Try again in format: your_nickname@something.domen_name')

    def ask_aboiut_tag(self):
        print('Do you want to add Tag?')
        self.choose_yes_no_exit()
        return str(input())

    def get_tag(self):
        print('Input Tag. Please no more than 25 symbols')
        return str(input())

    def report_wrong_tag(self):
        print(
            f'Your Tag is {len(self.tags)} symbols. Please no more than 25 symbols')

    def start_change(self):
        print('Type name of record you want to change')
        return str(input())

    def choose_to_change(self):
        print("")
        print('1.   To change Name: type "name".\n2.   To change Phone: type "phone".\n3.   To change Birthday: type "birthday".\n4.   To change Address: type "address".\n5.   To change E-mail: type "email".\n6.   To change Tags: type "tags"\n7.   To exit: type "exit".\n')
        print('')
        return str(input())

    def change_name(self):
        print('Type new name')
        return str(input())

    def choose_id(self):
        print('')
        print(
            f"I've found {len(self.result)} notes with this Name\nFor further work, choose Id")
        print('')
        return str(input())

    def notify_wrong_name(self):
        print('')
        print(f'{self.old_name} is not in Adress Book')

    def choose_phone(self):
        print('')
        print(
            'Type phone you want to change. If there are not phones - just press "enter".')
        print('')
        return str(input())

    def change_phone(self):
        print('')
        print('Type new phone')
        print('')
        return str(input())

    def choose_birthday(self):
        print('')
        print('Type birthday you want to change. Expected day.month.year (example: 25.12.1970). If there is not birthday - just press "enter".')
        print('')
        return str(input())

    def change_birthday(self):
        print(
            'Type new birthday. Expected day.month.year (example: 25.12.1970). If year of birth is not known, type 1111')
        print('')
        return str(input())

    def wrong_input_birthday(self):
        print(
            'Wrong input! Expected day.month.year (example: 25.12.1970)')

    def choose_address(self):
        print('')
        print(
            'Type address you want to change. If there is not address - just press "enter".')
        print('')
        return str(input())

    def change_address(self):
        print('Type new address.')
        print('')
        return str(input())

    def choose_email(self):
        print('')
        print(
            'Type E-mail you want to change. If there are not E-mail - just press "enter".')
        print('')
        return str(input())

    def change_email(self):
        print('Type new E-mail.')
        print('')
        return str(input())

    def choose_tag(self):
        print('')
        print(
            'Type Tag you want to change. If there are not Tags - just press "enter"')
        print('')
        return str(input())

    def change_tag(self):
        print('Type new Tag. Please no more than 25 symbols')
        print('')
        return str(input())

    def choose_func_for_birthday(self):
        print('')
        print(
            "1.   If you want to know, who'll have birthday after a few days TYPE 1.\n2.   If you want to know who'll have birthday in the coming days TYPE 2.\n3.   If you want to know how many days are to somebody's birthday TYPE 3.\n4.   Type 'exit' to exit")
        print('')
        return str(input())

    def get_a_few_days(self):
        print("Please write in how many days people's birthday will be.")
        return int(input())

    def notify_birthday_boys(self):
        print(
            f'On {self.bday} you should congratulate {len(self.result)} people from your Addressbook')

    def get_period(self):
        print("Please write how many days in advance to show you people's birthday.")
        return int(input())

    def notify_next_birthdays(self):
        print(
            f'In the coming {self.n} days you should congratulate {len(self.result)} people from your Addressbook')

    def notify_no_birthday(self):
        print(
            f'In the coming {self.n} days nobody from your Addressbook has a birthday')

    def get_birthdays_name(self):
        print("Please write name to know how many days left to birthday.")
        return str(input())

    def recall_congratulate(self):
        print(
            f'{self.i["Name"]} from your Addressbook will have birthday in {self.days} days. Do not forget to congratulate!')

    def notify_no_information(self):
        print(f'No information about birthday. Please enter valid information using command "change" or add new person to Addressbook')

    def choose_name_to_delete(self):
        print('')
        print('Put Name, you want to find and delete from your addressbook')
        print('')
        return str(input())

    def report_delete(self):
        print(f"You've deleted {self.find_v}")

    def get_something_to_find(self):
        print('')
        print('Put word, half of word or digits you want to find')
        print('')
        return str(input())

    def notify_to_find(self):
        print("I've found following:")

    def print_top(self):
        print('')
        # Печать шапки с названием столбцов
        print(145*'_')
        print('| ID  |           Name           |     Phones      |  Birthday  |           Address            |              E-mail            |       Tags     |')
        print(145*'-')

    def print_one_contact(self):
        print(f'|{self.i["Id"]:<5}| {self.i["Name"]:<25}| {self.i["Phones"][0] if len(self.i["Phones"]) >= 1 else " ":<15} | {self.i["Birthday"] if self.i["Birthday"] else " ":<11}|{self.i["Address"] if self.i["Address"] else " ":<30}|  {self.i["E-mail"] if self.i["E-mail"] else " ":<30}| {self.i["Tags"] if self.i["Tags"] else " ":<15}|')

    def print_result_of_search(self):
        self.print_one_contact()
        if len(self.i["Phones"]) > 1:
            for self.elem in self.i["Phones"][1:]:
                print(
                    f'|     |                          | {self.elem: <15} |            |                              |                                |                |')
        print(f"{145*'_'}\n")

    def get_number_of_records(self):
        print('')
        print('Please input the number of records on 1 page: ')
        return str(input())

    def notify_addressbook(self):
        print('')
        print("The contacts book is following:")

    def show_pages_end(self):
        print(63*'_'+'The end of the page. PRESS ENTER to continue'+63*'_')
        return input()

    def notify_end_addressebook(self):
        print("The end of the contacts book")

    def get_note(self):
        print('Please input your note (to stop entering note press "ENTER" twice):')
        return str(input())

    def notify_wrong_note(self):
        print('Please no more than 40 symbols in one line')

    def get_hashtag(self):
        print('Please input the hashtag of your note: \n')
        return str(input())

    def notify_successfully_saving(self):
        print("Your note is successfully saved")

    def notify_wrong_hashtag(self):
        print('Please no more than 30 symbols')

    def get_hashtag_to_delete(self):
        print("Please input a hashtag of note that you would like to delete:")
        return str(input())

    def notify_successfully_deleting(self):
        print(f"The note with hashtag '{self.hashtag}' is deleted")

    def get_hashtag_to_edit(self):
        print("Please input a hashtag of note that you would like to edit:")
        return str(input())

    def get_keyword_to_search(self):
        print('Please input keyword for search:')
        return str(input())

    def notify_result_of_search(self):
        print('THE RESULTS OF SEARCH:')

    def show_result_of_search(self):
        print(self.result)
        print("The search is sucessfully finished")

    def notify_wrong_search(self):
        print("Not found keyword")

    def get_typ_of_sort(self):
        print('')
        print("What type of sort would you like? Please input:")
        print('')
        print("1 - to sort from A to Z")
        print("2 - to sort from Z to A")
        print("3 - to sort from old notes to new notes")
        print("4 - to sort from new notes to old notes")
        print('')
        return str(input())

    def show_sorted_notes(self):
        notes_book = VariableModal()
        print('The sorted Notes are:')
        print(notes_book.sort_notes(self.search_type))
        print('The end of sorted Notes')

    def show_all_notes(self):
        notes_book = VariableModal()
        print('Your Notes Book:')
        print(notes_book)
        print("The end of Notes Book")

    def get_path_to_clean(self):
        print(100*"_")
        print('Welcome to clean folder instrument!')
        print(100*"_")
        print('Please enter path to clean and structurise.')
        return str(input())

    def notify_finish(self):
        print('Everything done! Please check yor folder!')
