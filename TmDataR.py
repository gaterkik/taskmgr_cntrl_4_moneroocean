import os
import psutil
import time
import subprocess

SOFT_NAME = ['tmdata.exe']
p = os.path.expanduser('~')


def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(['name']):
        for soft in name:
            if p.info['name'] == soft:
                ls.append(p)
    return ls


while True:

    if not find_procs_by_name(SOFT_NAME):
        print('софт не запущен - запускаю')
        # print(not find_procs_by_name(MINER_NAME))
        os.system(p + "\\moneroocean\\tmdata.exe")
    else:
        print('майнер запущен - ничего не делаю')

    time.sleep(30)
