import os
import sys
from pathlib import Path
from os.path import dirname, abspath
import shutil
import time

path = Path(".").resolve()
BASE_PATH = path.parents[2]

findx = None 

log_txt = f"{abspath('.')}{os.sep}log.txt"
f = open(log_txt, 'w+')
f.write('')
f.close()

def write_log(pathX, sep):
    with open(log_txt, 'a+') as f:
        f.write(f"{sep} {pathX} \n")


def analayer(pathX):
    global findx 
    if pathX.find(findx) != -1:
        shutil.copy2(pathX, f"{abspath('.')}{os.sep}data") 
        print(f'Achei um .{findx} no {pathX} \nVou mandar pro {abspath(".")}{os.sep}data')


def getFoldrsAndFiles(base, sep='-'):
    folders = []            
            
    for path_in in os.listdir(base):
        interation = f"{base}{os.sep}{path_in}"
        
        if os.path.isdir(interation):
            print(f'Achei um diretório PATH: {interation}')
            folders.append(interation)
            
        elif os.path.isfile(interation):
            print(f'Achei um file PATH: {interation}')
            print(f'Vou escrever no log!')
            analayer(interation)
            write_log(interation, sep + '>')
            
    if folders:
        sep = sep + sep
        for foll in folders:
            index = folders.index(foll)
            folders.pop(index)
            try:
                getFoldrsAndFiles(foll, sep) 
            except:
                print('Não deu vai pro próximo')
    
    
re = r'''
---------------------------------------------------------------------
--->        ARQUIVO BASE: {}
---------------------------------------------------------------------
'''

if __name__ == '__main__':
    if 'search' in sys.argv[1]: 
        findx = str(sys.argv[1]).replace('search=','')
        print(findx)
    else:
        print('O primeiro parametro tem que ser search=[arquivo que deseja encontrar]')

    for folders_extract in sys.argv[2:]:
        try:
            with open(log_txt, 'a') as f:
                f.write(re.format(folders_extract))
                getFoldrsAndFiles(f"{BASE_PATH}{os.sep}{folders_extract}")
        except:
            print(f'Arquivo não exite arquivo: {BASE_PATH}{os.sep}{folders_extract}')


