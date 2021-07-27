try:
    from .refactoring_main import *
except:
    from refactoring_main import *
try:
    from .views import *
except:
    from views import *


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


class CommandController:
    def handler(self, user_inpu):
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
