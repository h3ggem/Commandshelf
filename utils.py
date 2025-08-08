# utils.py
# This is a utility module for various helper functions.
# It is designed to be used in a command execution context, where it can read configurations
# from a JSON file and execute shell commands, optionally in a dry run mode.
# It is not intended to be run as a standalone script, but rather as part of a larger application
# that manages command execution based on user input or other triggers.

import os

def ensure_dir_exists(path: str, verbose: bool = False) -> None:
    """Ensure a directory exists; create it if it doesn't."""
    if not os.path.exists(path):
        os.makedirs(path)
        if verbose:
            print(f"Created directory: {path}")

def sanitize_command_name(name: str) -> str:
    """
    Sanitize a command name by keeping only letters, numbers,
    dashes, and underscores.
    """
    return "".join(c for c in name if c.isalnum() or c in ('-', '_')).rstrip()

def confirm(prompt: str) -> bool:
    """Prompt user with yes/no question and return True if yes."""
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in ('y', 'yes'):
            return True
        elif answer in ('n', 'no'):
            return False
        else:
            print("Please enter 'y' or 'n'.")

# Assisted by YouTube & AI when writing this code.
