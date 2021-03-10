import os, fnmatch
import pandas as pd
import datetime
from datetime import date, timedelta

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':

    print("current path:",os.getcwd())
    os.chdir("./merge_csv")
    print("working path:",os.getcwd())

    listOfFilesToRemove = os.listdir('./')
    pattern = "*.csv"
    li = []
    for entry in listOfFilesToRemove:
        if fnmatch.fnmatch(entry, pattern):
            print("csv file : ",entry)
            df = pd.read_csv(entry, index_col=None, header=0)
            li.append(df)

    df_frame = pd.concat(li, axis=0, ignore_index=True)

    today = date.today()
    df_frame.to_csv("stocks_movments_merged_" + str(today) + ".csv", index=True, sep='\t')

    print_hi('PyCharm')