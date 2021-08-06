from collections import UserList


class NotesBook(UserList):
    # список списков: список заметок, каждая заметка - список с 2 элементов:
    # заметка[0]-строка с тєгами, заметка[1] - текст заметки

    def add_note(self, text, hashtag):
        # добавляет заметку в NotesBook
        note = [hashtag, text]
        self.append(note)

    def delete_note(self, hashtag):
        # удаляет заметку из NotesBook, которая имеет заметка[0]==hashtag
        for note in self:
            if note[0] == hashtag:
                self.remove(note)

    def edit_note(self, new_note):
        # редактирует заметку из NotesBook, которая имеет заметка[0]==hashtag
        for note in self:
            if note[0] == new_note[0]:
                note[1] = new_note[1]

    def find_note(self, keyword):
        # находит все заметки, в тэгах которых содержится keyword
        result = NotesBook()
        for i in self:
            if keyword in i[0]:
                result.append(i)
        return result

    def sort_notes(self, search_type="1"):
        # выводит список заметков в отсортированном виде
        # "1" - в алфавитном порядке
        # "2" - в обратном алфавитном порядке
        # "3" - от старых заметок к новым
        # "4" - от новых заметок к старым
        if search_type == "1":
            sorted_list = sorted(self)  # возвращает список
        elif search_type == "2":
            sorted_list = sorted(self)
            sorted_list.reverse()
        elif search_type == "3":
            sorted_list = list(self)
        elif search_type == "4":
            sorted_list = list(self)
            sorted_list.reverse()
        result = NotesBook()
        for note in sorted_list:
            result.append(note)
        return result

    def __str__(self):
        result = ""

        # Печать шапки с названием столбцов
        result += f" {72*'_'} \n"
        result += '|             TAGS             |                NOTE                     |\n'
        result += f" {72*'_'} \n"
        # Печать заметок
        for note in self:
            lines = note[1].split('\n')
            counter = 0
            for line in lines:
                if counter == 0:
                    result += f'|{note[0]:^30}| {line:^40}|\n'
                else:
                    result += f'|{" ":^30}| {line:^40}|\n'
                counter += 1
            result += f'|{30*"_"}|{40*"_"}|\n'
        return result
