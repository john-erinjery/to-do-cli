import os
import sys

availiable_commands = ['create', 'list', 'delete', 'done', 'modify']
# Help Functions

def help(param=''):
    """
    The complete help facility of the CLI
    """

    if not param:
        print('''
To-Do-List CLI : A Command-line tool for organising tasks!

Usage : todo <command> [<args>]

Availiable commands are listed below.
Type 'todo help <command>' for more info on a specific command.

Commands  Summary
--------  -------
create    create a new task to be added to the To-Do list
list      list tasks
delete    delete tasks
done      mark tasks as done
modify    modify task details
''')

    elif param not in availiable_commands:
        print('\nWARN todo help : no such command {0}'.format(param))
        
    else:
        if param == 'create':
            pass
        elif param == 'list':
            pass
        elif param == 'done':
            pass
        elif param == 'delete':
            pass
        else:
            pass