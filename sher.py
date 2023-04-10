# -*- coding:utf-8 -*-


import os
import argparse

from libs.search import search_files


parser = argparse.ArgumentParser()

parser.add_argument("-q", "--query", type=str, required=True, help="Запрос поиска.")
parser.add_argument("-p", "--path", type=str, default=os.getcwd(), help="Путь к папке для поиска.")
parser.add_argument("--file", action="store_true", default=True,  help="Искать файл.")
parser.add_argument("--dir", action="store_true", help="Искать папку.")

args = parser.parse_args()


def main():
    if not os.path.isdir(args.path):
        exit(f"\n\n[-] Путь {args.path} не найден.")
        
    results = search_files(args.path, args.query)
    
    results.sort()
    
    if not results:
        exit("\n\n[-] Результаты поиска: ничего не найдено")
    
    print("[+] Результаты поиска: ")
    
    for result in results:
        if args.file and os.path.isfile(result):
            print(result)
        
        if args.dir and os.path.isdir(result):
            print(result)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit("[-] Завершение...")