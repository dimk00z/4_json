import json
import os
import argparse


def load_file(filepath):
    if not os.path.exists(filepath):
        print("Файла " + filepath + " не найдено!")
        return None
    else:
        print("Загружен файл " + filepath)
        return open(filepath, 'r', encoding='utf-8')


def load_json_data(json_file):
    try:
        return json.load(json_file)
    except ValueError:
        print("Ошибка переобразования JSON файла")


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


def read_json_filenames_from_args():
    args_parser = argparse.ArgumentParser(add_help=False)
    args_parser.add_argument("json_file_name", type=str, nargs='+',
                             help="json file for pretty print")
    return args_parser.parse_args().json_file_name


if __name__ == '__main__':
    json_file_names = read_json_filenames_from_args()
    for json_file_name in json_file_names:
        file_data = load_file(json_file_name)
        json_data = load_json_data(file_data)
        if json_data:
            pretty_print_json(json_data)
    print("Программа завершена.")
