# executor.py
# This code is designed to be used in a command execution context, where it can read configurations
# from a JSON file and execute shell commands, optionally in a dry run mode.
# It is not intended to be run as a standalone script, but rather as part of a larger application
# that manages command execution based on user input or other triggers.

import subprocess
import json
import os

CONFIG_FILE = os.path.expanduser("~/.commandshelf/config.json")

def load_config():
    """Load config from JSON file or return default if missing/corrupt."""
    if not os.path.exists(CONFIG_FILE):
        return {"dry_run": False}
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            if "dry_run" not in config:
                config["dry_run"] = False
            return config
    except (json.JSONDecodeError, OSError):
        print("!WARNING! Could not read config file, using default settings.")
        return {"dry_run": False}
    
def run_command(cmd: str) -> int:
    """Run a shell command or print it if dry-run is enabled."""
    config = load_config()
    if config.get("dry_run", False):
        print(f"[DRY RUN] Would run: {cmd}")
        return 0
    try:
        result = subprocess.run(cmd, shell=True, check=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{cmd}': {e}")
        return e.returncode

# Assisted by YouTube & AI when writing this code.
