import re
import shutil
#import pickle
import pathlib


class Cleaner:
    dir_list = ['audio', 'images', 'documents', 'video', 'archives', 'unknown']

    def __init__(self, path=None):
        self.path = path

    def change_dist(self, path_dist, path_g, name_list_dir, user_input):
        e_suf = path_dist.suffix
        name_new = str(path_dist.stem).split('.')[0]
        name_w = self.normalize(path_dist.stem)
        name_n = name_w + e_suf
        d_d = user_input + '\\' + name_list_dir
        d_dpath = pathlib.Path(d_d)
        if not d_dpath.exists():
            d_dpath.mkdir()
        d = user_input + '\\' + name_list_dir + '\\' + name_n
        if name_list_dir != 'archives':
            shutil.move(path_dist, d)
        else:
            d_w = user_input + '\\ '+ name_list_dir + '\\' + name_w
            shutil.move(path_dist, d)
            shutil.unpack_archive(d, d_w)
            rem_ar = pathlib.Path(d)
            rem_ar.unlink()

    def normalize(self, text):
        cyrilic_f = ['А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ю', 'Я', 'Ы', 'Ё', 'Э',
                     'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ю', 'я', 'ы', 'ё', 'э']
        cyr = ','.join(cyrilic_f)
        trans_f = ['A', 'B', 'V', 'H', 'G', 'D', 'E', 'E', 'Z', 'Z', 'Y', 'I', 'I', 'Y', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'H', 'T', 'C', 'S', 'S', 'Y', 'Y', 'Y', 'E', 'E',
                   'а', 'b', 'v', 'h', 'g', 'd', 'е', 'e', 'z', 'z', 'y', 'i', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 't', 'c', 's', 's', 'y', 'y', 'y', 'e', 'e']
        trans = ','.join(trans_f)
        dictionary = str.maketrans(cyr, trans)
        clean_text = re.sub('[^\w\s]', '_', text)
        result = clean_text.translate(dictionary)
        return result

    def print_recursive(self, path, user_input):
        audio_suf = ['.amr', '.ogg', '.wav', '.mp3']
        image_suf = ['.svg', '.jpg', '.jpeg', '.png']
        document_suf = ['.doc', '.docx', '.xlsx', '.pdf', '.txt', '.pptx', '.rtf', '.xls']
        archive_suf = ['.rar', '.zip', '.gz', '.tar']
        video_suf = ['.avi', '.mp4', '.mov', '.mkv', '.wmv']
        if path.exists():
            if path.is_dir() and path.name not in Cleaner.dir_list:
                for element in path.iterdir():
                    if element.is_file():
                        if element.suffix in audio_suf:
                            name_list_dir = 'audio'
                            self.change_dist(element, path,
                                        name_list_dir, user_input)
                        elif element.suffix in image_suf:
                            name_list_dir = 'images'
                            self.change_dist(element, path,
                                        name_list_dir, user_input)
                        elif element.suffix in document_suf:
                            name_list_dir = 'documents'
                            self.change_dist(element, path,
                                        name_list_dir, user_input)
                        elif element.suffix in archive_suf:
                            name_list_dir = 'archives'
                            self.change_dist(element, path,
                                        name_list_dir, user_input)
                        elif element.suffix in video_suf:
                            name_list_dir = 'video'
                            self.change_dist(element, path,
                                        name_list_dir, user_input)
                        else:
                            name_list_dir = 'unknown'
                            self.change_dist(element, path,
                                        name_list_dir, user_input)
                    else:
                        self.print_recursive(element, user_input)

    def delete_dir(self, path):
        path = pathlib.Path(path)
        if path.is_dir() and path.name not in Cleaner.dir_list:
            for element in path.iterdir():
                if element.is_dir() and element.name not in Cleaner.dir_list:
                    shutil.rmtree(element)
                else:
                    self.delete_dir(element)
