import sys
import os
from termcolor import colored
from docs import help
args = sys.argv

if len(args) == 1:
    help()

else:
    if args[1] in ('help', '-h'):
        if len(args) == 2:
            help()

        elif len(args) == 3:
            help(args[2])

        else:
            print(colored('\nERROR : Too many arguments passed.'))
