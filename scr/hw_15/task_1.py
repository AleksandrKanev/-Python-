# 📌 Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя логирование.
import argparse
import os
import logging
from collections import namedtuple

FORMAT = "{msg}"

logging.basicConfig(filename='log.log', format=FORMAT, filemode='a+', level=logging.NOTSET, style='{', encoding='utf-8')
logger = logging.getLogger()


def traverse_directory(directory):
    all_dir = os.walk(directory)
    Content = namedtuple('Content', ['path', 'name_content', 'ext'])
    for way, type_, file in all_dir:
        for dir_ in type_:
            cont = Content(way, dir_, 'd')  # как я понял это и есть флаг каталога
            logger.info(f'{cont.path}, {cont.name_content}, {cont.ext}')
        for f in file:
            res = str(f).rsplit('.', maxsplit=1)
            if len(res) == 1:
                res.append('файл без расширения')
            cont = Content(way, res[0], res[1])
            logger.info(f'{cont.path}, {cont.name_content}, {cont.ext}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Home work')
    parser.add_argument('param', type=str, nargs=1)
    args = parser.parse_args()
    traverse_directory(*args.param)
