# storage.py
# This module stores and loads commands from a JSON file.
# This code is designed to be used in a command execution context, where it can read configurations
# from a JSON file and execute shell commands, optionally in a dry run mode.
# It is not intended to be run as a standalone script, but rather as part of a larger application
# that manages command execution based on user input or other triggers.

import json
import os
from typing import Dict, List  # for type hints

COMMANDS_FILE = os.path.expanduser("~/.commandshelf/commands.json")

def load_commands() -> Dict[str, str]:
    """Load commands from JSON file or return empty dict if missing/corrupt."""
    if not os.path.exists(COMMANDS_FILE):
        return {}
    try:
        with open(COMMANDS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"!WARNING! Could not read commands file: {e}. Returning empty commands.")
        return {}

def save_commands(new_commands: Dict[str, str]) -> None:
    """
    Merge and save new commands into the JSON file.

    Args:
        new_commands (Dict[str, str]): A dictionary containing the command(s) to add.
                                       Example: {"updater": "sudo apt update"}
    """
    commands = load_commands()
    commands.update(new_commands)
    os.makedirs(os.path.dirname(COMMANDS_FILE), exist_ok=True)
    with open(COMMANDS_FILE, "w") as f:
        json.dump(commands, f, indent=2)

def add_command_from_args(args: List[str]) -> None:
    """
    Handles command-line arguments to add a new command.

    Args:
        args (List[str]): A list of strings, typically from a command-line parser.
                          Example: ["updater", "sudo apt update"]
    """
    if len(args) < 2:
        print("Usage: add <command_name> <command_string>")
        return

    command_name = args[0]
    command_string = " ".join(args[1:])  # Join the remaining parts to form the command string
    
    # Create the dictionary that save_commands expects
    new_command = {command_name: command_string}
    
    # Call the save function with the correctly formatted dictionary
    save_commands(new_command)
    print(f"Command '{command_name}' added successfully.")

# Assisted by YouTube & AI when writing this code.