import re
import pathlib
import shutil
import time

from threading import Thread

dir_list = ['audio', 'images', 'documents', 'video', 'archives', 'unknown']

AUDIO = ['.amr', '.ogg', '.wav', '.mp3']
IMAGES = ['.svg', '.jpg', '.jpeg', '.png']
VIDEO = ['.avi', '.mp4', '.mov', '.mkv']
DOCUMENTS = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', '.rtf', '.xls']
ARCHIVES = ['.zip', '.gz', '.tar']
UNKNOWN = []


def change_dist(path_dist, path_g, name_list_dir, user_input):

    e_suf = path_dist.suffix
    name_new = str(path_dist.stem).split('.')[0]
    name_w = normalize(path_dist.stem)

    name_n = name_w+e_suf
    d_d = user_input+'\\'+name_list_dir
    d_dpath = pathlib.Path(d_d)
    if not d_dpath.exists():
        d_dpath.mkdir()
    d = user_input+'\\'+name_list_dir+'\\'+name_n
    if name_list_dir != 'archives':
        shutil.move(path_dist, d)
    else:
        d_w = user_input+'\\'+name_list_dir+'\\'+name_w
        shutil.move(path_dist, d)
        shutil.unpack_archive(d, d_w)
        rem_ar = pathlib.Path(d)
        rem_ar.unlink()


def normalize(name):
    symbol_map = {ord("А"): "A", ord("а"): "a", ord("Б"): "B", ord("б"): "b", ord("В"): "V", ord("в"): "v", ord("Г"): "G", ord("г"): "g", ord("Д"): "D", ord("д"): "d", ord("Е"): "E", ord("е"): "e", ord("Ё"): "YO", ord("ё"): "yo", ord("Ж"): "ZH", ord("ж"): "zh", ord("З"): "Z", ord("з"): "z", ord("И"): "I", ord("и"): "i", ord("Й"): "Y", ord("й"): "y", ord("К"): "K", ord("к"): "k", ord("Л"): "L", ord("л"): "l", ord("М"): "M", ord("м"): "m", ord("Н"): "N", ord("н"): "n", ord("О"): "O", ord("о"): "o", ord("П"): "P", ord("п"): "p", ord("Р"): "R", ord(
        "р"): "r", ord("С"): "S", ord("с"): "s", ord("Т"): "T", ord("т"): "t", ord("У"): "U", ord("у"): "u", ord("Ф"): "F", ord("ф"): "f", ord("Х"): "H", ord("х"): "h", ord("Ц"): "C", ord("ц"): "c", ord("Ч"): "CH", ord("ч"): "ch", ord("Ш"): "SH", ord("ш"): "sh", ord("Щ"): "SCH", ord("щ"): "sch", ord("Ъ"): "", ord("ъ"): "", ord("Ы"): "I", ord("ы"): "i", ord("Ь"): "", ord("ь"): "", ord("Э"): "E", ord("э"): "e", ord("Ю"): "YU", ord("ю"): "yu", ord("Я"): "YA", ord("я"): "ya", ord("Є"): "YE", ord("є"): "ye", ord("Ї"): "YI", ord("ї"): "yi", ord(" "): "_"}
    new_name = name.translate(symbol_map)
    result = re.sub(r'[^\w\s]', '_', new_name)
    return result


def scan(path, user_input):

    if path.exists():
        if path.is_dir() and path.name not in dir_list:
            for element in path.iterdir():
                if element.is_file():
                    if element.suffix in AUDIO:
                        name_list_dir = 'audio'
                        change_dist(element, path, name_list_dir, user_input)

                    elif element.suffix in IMAGES:
                        name_list_dir = 'images'
                        change_dist(element, path, name_list_dir, user_input)

                    elif element.suffix in DOCUMENTS:
                        name_list_dir = 'documents'
                        change_dist(element, path, name_list_dir, user_input)

                    elif element.suffix in ARCHIVES:
                        name_list_dir = 'archives'
                        change_dist(element, path, name_list_dir, user_input)

                    elif element.suffix in VIDEO:
                        name_list_dir = 'video'
                        change_dist(element, path, name_list_dir, user_input)

                    else:
                        name_list_dir = 'unknown'
                        change_dist(element, path, name_list_dir, user_input)
                else:
                    scan(element, user_input)


def delete_dir(path):

    path = pathlib.Path(path)
    if path.is_dir() and path.name not in dir_list:
        for element in path.iterdir():
            if element.is_dir() and element.name not in dir_list:
                shutil.rmtree(element)
            else:
                delete_dir(element)


def delete_dir(path):
    path = pathlib.Path(path)
    if path.is_dir() and path.name not in dir_list:
        for element in path.iterdir():
            if element.is_dir() and element.name not in dir_list:
                shutil.rmtree(element)
            else:
                delete_dir(element)


def main(user_input):
    path = pathlib.Path(user_input)
    scan(path, user_input)
    delete_dir(path)
    return path


if __name__ == '__main__':
    user_input = input('Please enter the path:')
    started = time.time()
    main(user_input)
    print(f'Done! Check your folder {user_input}, please.\n')
    elapsed = time.time() - started
    print(f'It takes {elapsed} sec')
