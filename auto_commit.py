# This script automatically pushes changes to GitHub

import os
import subprocess
from datetime import datetime

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"Error running command {command}: {result.stderr}")
    return result

def commit_and_push_changes():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    run_command("git add .")
    commit_message = f"Auto commit at {current_time}"
    run_command(f"git commit -m \"{commit_message}\"")
    run_command("git push origin main")  # Replace 'main' with your branch name

if __name__ == "__main__":
    commit_and_push_changes()
