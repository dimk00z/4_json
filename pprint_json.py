import json
import os
import argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        print("Файла " + filepath + " не найдено!")
        return None
    else:
        print("Загружен файл " + filepath)
        return open(filepath, 'r', encoding='utf-8')

def load_json(json_file):
    try:
        return json.load(json_file)
    except ValueError:
        print("Ошибка переобразования JSON файла")


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("json_file_name", type=str, nargs='+',
                        help="display a square of a given number")
    for arg in parser.parse_args().json_file_name:
        json_from_file = load_data(arg)
        json_data = load_json(json_from_file)
        if json_data:
            pretty_print_json(json_data)
    print("Программа завершена.")
