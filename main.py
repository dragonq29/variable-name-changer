# -*- coding: utf-8 -*-
from Tkinter import *

from StringChanger import StringChanger

f = open("input.txt", 'r')
lines = f.readlines()
f.close()

res_strings = StringChanger(lines)