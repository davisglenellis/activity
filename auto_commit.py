# This script automatically pushes changes to GitHub
import os
import subprocess
from datetime import datetime
from random import random
import logging

# This runs commands in the command line
def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"Error running command {command}: {result.stderr}")
    return result

# This section commits and pushes the changes to GitHub
def commit_and_push_changes():
    # Define the path to the activity directory
    activity_dir = "/Users/davisglenellis/activity"

    # Change to the activity directory
    try:
        os.chdir(activity_dir)
    except Exception as e:
        logging.error(f"Error changing directory: {e}")

    # Define the commit message with the current date
    commit_message = f"Automated commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    # Commit and push changes
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push"], check=True)

# I only want to push around 3 times a day, and add some randomness so it seems more natural
def sometimes_this_triggers_commit_and_push():
    if random() < 0.99:
        commit_and_push_changes()
        print('worked!')

if __name__ == "__main__":
    sometimes_this_triggers_commit_and_push()
