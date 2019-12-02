import argparse
import os
import shutil
import time
from concurrent.futures import ThreadPoolExecutor

path = 'C:/Users/Артем/PycharmProjects/homework_30/sorted/'

parser = argparse.ArgumentParser(description='Sort files')
parser.add_argument('-t', '--extension', type=str, help='Enter file extension')
arg = parser.parse_args()


def files_mover(file_name) -> None:
    file_date = time.gmtime(os.path.getmtime(f'{path}{file_name}'))
    file_date = f'{file_date.tm_mday}_{file_date.tm_mon}'
    if file_date in os.listdir(path):
        shutil.move(f'{path}{file_name}', f'{path}{file_date}')
    else:
        os.mkdir(f'{path}{file_date}')
        shutil.move(f'{path}{file_name}', f'{path}{file_date}')


while True:
    list_of_names = os.listdir(path)
    with ThreadPoolExecutor() as executor:
        for name in list_of_names:
            if os.path.splitext(name)[1] == arg.extension:
                executor.submit(files_mover, name)
