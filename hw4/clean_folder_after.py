import pathlib
import re
import shutil
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread


def handle_image(path: pathlib.Path, root_folder: pathlib.Path):
    target_folder = root_folder / "images"
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/path.name)


def handle_video(path: pathlib.Path, root_folder: pathlib.Path):
    target_folder = root_folder / "videos"
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder / path.name)


def handle_document(path: pathlib.Path, root_folder: pathlib.Path):
    target_folder = root_folder / "documents"
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder / path.name)


def handle_archive(path: pathlib.Path, root_folder: pathlib.Path):
    target_folder = root_folder / "archives"
    name, _ = split_extension(path.name)
    target_folder.mkdir(exist_ok=True)
    archive_folder = target_folder / name
    archive_folder.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(str(path.absolute()),
                              str(archive_folder.absolute()))
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    path.unlink()


def handle_folder(path: pathlib.Path):
    try:
        path.rmdir()
    except OSError:
        pass


IMAGES = []
AUDIO = []
VIDEO = []
DOCUMENTS = []
ARCHIVES = []
FOLDERS = []
REGISTERED_EXTENSIONS = {
    'JPEG': IMAGES,
    'PNG': IMAGES,
    'JPG': IMAGES,
    'SVG': IMAGES,
    'AVI': VIDEO,
    'MP4': VIDEO,
    'MOV': VIDEO,
    'MKV': VIDEO,
    'DOC': DOCUMENTS,
    'DOCX': DOCUMENTS,
    'TXT': DOCUMENTS,
    'XLSX': DOCUMENTS,
    'PPTX': DOCUMENTS,
    'PDF': DOCUMENTS,
    'LOG': DOCUMENTS,
    'MP3': AUDIO,
    'OGG': AUDIO,
    'WAV': AUDIO,
    'AMR': AUDIO,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
}


def normalize(name: str) -> str:
    symbol_map = {ord("А"): "A", ord("а"): "a", ord("Б"): "B", ord("б"): "b", ord("В"): "V", ord("в"): "v", ord("Г"): "G", ord("г"): "g", ord("Д"): "D", ord("д"): "d", ord("Е"): "E", ord("е"): "e", ord("Ё"): "YO", ord("ё"): "yo", ord("Ж"): "ZH", ord("ж"): "zh", ord("З"): "Z", ord("з"): "z", ord("И"): "I", ord("и"): "i", ord("Й"): "Y", ord("й"): "y", ord("К"): "K", ord("к"): "k", ord("Л"): "L", ord("л"): "l", ord("М"): "M", ord("м"): "m", ord("Н"): "N", ord("н"): "n", ord("О"): "O", ord("о"): "o", ord("П"): "P", ord("п"): "p", ord("Р"): "R", ord(
        "р"): "r", ord("С"): "S", ord("с"): "s", ord("Т"): "T", ord("т"): "t", ord("У"): "U", ord("у"): "u", ord("Ф"): "F", ord("ф"): "f", ord("Х"): "H", ord("х"): "h", ord("Ц"): "C", ord("ц"): "c", ord("Ч"): "CH", ord("ч"): "ch", ord("Ш"): "SH", ord("ш"): "sh", ord("Щ"): "SCH", ord("щ"): "sch", ord("Ъ"): "", ord("ъ"): "", ord("Ы"): "I", ord("ы"): "i", ord("Ь"): "", ord("ь"): "", ord("Э"): "E", ord("э"): "e", ord("Ю"): "YU", ord("ю"): "yu", ord("Я"): "YA", ord("я"): "ya", ord("Є"): "YE", ord("є"): "ye", ord("Ї"): "YI", ord("ї"): "yi", ord(" "): "_"}
    new_name = name.translate(symbol_map)
    t_name = re.sub(r'[^\w\s]', '_', new_name)
    return t_name


def split_extension(file_name: str):
    ext_start = 0
    for idx, char in enumerate(file_name):
        if char == ".":
            ext_start = idx
    name = file_name[:ext_start]
    extension = file_name[ext_start+1:].upper()
    if not ext_start:
        return file_name, ""
    return name, extension


def scan(folder, FOLDERS, REGISTERED_EXTENSIONS):
    WORKERS = 2
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        for item in folder.iterdir():
            if item.is_dir():
                if item.name not in ("images", "videos", "documents", "archives"):
                    executor.submit(scan, item, FOLDERS, REGISTERED_EXTENSIONS)
                continue
            name, extension = split_extension(file_name=item.name)
            new_name = normalize(name)
            new_item = folder / ".".join([new_name, extension.lower()])
            item.rename(new_item)
            if extension:
                try:
                    container = REGISTERED_EXTENSIONS[extension]
                    container.append(new_item)
                except KeyError:
                    continue
    if not list(folder.iterdir()):
        folder.rmdir()
        return


def remove_files(folder):
    for file in IMAGES:
        slave1 = Thread(target=handle_image, args=(file, folder))
        slave1.start()
    for file in VIDEO:
        slave2 = Thread(target=handle_video, args=(file, folder))
        slave2.start()       
    for file in DOCUMENTS:
        slave3 = Thread(target=handle_document, args=(file, folder))
        slave3.start()        
    for file in ARCHIVES:
        slave4 = Thread(target=handle_archive, args=(file, folder))
        slave4.start()        
    for f in FOLDERS[::-1]:
        slave5 = Thread(target=handle_folder, args=(folder))
        slave5.start()        
    slave1.join()
    slave2.join()
    slave3.join()
    slave4.join()
    slave5.join()


def main(folder: pathlib.Path) -> None:
    scan(folder, FOLDERS, REGISTERED_EXTENSIONS)
    remove_files(folder)


if __name__ == "__main__":
    arg = pathlib.Path(input('Enter path: '))
    print(f"Start in {arg}.\n")
    started = time.time()
    main(arg.absolute())
    print(f'Done! Check your folder {arg.absolute()}, please.\n')
    elapsed = time.time() - started
    print(f'It takes {elapsed} sec')
