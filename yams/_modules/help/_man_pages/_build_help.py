#!/usr/bin/python3
import sys
import os
'''
usage: exec from this dir
will look for each folder without _ and with
a man page inside and compile it to a main.py that
prints the compiled man page
'''

cmd = '''
du -a|awk '{print $2}'|sed 's/\.\///g'|grep -v _|grep \.man
'''

def transpile(filenames: list):
    for name in filenames:
        directory = '/'.join(name.split('/')[:-1])
        new_file = directory+'/main.py'
        contents = os.popen(f'''nroff - -m man < {name}''').read()
        contents = 'print("""' + contents
        contents += '""")'
        with open(new_file, 'w') as f:
            f.write(contents)
        with open(directory+'/__init__.py', 'w') as f:
            f.write('from .main import *')


if __name__ == '__main__':
    files = os.popen(cmd).read()[:-1]
    print(files)
    transpile(files.split('\n'))
