#!/usr/bin/python3

"""

A script that adds all arguments to a python list
and then save them to a file

"""
import sys
import json


try:
    with open('add_item.json', 'r') as file:
        read_cont = file.read()
        cont = json.loads(read_cont)
        for arg in sys.argv[1:]:
            cont.append(arg)
        read_cont = json.dumps(cont)
except Exception:
    with open('add_item.json', 'w') as file:
        cont = []
        for arg in sys.argv[1:]:
            cont.append(arg)
        read_cont = json.dumps(cont)
        file.write(read_cont)
finally:
    with open('add_item.json', 'w') as file:
        file.write(read_cont)
