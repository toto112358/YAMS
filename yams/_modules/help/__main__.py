# -*- coding: utf-8 -*-
import sys
try:
    man_page = '._man_pages.'+sys.argv[1]
    exec(f'''from {man_page} import *''')

except:
    print('submodules available:\n')
    from .commands import *
    print('try help + command')
