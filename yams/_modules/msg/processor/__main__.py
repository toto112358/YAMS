# -*- coding: utf-8 -*-
import sys
from .main import process

imput = ""
with sys.stdin as f:
    for line in f.readlines():
        imput += line

print(process(imput))
