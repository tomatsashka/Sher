![(https://giffiles.alphacoders.com/211/211748.gif)](https://giffiles.alphacoders.com/211/211748.gif)

<br>
<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/129580860/230854841-815f4f2a-0dad-4796-877f-96210a616dae.png" />
</p>
<br>

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
