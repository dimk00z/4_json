import json
import os
import argparse
from json import dumps,load as json_load 

def load_file(filepath):
    if os.path.exists(filepath):
        return open(filepath, 'r', encoding='utf-8')


def load_json_data(json_file):
    try:
        return json_load(json_file)
    except ValueError:
        return None


def pretty_print_json(json):
    if json:
        print(dumps(json, indent=4, sort_keys=True, ensure_ascii=False))
    else:
        print("Ошибка переобразования JSON файла")


def read_json_filenames_from_args():
    args_parser = argparse.ArgumentParser(add_help=False)
    args_parser.add_argument("json_file_name", type=str, nargs='+',
                             help="json file for pretty print")
    return args_parser.parse_args().json_file_name


if __name__ == '__main__':
    json_file_names = read_json_filenames_from_args()
    for json_file_name in json_file_names:
        file_data = load_file(json_file_name)
        if not file_data:
            print("Файла {} не найдено!".format(json_file_name))
        else:
            print("Загружен файл {}".format(json_file_name))
            json = load_json_data(file_data) 
            pretty_print_json(json)           
        print("Программа завершена.")
