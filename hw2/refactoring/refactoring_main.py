import os
import pathlib
#import pickle
#import json
import re

from datetime import datetime, timedelta, date
try:
    from .classbook import *
except:
    from classbook import *
try:
    from .clean import *
except:
    from clean import *
try:
    from .controller import CommandController
except:
    from controller import CommandController
try:
    from .modals import*
except:
    from modals import*
try:
    from .notes_book import *
except:
    from notes_book import *
try:
    from .views import *
except:
    from views import *


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
EXIT = ['exit', 'esc', 'close', 'учше']


def error_handler(func):
    def inner(*args):
        view = ConsoleView()
        try:
            result = func(*args)
            return result
        except:
            result = view.report_input_error()
            return result
    return inner


@error_handler
def main():
    controller = CommandController()
    view = ConsoleView()
    view.greet()
    while True:
        command = view.start_work()
        for key in STARTING_COMMANDS:
            if command in key:
                command = STARTING_COMMANDS[key]
        model = VariableModal(path)
        if command == 'load':
            path = view.get_path_to_willing_file()
            #model = VariableModal(path)
            try:
                model.load_books()
                break
            except:
                view.report_wrong_path()
        elif command == 'new':
            path = view.get_path_to_new_file()
            #model = VariableModal(path)
            break
        elif command == 'exit':
            view.esc_e = False
            view.close()
            break
        else:
            view.report_wrong_command()
    while view.esc_e:
        user_inpu = view.choose_command()
        user_inpu = user_inpu.lower()
        result = controller.handler(user_inpu)
        if result:
            print(result)
        elif result == None:
            pass
        else:
            break


'''
@error_handler
def handler(user_inpu): # перенесла в controller.py
    view = ConsoleView()
    if user_inpu in ANSWEARS.keys():
        return ANSWEARS[user_inpu]()
    elif user_inpu in ADD:
        decision = view.correct_wrong_add()
        decision = decision.lower()
        if decision in YES_COMMANDS:
            return add()
    elif user_inpu in CHANGE:
        decision = view.correct_wrong_change()
        decision = decision.lower()
        if decision in YES_COMMANDS:
            return change()
    elif user_inpu in FIND:
        decision = view.correct_wrong_find()
        decision = decision.lower()
        if decision in YES_COMMANDS:
            return find()
    elif user_inpu in HELP:
        decision = view.correct_wrong_help()
        decision = decision.lower()
        if decision in YES_COMMANDS:
            return view.help_func()
    elif user_inpu in DELETE:
        decision = view.correct_wrong_delete()
        decision = decision.lower()
        if decision in YES_COMMANDS:
            return delete()
    elif user_inpu in BIRTHDAY:
        decision = view.correct_wrong_birthday()
        decision = decision.lower()
        if decision in YES_COMMANDS:
            return birthday()
    elif user_inpu in CLEAN:
        decision = view.correct_wrong_clean()
        decision = decision.lower()
        if decision in YES_COMMANDS:
            return clean_folder()
    elif user_inpu in SHOW:
        decision = view.correct_wrong_show()
        decision = decision.lower()
        if decision in YES_COMMANDS:
            return show()
    else:
        return view.report_input_error()
'''


@error_handler
def save():
    book = VariableModal()
    book.save_books()


@error_handler
def exit():
    view = ConsoleView()
    save()
    view.esc_e = False
    return view.close()


@error_handler
def help_func():
    view = ConsoleView()
    view.help_func()


@error_handler
def add():
    view = ConsoleView()
    book = VariableModal()
    name = view.get_name()
    if name in EXIT:
        view.esc_e = False
        return view.worn()
    if len(book) > 0 and len(book) <= 25:
        id_n = book[-1]["Id"] + 1
    else:
        id_n = 1
    record1 = Record(name, id_n)
    while True:
        decision = view.ask_about_phone()  # try decision = view.ask_about_phone().lower()
        decision = decision.lower()
        if decision in YES_COMMANDS:
            phone = view.get_phone()
            if re.fullmatch('[+]?[0-9]{3,12}', phone):
                record1.add_phone(phone)
            else:
                view.report_wrong_phone()
        elif decision in EXIT:
            book.add_record(record1.user)
            view.esc_e = False
            return view.close()
        elif decision in NO_COMMANDS:
            break
        else:
            view.report_wrong_input()
    while True:
        decision = view.ask_about_birthday()
        decision = decision.lower()
        if decision in YES_COMMANDS:
            birthday = view.get_birthday()
            try:
                # birthday_d =
                datetime.strptime(birthday, "%d.%m.%Y").date()
                record1.user['Birthday'] = birthday
                break
            except:
                view.report_wrong_birthday()
        elif decision in EXIT:
            book.add_record(record1.user)
            view.esc_e = False
            return view.close()
        elif decision in NO_COMMANDS:
            break
        else:
            view.report_wrong_input()
    while True:
        decision = view.ask_about_address()
        decision = decision.lower()
        if decision in YES_COMMANDS:
            address = view.get_address()
            if len(address) > 1 and len(address) <= 50:
                record1.user['Address'] = address
                break
            else:
                view.report_wrong_address()
        elif decision in EXIT:
            book.add_record(record1.user)
            view.esc_e = False
            return view.close()
        elif decision in NO_COMMANDS:
            break
        else:
            view.report_wrong_input()
    while True:
        decision = view.ask_aboiut_email()
        decision = decision.lower()
        if decision in YES_COMMANDS:
            email = view.get_email()
            if re.match('([a-zA-Z][a-zA-Z0-9\._!#$%^*=\-]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,})', email):
                if len(email) > 1 and len(email) <= 50:
                    record1.user['E-mail'] = email
                    break
                else:
                    view.report_wrong_email()
            else:
                view.report_wrong_format_email()
        elif decision in EXIT:
            book.add_record(record1.user)
            view.esc_e = False
            return view.close()
        elif decision in NO_COMMANDS:
            break
        else:
            view.report_wrong_input()
    while True:
        decision = view.ask_aboiut_tag()
        decision = decision.lower()
        if decision in YES_COMMANDS:
            tags = view.get_tag()
            if len(tags) > 1 and len(tags) <= 25:
                record1.user['Tags'] = tags
                book.add_record(record1.user)
                save()
                return view.say()
            else:
                view.report_wrong_tag()
        elif decision in EXIT:
            book.add_record(record1.user)
            view.esc_e = False
            return view.close()
        elif decision in NO_COMMANDS:
            break
        else:
            view.report_wrong_input()


NAME_COMMAND = ['name', 'тфьу', '1']
PHONE_COMMAND = ['phone', 'зрщту', '2']
BIRTHDAY_COMMAND = ['birthday', 'ишкервфн', '3']
ADDRESS_COMMAND = ['address', 'adress', 'adres', 'фввкуіі', 'фвкуі', '4']
EMAIL_COMMAND = ['email', 'e-mail', 'уьфшд', '5']
TAGS_COMMAND = ['tags', 'tag', 'ефп', '6']


@error_handler
def change():
    view = ConsoleView()
    book = VariableModal()
    old_name = view.start_change()
    old_name = old_name.lower()
    result = book.find_value(old_name)
    if len(result) > 0 and len(result) != None:
        show_find(result)
        decision = view.choose_to_change()
        decision = decision.lower()
        if decision in NAME_COMMAND:
            new_name = view.change_name()
            if len(result) > 1:
                show_find(result)
                del_input = view.choose_id()
                for i in result:
                    if i["Id"] == del_input:
                        i['Name'] = new_name
                        save()
                        return view.say()
            elif len(result) == 1:
                for i in result:
                    i['Name'] = new_name  # try result['Name'] = new_name
                    save()
                    return view.say()
            else:
                view.notify_wrong_name()
        elif decision in PHONE_COMMAND:
            old_name = view.choose_phone()
            if len(result) > 1:
                show_find(result)
                del_input = view.choose_id()
                for i in result:
                    if i["Id"] == del_input:
                        new_phone = view.change_phone()
                        for i in result:
                            if len(i['Phones']) > 1:
                                for j in i['Phones']:
                                    if j == old_name:
                                        i['Phones'].remove(j)
                                        i['Phones'].append(new_phone)
                                        save()
                                        return view.say()
                                    else:
                                        view.notify_wrong_name()
                            elif len(i['Phones']) == 1:
                                i['Phones'].remove(old_name)
                                i['Phones'].append(new_phone)
                                return view.say()
                            elif len(i['Phones']) == 0:
                                i['Phones'].append(new_phone)
                                save()
                                return view.say()
            elif len(result) == 1:
                new_phone = view.change_phone()
                for i in result:
                    if len(i['Phones']) > 1:
                        for j in i['Phones']:
                            if j == old_name:
                                i['Phones'].remove(j)
                                i['Phones'].append(new_phone)
                                save()
                                return view.say()
                        else:
                            view.notify_wrong_name()
                    elif len(i['Phones']) == 1:
                        i['Phones'].remove(old_name)
                        i['Phones'].append(new_phone)
                        return view.say()
                    elif len(i['Phones']) == 0:
                        i['Phones'].append(new_phone)
                        save()
                        return view.say()
            else:
                view.notify_wrong_name()
        elif decision in BIRTHDAY_COMMAND:
            old_name = view.choose_birthday()
            if len(result) > 1:
                show_find(result)
                del_input = view.choose_id()
                for i in result:
                    if i["Id"] == del_input:
                        new_birthday = view.change_birthday()
                        try:
                            new_birthday = datetime.strptime(
                                new_birthday, "%d.%m.%Y").date()
                        except:
                            view.wrong_input_birthday()
                        for i in result:
                            if i['Birthday'] == old_name:
                                i['Birthday'] = new_birthday
                                save()
                                return view.say()
                            elif i['Birthday'] == None:
                                i['Birthday'] = new_birthday
                                save()
                                return view.say()
                            else:
                                view.notify_wrong_name()
            elif len(result) == 1:
                new_birthday = view.change_birthday()
                try:
                    new_birthday = datetime.strptime(
                        new_birthday, "%d.%m.%Y").date()
                except:
                    view.wrong_input_birthday()
                for i in result:
                    if i['Birthday'] == old_name:
                        i['Birthday'] = new_birthday
                        save()
                        return view.say()
                    elif i['Birthday'] == None:
                        i['Birthday'] = new_birthday
                        save()
                        return view.say()
                    else:
                        view.notify_wrong_name()
        elif decision in ADDRESS_COMMAND:
            old_name = view.choose_address()
            new_address = view.change_address()
            for i in result:
                if i['Address'] == old_name:
                    i['Address'] = new_address
                    save()
                    return view.say()
                elif i['Address'] == None:
                    i['Address'] = new_address
                    save()
                    return view.say()
                else:
                    view.notify_wrong_name()
        elif decision in EMAIL_COMMAND:
            old_name = view.choose_email()
            new_email = view.change_email()
            for i in result:
                if i['E-mail'] == old_name:
                    i['E-mail'] = new_email
                    save()
                    return view.say()
                elif i['E-mail'] == None:
                    i['E-mail'] = new_email
                    save()
                    return view.say()
                else:
                    view.notify_wrong_name()
        elif decision in TAGS_COMMAND:
            old_name = view.choose_tag()
            new_tag = view.change_tag()
            for i in result:
                if i['Tags'] == old_name:
                    i['Tags'] = new_tag
                    save()
                    return view.say()
                elif i['Tags'] == None:
                    i['Tags'] = new_tag
                    save()
                    return view.say()
                else:
                    view.notify_wrong_name()

        elif decision in EXIT or decision == '7':
            view.esc_e = False
            return view.esc_e

    else:
        view.notify_wrong_name()


@error_handler
def birthday():
    book = VariableModal()
    view = ConsoleView()
    decision = view.choose_func_for_birthday()
    result = []
    if decision == 1:
        n = view.get_a_few_days()
        if n >= 365:
            n = n % 365
        today_d = datetime.now().date()
        d = timedelta(days=n)
        bday = today_d + d
        bday = bday.strftime("%d.%m.%Y")
        for i in book:
            if i["Birthday"] != 0 and i["Birthday"] != None:
                if days_to_birthday(i["Birthday"]) == n:
                    result.append(i)
        view.notify_birthday_boys()
        show_find(result)
    elif decision == 2:
        n = view.get_period()
        for i in book:
            if i["Birthday"] != 0 and i["Birthday"] != None:
                if days_to_birthday(i["Birthday"]) <= n:
                    result.append(i)
        if len(result) > 0:
            view.notify_next_birthdays()
            show_find(result)
        else:
            view.notify_no_birthday()
    elif decision == 3:
        name = view.get_birthdays_name()
        result = book.find_value(name)
        if len(result) > 1:
            show_find(result)
            id_input = view.choose_id()
            for i in result:
                if i["Id"] == id_input:
                    days = days_to_birthday(i['Birthday'])
                    view.recall_congratulate()
        elif len(result) == 1:
            for i in result:
                days = days_to_birthday(i['Birthday'])
                view.recall_congratulate()
        else:
            view.notify_no_information()
    elif decision in EXIT or decision == 4:
        view.esc_e = False
        return view.close()
    else:
        view.notify_wrong_name()


@error_handler
def days_to_birthday(bday):
    today_d = datetime.now().date()
    bday = datetime.strptime(bday, "%d.%m.%Y").date()
    bday = date(today_d.year, bday.month, bday.day)
    if today_d > bday:
        bday = date(today_d.year+1, bday.month, bday.day)
        days_left = (bday-today_d)
    else:
        days_left = (bday-today_d)
    return days_left.days


@error_handler
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


@error_handler
def delete():
    view = ConsoleView()
    book = VariableModal()
    find_v = view.choose_name_to_delete()
    find_v = find_v.lower()
    result = book.find_value(find_v)
    for i in result:
        if i["Name"].lower() != find_v:
            result.remove(i)
    if len(result) > 1:
        show_find(result)
        del_input = view.choose_id()
        for i in book:
            if i["Name"].lower() == find_v and i["Id"] == del_input:
                book.remove(i)
                view.report_delete()
                save()
    elif len(result) == 1:
        for i in result:
            if i["Name"].lower() == find_v:
                book.remove(i)
                view.report_delete()
                save()
    else:
        view.notify_wrong_name()


@error_handler
def find():
    view = ConsoleView()
    book = VariableModal()
    find_v = view.get_something_to_find()
    result = book.find_value(find_v)
    show_find(result)


@error_handler
def show_find(v_list):
    view = ConsoleView()
    view.notify_to_find()
    view.print_top()
    for i in v_list:
        view.print_result_of_search()


@error_handler
def show():
    view = ConsoleView()
    book = VariableModal()
    number = view.get_number_of_records()
    try:
        number = int(number)
    except:
        number = 10
    view.notify_addressbook()
    # Печать шапки с названием столбцов
    view.print_top()
    if number == 0 or number == None:
        number = 10
    iter = book.iterator(number)
    for i in iter:
        print(i)
        view.show_pages_end()
    return view.notify_end_addressebook()

# Команды для Handler для работы с NotesBook


@error_handler
def add_note():
    view = ConsoleView()
    notes_book = VariableModal()
    lines = []
    flag = True
    # ввод многострочной заметки
    while flag:
        line = view.get_note()
        if len(line) > 0 and len(line) <= 40:
            lines.append(line)
        elif len(line) > 40:
            view.notify_wrong_note()
        else:
            flag = False
    text = '\n'.join(lines)
    # ввод тєгов
    flag = True
    while flag:
        hashtag = view.get_hashtag()
        # добавление заметки в NotesBook
        if len(line) > 0 and len(line) < 40:
            notes_book.add_note(text, hashtag.upper())
            flag = False
            view.notify_successfully_saving()
        else:
            view.notify_wrong_hashtag()


@error_handler
def delete_note():
    view = ConsoleView()
    notes_book = VariableModal()
    hashtag = view.get_hashtag_to_delete().upper()
    notes_book.delete_note(hashtag)
    view.notify_successfully_deleting()


@error_handler
def edit_note():
    view = ConsoleView()
    notes_book = VariableModal()
    hashtag = view.get_hashtag_to_edit().upper()
    notes_book.edit_note(hashtag)


@error_handler
def find_note():
    view = ConsoleView()
    notes_book = VariableModal()
    keyword = view.get_keyword_to_search().upper()
    view.notify_result_of_search()
    result = notes_book.find_note(keyword)
    if result:
        view.show_result_of_search()
    else:
        view.notify_wrong_search()


@error_handler
def sort_notes():
    view = ConsoleView()
    search_type = view.get_typ_of_sort()
    view.show_sorted_notes()


@error_handler
def show_notes():
    view = ConsoleView()
    view.show_all_notes()

# Конец конец команд для NotesBook


@error_handler
def clean_folder():
    cleaner = Cleaner()
    view = ConsoleView()
    user_input = view.get_path_to_clean()
    path = pathlib.Path(user_input)
    cleaner.print_recursive(path, user_input)
    cleaner.delete_dir(user_input)
    view.notify_finish()


ANSWEARS = {'add': add, 'ad': add, '+': add, 'фвв': add,
            'change': change, 'срфтпу': change,
            'close': exit, 'exit': exit, 'учше': exit,
            'clear': clear, 'сдуфк': clear,
            'find': find, 'аштв': find,
            'help': help_func, 'рудз': help_func, 'хелп': help_func,
            'save': save, 'іфму': save, 'ыфму': save,
            'show': show, 'ырщц': show, 'ірщц': show,
            'delete': delete, 'del': delete, 'вуд': delete, 'вудуеу': delete,
            'birthday': birthday, 'ишкервфн': birthday,
            'add note': add_note, 'фвв тщеу': add_note,
            'delete note': delete_note, 'вудуеу тщеу': delete_note,
            'edit note': edit_note, 'увше тщеу': edit_note,
            'find note': find_note, 'аштв тщеу': find_note,
            'sort notes': sort_notes, 'ыщке тщеуы': sort_notes,
            'show notes': show_notes, 'ырщц тщеуы': show_notes,
            'clean': clean_folder, 'сдуфт': clean_folder}


if __name__ == '__main__':
    main()
