# Sher

## Описание проекта:
Проект Sher представляет собой утилиту для поиска файлов и (или) файлов по ключевому слову в определённой директории.

## Используемые модули:
- os
- functools
- argparse

## Структура проекта:
```
Sher/
| - sher.py
| - libs
    | - search.py
```
    
## Установка:
```
git clone https://github.com/tomatsashka/Sher.git
cd Sher
```
    
## Использование:
```
sher.py [-h] -q QUERY [-p PATH] [--file] [--dir]
```

**Пример использования:**
```
python sher.py -q hello.txt -p /home/user/ --file
python sher.py -q hello -p /home/user/ --dir
```
