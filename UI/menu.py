import sys
import os
sys.path.insert(0, '/mnt/f/Cristobal/Tareas Prog/Prog III/Parcial1/')

from Data import api

def print_options():
    print("0. Exit app")
    print("1. Show amount of registers")
    print("2. Show registers(amount selected by user)")

def select_option(option):
    if option == 1:
        print("There are",api.get_amount_of_registers(), "registers")
    elif option == 2:
        api.show_registers()
        

def _menu():
    option=1
    while 0 != option:
        print_options()
        option=int(input("Enter the option\n"))
        select_option(option)
        if option:
            input("\nPRESS ENTER KEY TO CONTINUE")
        os.system('clear')


