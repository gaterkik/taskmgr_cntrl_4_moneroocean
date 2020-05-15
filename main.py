import psutil
import time
import subprocess

SOFT_NAME = 'Taskmgr.exe'
SERVICE_NAME = 'moneroocean_miner'
MINER_NAME = 'xmrig.exe'


def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(['name']):
        if p.info['name'] == name:
            ls.append(p)
    return ls


while True:
    s = psutil.win_service_get(SERVICE_NAME)
    print(s.as_dict()['status'])
    if find_procs_by_name(SOFT_NAME):
        print('Запущен диспетчер задач')
        if s.as_dict()['status'] == 'running':
            print('майнер запущен - останавливаю')
            print('Служба {} запущена'.format(SERVICE_NAME))
            subprocess.call(['sc', 'stop', SERVICE_NAME])
        else:
            print('майнер не запущен - ничего не делаю')
    else:
        print('He 3апущен диспетчер задач')
        if not find_procs_by_name(MINER_NAME):
            print('майнер не запущен - запускаю')
            subprocess.call(['sc', 'start', SERVICE_NAME])
        else:
            print('майнер запущен - ничего не делаю')
    time.sleep(1)

