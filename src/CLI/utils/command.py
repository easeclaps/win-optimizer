from subprocess import run, DEVNULL
from rich.console import Console

import shlex

def execute_command(command: str) -> None:
    if command is None:
        raise ValueError("command can't be empty")

    process = run(shlex.split(shlex.quote(command)), stdout=DEVNULL, stderr=DEVNULL, shell=True, capture_output=False)

    if process.returncode != 0:
        Console().print(" - Failed to run: [bold red]" + command + "[/bold red]")

def execute_commands(commands: list) -> None:
    if commands is None:
        raise ValueError("commands can't be empty")

    [execute_command(command) for command in commands]
