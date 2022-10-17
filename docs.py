import os
import sys
import datetime
from termcolor import colored
from json import load
availiable_commands = ['create', 'list', 'delete', 'done', 'modify', 'config']
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
config    configuration details for todo
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
    -d, --date              Date for task completion in DD-MM-YYYY format. {2}
                            set to the current date by default.
    -t, --time              Time for the Task completion. {3}
    -det, --details         Further details on the task.

{4}
            '''.format(colored('todo create \'Do the Dishes\'', 'green'), colored('Usage : todo create <task> [<options>]', attrs=['bold']),\
                colored('(eg : -d 23 Oct 2020)', attrs=['dark']), colored('(eg : -t 2.00 pm)', attrs=['dark']),\
                colored('e.g: todo create -n "Take out the Trash" -d 23-10-2020 -t 2.00 pm -det "Take out the trash at 2, Dad said." -id 1', attrs=['dark'])))


        elif param == 'list':
            pass
        elif param == 'done':
            pass
        elif param == 'delete':
            pass
        else:
            pass
# backend-functions
# These functions are not part of the main program, they are present to support the main functions.

def _check_config_file() -> bool:
    """
    Configuration directory check

    This functions checks the .config directory at 'C:/Users/USERNAME/.config' for 'todo.json' file.
    If the file is not present, it will return False, else True.
    """
    config_dir_path = 'C:/Users/{}/.config'.format(os.getenv('USERNAME'))
    global config_file_path

    config_file_path = config_dir_path + '/todo.json'
    if os.path.exists(config_file_path):
        return True
    else:
        return False

def _config_dictionary() -> dict:
    '''
    Returns the configuration dictionary for todo
    '''

    if _check_config_file():
        with open(config_file_path) as f:
            return load(f)
    else:
        return load(open('config.json'))
        
def create(id, name:str, time:str="", det:str='',date:str=datetime.date.today().strftime("%d-%m-%Y")):
    pass
