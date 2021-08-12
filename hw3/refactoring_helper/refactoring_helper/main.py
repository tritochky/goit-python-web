from .controller import*
from .models import*
from .views import*


STARTING_COMMANDS = {('load', 'дщфв', '1'): 'load',
                     ('new', 'туц', '2'): 'new',
                     ('exit', 'esc', 'close', 'учше', '3'): 'exit'}


def error_handler(func):
    def inner(*args):
        try:
            return func(*args)
        except:
            print('я внутри error_handler ')
            print(
                'Wrong input! Type exact command you want to do,"exit" to exit or "help" for list of commands.')
    return inner


@error_handler
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
