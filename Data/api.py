import Data.dtst as dt
import pandas as pd

def show_registers():
    num_of_registers=int(input("Enter the amount of registers you want to display\n"))
    print(dt.df.head(num_of_registers))

def get_amount_of_registers():
    return (len(dt.df.index))

