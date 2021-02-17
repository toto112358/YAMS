#!/usr/bin/python3

from urllib import request
import sys

module = '._modules.'+sys.argv[1]

sys.argv = sys.argv[1:]
exec(f"from {module} import __main__")
