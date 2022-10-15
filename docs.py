import os
import sys
import datetime
from termcolor import colored
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
        print(colored('\nWARN todo help : no such command {0}'.format(param), 'red'))
        
    else:
        if param == 'create':
            print('''
{1}

For creating tasks to add to the to-do list.
e.g : To create a basic task, doing the dishes:

    {0}

Options:
    -id, --identificator    A Unique ID assiged to the task
                            can be used to Identify the tasks in other functions.
    -n, --name              The name of the task
    -d, --date              Date for task completion in DD Mon YYYY format. {2}
                            set to the current date by default.
    -t, --time              Time for the Task completion. {3}
    -det, --details         Further details on the task.

{4}
            '''.format(colored('todo create \'Do the Dishes\'', 'green'), colored('Usage : todo create <task> [<options>]', attrs=['bold']),\
                colored('(eg : -d 23 Oct 2020)', attrs=['dark']), colored('(eg : -t 2.00 pm)', attrs=['dark']),\
                colored('e.g: todo create -n "Take out the Trash" -d 23 Oct 2020 -t 2.00 pm -det "Take out the trash at 2, Dad said." -id 1', attrs=['dark'])))


        elif param == 'list':
            pass
        elif param == 'done':
            pass
        elif param == 'delete':
            pass
        else:
            pass

def create(id, name, time='', det='',date=''):
    pass