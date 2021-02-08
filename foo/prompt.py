#!/usr/bin/python3


import sys

class command:
	def __init__(self, cmd):
		self.cmd = cmd

	def exec(self):
		if self.cmd == 'q':
			sys.exit()

class prompt:
	def __init__(self, filename):
		self.filename = filename

	def exec(self, cmd):
		self.contents = (open(self.filename, 'r',
				encoding = 'utf-8').readlines()
				if self.filename else [])
		print(self.contents)
		print(cmd)
