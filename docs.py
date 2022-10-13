import os
import sys

# Help Functions

def help(*param):
    if not param:
        print('''
To-Do-List CLI : A Command-line tool for organising tasks!

Usage : todo <command> [<args>]

Availiable commands are listed below .
Type 
Commands :

''')
