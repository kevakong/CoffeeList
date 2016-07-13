import pandas as pd
import random

df = []
filename = 'Employees_Birthday_Report_FINAL.csv'

def create_initial_list(filename):
    """
    Inputs a .csv filename
    returns a list of full names from the file
    """
    df = pd.read_csv(filename)
    length = len(df.index)  # how many names are in the data file
    list_names = []  # initialize list
    for name in range(length):  # for every index of dataframe
        list_names.append(df.iloc[name]['Full Name'])  # append full names to list of full names
    backuplist = list_names
    return list_names
list_names = create_initial_list(filename)
print list_names
random.shuffle(list_names)
print list_names

