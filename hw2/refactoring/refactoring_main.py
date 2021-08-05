#import os
#import pathlib
#import pickle
#import re

#from datetime import datetime, timedelta, date
#from classbook import*
#from clean import*
from controller import*
from models import*
#from notes_book import*
from views import*


STARTING_COMMANDS = {('load', 'дщфв', '1'): 'load',
                     ('new', 'туц', '2'): 'new',
                     ('exit', 'esc', 'close', 'учше', '3'): 'exit'}
'''
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
            print('я внутри error_handler ')
            result = view.report_input_error()
            return result
    return inner
'''

# @error_handler


def main():
    controller = CommandController()
    view = ConsoleView()
    controller.view = view
    view.greet()
    while True:
        command = view.start_work()
        for key in STARTING_COMMANDS:
            if command in key:
                command = STARTING_COMMANDS[key]
        #model = VariableModel(path)
        if command == 'load':
            path = view.get_path_to_willing_file()
            model = VariableModel(path)
            controller.model = model
            try:
                model.load_books()
                break
            except:
                view.report_wrong_path()
        elif command == 'new':
            path = view.get_path_to_new_file()
            model = VariableModel(path)
            controller.model = model
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


if __name__ == '__main__':
    main()
