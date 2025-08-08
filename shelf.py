# shelf.py
# This module manages a shelf of commands, allowing users to store and retrieve shell commands
# in a JSON file. It supports adding, running, listing, and removing commands via CLI.
# It is designed to be part of a larger app that manages command execution based on user input.

import argparse
import sys
from storage import load_commands, save_commands
from executor import run_command

# Add a new command to storage, optionally overwriting existing commands
def add_command(name: str, command: str, overwrite: bool = False) -> None:
    """Add a command to storage, optionally overwriting existing ones."""
    commands = load_commands()
    if not overwrite and name in commands:
        print(f"Command '{name}' already exists. Use --overwrite to replace it.")
        sys.exit(1)
    save_commands({name: command})
    print(f"Command '{name}' added successfully.")

# Run a stored command by name
def run_stored_command(name: str) -> None:
    """Run a stored command by name."""
    commands = load_commands()
    if name not in commands:
        print(f"No command named '{name}' found.")
        sys.exit(1)
    cmd = commands[name]
    print(f"Running command '{name}': {cmd}")
    exit_code = run_command(cmd)
    sys.exit(exit_code)

# List all stored commands in a readable format
def list_commands() -> None:
    """List all stored commands."""
    commands = load_commands()
    if not commands:
        print("No commands stored.")
        return
    print("Stored commands:")
    for name, cmd in commands.items():
        print(f" - {name}: {cmd}")

# Remove a stored command by name
def remove_command(name: str) -> None:
    """Remove a stored command by name."""
    commands = load_commands()
    if name not in commands:
        print(f"No command named '{name}' found.")
        sys.exit(1)
    del commands[name]
    save_commands(commands)
    print(f"Command '{name}' removed.")

# Main CLI entrypoint that handles subcommands and arguments
def main():
    parser = argparse.ArgumentParser(description="Manage your commandshelf.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subparser for 'add' command
    parser_add = subparsers.add_parser("add", help="Add a new command")
    parser_add.add_argument("name", type=str, help="Name of the command")
    parser_add.add_argument("cmd", type=str, help="Shell command to store")  # renamed to 'cmd'
    parser_add.add_argument("--overwrite", action="store_true", help="Overwrite existing command")

    # Subparser for 'run' command
    parser_run = subparsers.add_parser("run", help="Run a stored command")
    parser_run.add_argument("name", type=str, help="Name of the command to run")

    # Subparser for 'list' command
    subparsers.add_parser("list", help="List all stored commands")

    # Subparser for 'remove' command
    parser_remove = subparsers.add_parser("remove", help="Remove a stored command")
    parser_remove.add_argument("name", type=str, help="Name of the command to remove")

    args = parser.parse_args()

    # Dispatch to the appropriate function based on subcommand
    if args.command == "add":
        add_command(args.name, args.cmd, args.overwrite)  # use args.cmd here
    elif args.command == "run":
        run_stored_command(args.name)
    elif args.command == "list":
        list_commands()
    elif args.command == "remove":
        remove_command(args.name)

if __name__ == "__main__":
    main()
