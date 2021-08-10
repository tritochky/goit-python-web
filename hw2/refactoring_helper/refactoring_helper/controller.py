import os
import pathlib
import re

from datetime import datetime, timedelta, date
from .classbook import*
from .clean import*
from .models import*
from .notes_book import*
from .views import*


class CommandController:

    def __init__(self):
        self.model = VariableModel('')
        self.view = ConsoleView()

    def handler(self, user_inpu):

        ANSWEARS = {'add': self.add, 'ad': self.add, '+': self.add, 'фвв': self.add,
                    'change': self.change, 'срфтпу': self.change,
                    'close': self.exit, 'exit': self.exit, 'ex': self.exit, 'учше': self.exit,
                    'clear': self.clear, 'сдуфк': self.clear,
                    'find': self.find, 'аштв': self.find,
                    'help': self.help_func, 'рудз': self.help_func, 'хелп': self.help_func,
                    'save': self.save, 'іфму': self.save, 'ыфму': self.save,
                    'show': self.show, 'ырщц': self.show, 'ірщц': self.show,
                    'delete': self.delete, 'del': self.delete, 'вуд': self.delete, 'вудуеу': self.delete,
                    'birthday': self.birthday, 'ишкервфн': self.birthday,
                    'add note': self.add_note, 'фвв тщеу': self.add_note,
                    'delete note': self.delete_note, 'вудуеу тщеу': self.delete_note,
                    'edit note': self.edit_note, 'увше тщеу': self.edit_note,
                    'find note': self.find_note, 'аштв тщеу': self.find_note,
                    'sort notes': self.sort_notes, 'ыщке тщеуы': self.sort_notes,
                    'show notes': self.show_notes, 'ырщц тщеуы': self.show_notes,
                    'clean': self.clean_folder, 'сдуфт': self.clean_folder}

        if user_inpu in ANSWEARS.keys():
            return ANSWEARS[user_inpu]()
        elif user_inpu in ADD:
            decision = self.view.correct_wrong_add()
            decision = decision.lower()
            if decision in YES_COMMANDS:
                return self.add()
        elif user_inpu in CHANGE:
            decision = self.view.correct_wrong_change()
            decision = decision.lower()
            if decision in YES_COMMANDS:
                return self.change()
        elif user_inpu in FIND:
            decision = self.view.correct_wrong_find()
            decision = decision.lower()
            if decision in YES_COMMANDS:
                return self.find()
        elif user_inpu in HELP:
            decision = self.view.correct_wrong_help()
            decision = decision.lower()
            if decision in YES_COMMANDS:
                return self.view.show_help_func()
        elif user_inpu in DELETE:
            decision = self.view.correct_wrong_delete()
            decision = decision.lower()
            if decision in YES_COMMANDS:
                return self.delete()
        elif user_inpu in BIRTHDAY:
            decision = self.view.correct_wrong_birthday()
            decision = decision.lower()
            if decision in YES_COMMANDS:
                return self.birthday()
        elif user_inpu in CLEAN:
            decision = self.view.correct_wrong_clean()
            decision = decision.lower()
            if decision in YES_COMMANDS:
                return self.clean_folder()
        elif user_inpu in SHOW:
            decision = self.view.correct_wrong_show()
            decision = decision.lower()
            if decision in YES_COMMANDS:
                return self.show()
        else:
            return self.view.report_wrong_command()

    # @error_handler

    def save(self):
        self.model.save_books()

    # @error_handler

    def exit(self):
        self.save()
        self.view.esc_e = False
        return self.view.close()

    # @error_handler

    def help_func(self):
        self.view.show_help_func()

    # @error_handler

    def add(self):
        name = self.view.get_name()
        if name in EXIT:
            self.view.esc_e = False
            return self.view.worn()
        if len(self.model.book) > 0 and len(self.model.book) <= 25:
            id_n = self.model.book[-1]["Id"] + 1
        else:
            id_n = 1
        record1 = Record(name, id_n)
        while True:
            # try decision = view.ask_about_phone().lower()
            decision = self.view.ask_about_phone()
            decision = decision.lower()
            if decision in YES_COMMANDS:
                phone = self.view.get_phone()
                if re.fullmatch('[+]?[0-9]{3,12}', phone):
                    record1.add_phone(phone)
                else:
                    self.view.report_wrong_phone()
            elif decision in EXIT:
                self.model.book.add_record(record1.user)
                self.view.esc_e = False
                return self.view.close()
            elif decision in NO_COMMANDS:
                break
            else:
                self.view.report_wrong_command()
        while True:
            decision = self.view.ask_about_birthday()
            decision = decision.lower()
            if decision in YES_COMMANDS:
                birthday = self.view.get_birthday()
                try:
                    # birthday_d =
                    datetime.strptime(birthday, "%d.%m.%Y").date()
                    record1.user['Birthday'] = birthday
                    break
                except:
                    self.view.report_wrong_birthday()
            elif decision in EXIT:
                self.model.book.add_record(record1.user)
                self.view.esc_e = False
                return self.view.close()
            elif decision in NO_COMMANDS:
                break
            else:
                self.view.report_wrong_command()
        while True:
            decision = self.view.ask_about_address()
            decision = decision.lower()
            if decision in YES_COMMANDS:
                address = self.view.get_address()
                if len(address) > 1 and len(address) <= 50:
                    record1.user['Address'] = address
                    break
                else:
                    # lenght = len(address)
                    self.view.report_wrong_address(address)
            elif decision in EXIT:
                self.model.book.add_record(record1.user)
                self.view.esc_e = False
                return self.view.close()
            elif decision in NO_COMMANDS:
                break
            else:
                self.view.report_wrong_command()
        while True:
            decision = self.view.ask_aboiut_email()
            decision = decision.lower()
            if decision in YES_COMMANDS:
                email = self.view.get_email()
                if re.match('([a-zA-Z][a-zA-Z0-9\._!#$%^*=\-]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,})', email):
                    if len(email) > 1 and len(email) <= 50:
                        record1.user['E-mail'] = email
                        break
                    else:
                        self.view.report_wrong_email(email)
                else:
                    self.view.report_wrong_format_email()
            elif decision in EXIT:
                self.model.book.add_record(record1.user)
                self.view.esc_e = False
                return self.view.close()
            elif decision in NO_COMMANDS:
                break
            else:
                self.view.report_wrong_command()
        while True:
            decision = self.view.ask_aboiut_tag()
            decision = decision.lower()
            if decision in YES_COMMANDS:
                tags = self.view.get_tag()
                if len(tags) >= 1 and len(tags) <= 25:
                    record1.user['Tags'] = tags
                    break
                else:
                    self.view.report_wrong_tag(tags)
            elif decision in EXIT:
                self.model.book.add_record(record1.user)
                self.view.esc_e = False
                return self.view.close()
            elif decision in NO_COMMANDS:
                break
            else:
                self.view.report_wrong_command()
        self.model.book.add_record(record1.user)
        self.save()
        self.view.say()

    # @error_handler
    def change(self):
        old_name = self.view.start_change()
        old_name = old_name.lower()
        result = self.model.book.find_value(old_name)
        if len(result) > 0 and len(result) != None:
            self.show_find(result)
            if len(result) > 1:
                del_input = self.view.choose_id(result)
            decision = self.view.choose_to_change()
            decision = decision.lower()
            if decision in NAME_COMMAND:
                new_name = self.view.change_name()
                for i in result:
                    if 'del_input' in locals():
                        if i["Id"] == del_input:
                            i['Name'] = new_name
                            self.save()
                            return self.view.say()
                    elif 'del_input' not in locals():
                        i['Name'] = new_name
                        self.save()
                        return self.view.say()
                    else:
                        self.view.notify_wrong_name(old_name)
            elif decision in PHONE_COMMAND:  # нужен ай ди везде
                old_name = self.view.choose_phone()
                new_phone = self.view.change_phone()
                for i in result:
                    if 'del_input' in locals():
                        if i["Id"] == del_input:
                            if len(i['Phones']) > 1:
                                for j in i['Phones']:
                                    if j == old_name:
                                        i['Phones'].remove(j)
                                        i['Phones'].append(new_phone)
                                        self.save()
                                        return self.view.say()
                                    elif old_name == '':
                                        i['Phones'].append(new_phone)
                                        self.save()
                                        return self.view.say()
                                    else:
                                        self.view.notify_wrong_name(
                                            old_name)
                            elif len(i['Phones']) == 1:
                                if i['Phones'] == old_name:
                                    i['Phones'].remove(old_name)
                                    i['Phones'].append(new_phone)
                                    return self.view.say()
                                elif old_name == '':
                                    i['Phones'].append(new_phone)
                                    self.save()
                                    return self.view.say()
                            elif len(i['Phones']) == 0:
                                i['Phones'].append(new_phone)
                                self.save()
                                return self.view.say()
                    elif 'del_input' not in locals():
                        if len(i['Phones']) > 1:
                            for j in i['Phones']:
                                if j == old_name:
                                    i['Phones'].remove(j)
                                    i['Phones'].append(new_phone)
                                    self.save()
                                    return self.view.say()
                                elif old_name == '':
                                    i['Phones'].append(new_phone)
                                    self.save()
                                    return self.view.say()
                                else:
                                    self.view.notify_wrong_name(old_name)
                        elif len(i['Phones']) == 1:
                            if i['Phones'] == old_name:
                                i['Phones'].remove(old_name)
                                i['Phones'].append(new_phone)
                                return self.view.say()
                            elif old_name == '':
                                i['Phones'].append(new_phone)
                                self.save()
                                return self.view.say()
                        elif len(i['Phones']) == 0:
                            i['Phones'].append(new_phone)
                            self.save()
                            return self.view.say()
                    else:
                        self.view.notify_wrong_name(old_name)
            elif decision in BIRTHDAY_COMMAND:
                old_name = self.view.choose_birthday()
                new_birthday = self.view.change_birthday()
                try:
                    datetime.strptime(
                        new_birthday, "%d.%m.%Y").date()
                except:
                    self.view.wrong_input_birthday()
                for i in result:
                    if 'del_input' in locals():
                        if i["Id"] == del_input:
                            if i['Birthday'] == old_name:
                                i['Birthday'] = new_birthday
                                self.save()
                                return self.view.say()
                            elif i['Birthday'] == None:
                                i['Birthday'] = new_birthday
                                self.save()
                                return self.view.say()
                            else:
                                self.view.notify_wrong_name(old_name)
                    elif 'del_input' not in locals():
                        if i['Birthday'] == old_name:
                            i['Birthday'] = new_birthday
                            self.save()
                            return self.view.say()
                        elif i['Birthday'] == None:
                            i['Birthday'] = new_birthday
                            self.save()
                            return self.view.say()
                        else:
                            self.view.notify_wrong_name(old_name)
                    else:
                        self.view.notify_wrong_name(old_name)
            elif decision in ADDRESS_COMMAND:
                old_name = self.view.choose_address()
                new_address = self.view.change_address()
                for i in result:
                    if 'del_input' in locals():
                        if i["Id"] == del_input:
                            if i['Address'] == old_name:
                                i['Address'] = new_address
                                self.save()
                                return self.view.say()
                            elif i['Address'] == None:
                                i['Address'] = new_address
                                self.save()
                                return self.view.say()
                            else:
                                self.view.notify_wrong_name(old_name)
                    elif 'del_input' not in locals():
                        if i['Address'] == old_name:
                            i['Address'] = new_address
                            self.save()
                            return self.view.say()
                        elif i['Address'] == None:
                            i['Address'] = new_address
                            self.save()
                            return self.view.say()
                        else:
                            self.view.notify_wrong_name(old_name)
            elif decision in EMAIL_COMMAND:
                old_name = self.view.choose_email()
                new_email = self.view.change_email()
                for i in result:
                    if 'del_input' in locals():
                        if i["Id"] == del_input:
                            if i['E-mail'] == old_name:
                                i['E-mail'] = new_email
                                self.save()
                                return self.view.say()
                            elif i['E-mail'] == None:
                                i['E-mail'] = new_email
                                self.save()
                                return self.view.say()
                            elif old_name == '':
                                i['E-mail'].append(new_email)
                                self.save()
                                return self.view.say()
                            else:
                                self.view.notify_wrong_name(old_name)
                    elif 'del_input' not in locals():
                        if i['E-mail'] == old_name:
                            i['E-mail'] = new_email
                            self.save()
                            return self.view.say()
                        elif i['E-mail'] == None:
                            i['E-mail'] = new_email
                            self.save()
                            return self.view.say()
                        elif old_name == '':
                            i['E-mail'].append(new_email)
                            self.save()
                            return self.view.say()
                        else:
                            self.view.notify_wrong_name(old_name)
            elif decision in TAGS_COMMAND:
                old_name = self.view.choose_tag()
                new_tag = self.view.change_tag()
                for i in result:
                    if 'del_input' in locals():
                        if i["Id"] == del_input:
                            if i['Tags'] == old_name or i['Tags'] == None:
                                if len(new_tag) >= 1 and len(new_tag) <= 25:
                                    i['Tags'] = new_tag
                                    self.save()
                                    self.view.say()
                                else:
                                    self.view.report_wrong_tag(new_tag)
                            else:
                                self.view.notify_wrong_name(old_name)
                    elif 'del_input' not in locals():
                        if i['Tags'] == old_name or i['Tags'] == None:
                            if len(new_tag) >= 1 and len(new_tag) <= 25:
                                i['Tags'] = new_tag
                                self.save()
                                self.view.say()
                            else:
                                self.view.report_wrong_tag(new_tag)
                        else:
                            self.view.notify_wrong_name(old_name)
            elif decision in EXIT or decision == '7':
                self.view.esc_e = False
                self.view.close()
                return self.view.esc_e
        else:
            self.view.notify_wrong_name(old_name)

    # @error_handler

    def birthday(self):
        decision = self.view.choose_func_for_birthday()
        result = []
        if decision == 1:
            n = self.view.get_a_few_days()
            if n >= 365:
                n = n % 365
            today_d = datetime.now().date()
            d = timedelta(days=n)
            bday = today_d + d
            bday = bday.strftime("%d.%m.%Y")
            for i in self.model.book:
                if i["Birthday"] != 0 and i["Birthday"] != None:
                    if self.days_to_birthday(i["Birthday"]) == n:
                        result.append(i)
            self.show_find(result)
            self.view.notify_birthday_boys(bday, result)
        elif decision == 2:
            n = self.view.get_period()
            for i in self.model.book:
                if i["Birthday"] != 0 and i["Birthday"] != None:
                    if self.days_to_birthday(i["Birthday"]) <= n:
                        result.append(i)
            if len(result) > 0:
                self.show_find(result)
                self.view.notify_next_birthdays(n, result)
            else:
                self.view.notify_no_birthday(n)
        elif decision == 3:
            name = self.view.get_birthdays_name()
            result = self.model.book.find_value(name)
            if len(result) > 1:
                self.show_find(result)
                id_input = self.view.choose_id(result)
                for i in result:
                    if i["Id"] == id_input:
                        days = self.days_to_birthday(i['Birthday'])
                        if days == 0:
                            self.view.recall_congratulate_now(i)
                        else:
                            self.view.recall_congratulate(i, days)
            elif len(result) == 1:
                for i in result:
                    days = self.days_to_birthday(i['Birthday'])
                    if days == 0:
                        self.view.recall_congratulate_now(i)
                    else:
                        self.view.recall_congratulate(i, days)
            else:
                self.view.notify_no_information()
        elif decision in EXIT or decision == 4:
            self.view.esc_e = False
            return self.view.close()
        else:
            self.view.report_wrong_command()

    # @error_handler

    def days_to_birthday(self, bday):
        today_d = datetime.now().date()
        bday = datetime.strptime(bday, "%d.%m.%Y").date()
        bday = date(today_d.year, bday.month, bday.day)
        if today_d > bday:
            bday = date(today_d.year+1, bday.month, bday.day)
            days_left = (bday-today_d)
        else:
            days_left = (bday-today_d)
        return days_left.days

    # @error_handler

    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')

    # @error_handler

    def delete(self):
        find_v = self.view.choose_name_to_delete()
        find_v = find_v.lower()
        result = self.model.book.find_value(find_v)
        if len(result) > 1:
            for i in result:
                self.show_find(result)
                del_input = self.view.choose_id(result)
                for i in self.model.book:
                    if i["Id"] == del_input:
                        self.model.book.remove(i)
                        self.view.report_delete(find_v)
                        self.save()
        elif len(result) == 1:
            for i in result:
                if i["Name"].lower() == find_v:
                    self.model.book.remove(i)
                    self.view.report_delete(find_v)
                    self.save()
        else:
            self.view.notify_wrong_name()

    # @error_handler

    def find(self):
        find_v = self.view.get_something_to_find()
        result = self.model.book.find_value(find_v)
        self.show_find(result)

    # @error_handler

    def show_find(self, v_list):
        self.view.notify_to_find()
        self.view.print_top()
        for i in v_list:
            self.view.print_result_of_search(i)

    # @error_handler

    def show(self):
        number = self.view.get_number_of_records()
        try:
            number = int(number)
        except:
            number = 10
        self.view.notify_addressbook()
        # Печать шапки с названием столбцов
        self.view.print_top()
        iter = self.model.book.iterator(number)
        for i in iter:
            self.view.print_one_contact(i)
        self.view.notify_end_addressebook()

    # Команды для Handler для работы с NotesBook

    # @error_handler

    def add_note(self):
        lines = []
        flag = True
        # ввод многострочной заметки
        while flag:
            line = self.view.get_note()
            if len(line) > 0 and len(line) <= 40:
                lines.append(line)
            elif len(line) > 40:
                self.view.notify_wrong_note()
            else:
                flag = False
        text = '\n'.join(lines)
        # ввод тєгов
        flag = True
        while flag:
            hashtag = self.view.get_hashtag()
            # добавление заметки в NotesBook
            if len(hashtag) > 0 and len(hashtag) < 30:
                self.model.notes_book.add_note(text, hashtag.upper())
                self.save()
                flag = False
                return self.view.notify_successfully_saving()
            else:
                self.view.notify_wrong_hashtag()

    # @error_handler

    def delete_note(self):
        hashtag = self.view.get_hashtag_to_delete().upper()
        self.model.notes_book.delete_note(hashtag)
        self.view.notify_successfully_deleting(hashtag)

    # @error_handler

    def edit_note(self):
        hashtag = self.view.get_hashtag_to_edit().upper()
        for note in self.model.notes_book:
            if note[0] == hashtag:
                self.view.show_note_to_edit(note[1])
                # находим нужную заметку с заданным ключевым словом
                # и изменяем текст заметки
                lines = note[1].split('\n')
                counter = 0
                for line in lines:
                    new_line = self.view.start_to_edit_note(line)
                    if new_line:
                        lines.pop(counter)
                        lines.insert(counter, new_line)
                    counter += 1
                note[1] = '\n'.join(lines)
                new_note = note
                self.model.notes_book.edit_note(new_note)
                self.view.notify_editing_result()
                break
        else:
            self.view.notify_unsuccessful_editing()

    # @error_handler

    def find_note(self):
        keyword = self.view.get_keyword_to_search().upper()
        self.view.notify_result_of_search()
        result = self.model.notes_book.find_note(keyword)
        if result:
            self.view.show_result_of_search(result)
        else:
            self.view.notify_wrong_search()

    # @error_handler

    def sort_notes(self):
        search_type = self.view.get_typ_of_sort()
        # self.view.show_sorted_notes(search_type)
        self.view.print_notes_book(
            self.model.notes_book.sort_notes(search_type))

    # @error_handler

    def show_notes(self):
        self.view.show_all_notes()
        self.view.print_notes_book(self.model.notes_book)

    # Конец конец команд для NotesBook

    # @error_handler

    def clean_folder(self):
        cleaner = Cleaner()
        user_input = self.view.get_path_to_clean()
        path = pathlib.Path(user_input)
        cleaner.print_recursive(path, user_input)
        cleaner.delete_dir(user_input)
        self.view.notify_finish()


STARTING_COMMANDS = {('load', 'дщфв', '1'): 'load',
                     ('new', 'туц', '2'): 'new',
                     ('exit', 'esc', 'close', 'учше', '3'): 'exit'}

YES_COMMANDS = ['y', 'yes', 'нуі', 'н', 'да', 'д']
NO_COMMANDS = ['n', 'not', 'no', 'нет', 'тщ', 'тще', 'т']

ADD = ['a', 'ad', 'addd', 'asd', 'asdd', 'sdd', 'adf', 'фів', 'івв',
       'фівв', 'фввв', 'фва', 'вв', 'ыва', 'фвы', 'фыв', 'явв', 'фв']
CHANGE = ['chane', 'chnge', 'cange', 'chenge', 'hange', 'chng', 'cchenge', 'chhenge', 'cheenge', 'chaange',
          'сменить', 'chang', 'срутпу', 'срутп', 'менять', 'изменить', 'срфтп', 'рсфтпу', 'срутпу', 'cheng']
FIND = ['fnd', 'ind', 'fid', 'fin', 'faind', 'fand', 'ffind', 'fiind', 'finnd', 'findd',
        'seek', 'look', 'look for', 'атв', 'афтв', 'штв', 'афт', 'поиск', 'искать', 'найти', 'шштв']
HELP = ['&', '?', 'hlp', 'what', 'why', 'where', 'how', 'elp', 'hep', 'hel', 'healp',
        'halp', 'hhelp', 'heelp', 'hellp', 'helpp', 'рфдз', 'рдз', 'руз', 'руд', 'помощь']
DELETE = ['вуд', '-', 'del', 'вудуеу', 'вуфдуеу', 'dealete', 'elete', 'elet',
          'delet', 'dlte', 'dlt', 'lete', 'dealete', 'вудуе', 'удалить', 'pop']
BIRTHDAY = ['lf', 'birsday', 'bersday', 'bezday', 'bethday', 'birzday', 'bearsday', 'birthdey', 'beersday', 'brthday',
            'иууксвфн', 'ишквфн', 'др', 'рождение', 'бездей', 'бирсдей', 'днюха', 'birthday people', 'birthday boy',
            'birthday girl', 'birthda', 'birtda', 'birth', 'иуервфн', 'иуівфн', 'birt']
CLEAN = ['cleen', 'clan', 'clin', 'cleane', 'cleene', 'klin', 'klean', 'lean', 'clen',
         'kleen', 'суф', 'лдуут', 'лдуфт', 'сдуфту', 'клн', 'клин', 'разобрать', 'мусор']
SHOW = ['ырща', 'ырщцу', 'showe', 'schow', 'schove', 'chov', 'shove', 'schov',
        'schowe', 'how', 'sho', 'shouv', 'шов', 'ірщцу', 'показать', 'рщц', 'ірщм']
EXIT = ['exit', 'esc', 'close', 'ex', 'учше', 'уч']


NAME_COMMAND = ['name', 'тфьу', '1']
PHONE_COMMAND = ['phone', 'зрщту', '2']
BIRTHDAY_COMMAND = ['birthday', 'ишкервфн', '3']
ADDRESS_COMMAND = ['address', 'adress', 'adres', 'фввкуіі', 'фвкуі', '4']
EMAIL_COMMAND = ['email', 'e-mail', 'уьфшд', '5']
TAGS_COMMAND = ['tags', 'tag', 'ефп', '6']
