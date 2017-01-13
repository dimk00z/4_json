import json
import sys
import os
import pprint


def load_data(filepath):
    if not os.path.exists(filepath):
        print("Файла "+filepath+" не найдено!")
        return None
    print("Загружен файл "+filepath)
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    pretty_printer = pprint.PrettyPrinter(indent=4)
    pretty_printer.pprint(data)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for param in sys.argv[1:]:
            json_from_file = load_data(param)
            if json_from_file:
                pretty_print_json(json_from_file)
    else:
        print("Не введены параметры командной строки " +
              "вида: python pprint_json.py <path to file>")
    print("Программа завершена.")


