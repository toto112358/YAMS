# -*- coding: utf-8 -*-
#!/usr/bin/python3
import os
cmd = """
du  | awk '{print $2}' | sed 's/\.\///g'|grep -v ^_|grep -v __|sed '$d'|grep -v '/_'
"""
def process(files):
    """
    returns list of all commands from du scan of module dir
    """
    result = []
    for el1 in files:
        append = True
        for el2 in files:
            if el1 in el2 and el1 != el2:
                append = False
        if append:
            result.append(el1)
    return '\n'.join(result).replace('/', '.')

def transpile(contents):
    with open('./help/commands.py', 'w') as f:
        contents = 'print("""' + contents
        contents += '""")'
        f.write(contents)


if __name__ == '__main__':
    files = os.popen(cmd).read()
    files = files.split('\n')[:-1]
    transpile(process(files))
