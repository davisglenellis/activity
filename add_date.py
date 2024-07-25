# This is the script that adds the current date to auto_commit.py

import os
import random
import string
import datetime

# Right now, adds the current date. In the future, I may call a LLM API to generate real code.
def update_file(filename='/Users/davisglenellis/activity/auto_commit.txt'):
    with open(filename, 'a') as file:
        file.write(str(datetime.date.today()) + '\n')

if __name__ == "__main__":
    update_file()