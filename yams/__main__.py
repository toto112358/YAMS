#!/usr/bin/python3

from urllib import request
import sys


try:
    module = '._modules.'+sys.argv[1]
    sys.argv = sys.argv[1:]
    exec(f"from {module} import __main__")
except IndexError:
    module = '._modules.'+'help'
    sys.argv = sys.argv[1:]
    exec(f"from {module} import __main__")

except ModuleNotFoundError:
    print('run yams help to get a list of all commands')

except ImportError:
    print('run yams help to get a list of all commands')

# todo: add exception handler class if needed
