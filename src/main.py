#!/usr/bin/python3

from urllib import request


url = 'https://lucasanss.xyz'

response = request.urlopen(url)
help(response)
print(response.read())
