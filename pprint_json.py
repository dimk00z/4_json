import json
import os
import argparse
from json import dumps, load as json_load


def read_json_filenames_from_args():
    args_parser = argparse.ArgumentParser(add_help=False)
    args_parser.add_argument("json_file_name", type=str, nargs='+',
                             help="json file for pretty print")
    return args_parser.parse_args().json_file_name


def load_json_from_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return json_load(file_handler)


def pretty_print_json(json):
    print(dumps(json, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    json_file_names = read_json_filenames_from_args()
    for json_file_name in json_file_names:
        try:
            json = load_json_from_file(json_file_name)
            if json:
                pretty_print_json(json)
            else:
                print("Файл {} не найден".format(json_file_name))
        except ValueError:
            print("Ошибка переобразования {} файла".format(json_file_name))
    print("Программа завершена.")
