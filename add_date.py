# This is the script that adds the current date to auto_commit.py

from random import random
from datetime import datetime

# Right now, adds the current date. In the future, I may call a LLM API to generate real code.
def update_file(filename='/Users/davisglenellis/activity/auto_commit.txt'):
    with open(filename, 'a') as file:
        file.write(str(datetime.now()) + '\n')

def sometimes_update_file():
    if random() < 0.04:
        update_file()
        print('worked!')

if __name__ == "__main__":
    sometimes_update_file()