# venv_manager.py

import argparse
import os
import shutil
import subprocess

# Define the standard name for the virtual environment directory.
VENV_DIR = 'venv'

def list_venvs():
    """
    Lists all virtual environments in the current working directory.
    A directory is considered a virtual environment if it contains a 'bin/activate' file.
    """
    print("Listing virtual environments in the current directory:")
    found = False
    # Check all subdirectories in the current directory.
    for item in os.listdir('.'):
        if os.path.isdir(item):
            # Check for the existence of the activation script.
            if os.path.exists(os.path.join(item, 'bin', 'activate')):
                print(f"✅ {item}")
                found = True
    if not found:
        print("No virtual environments found.")
    print("\nTo activate an environment, use: 'source <env_name>/bin/activate'")

def create_venv(name):
    """
    Creates a new virtual environment with the specified name.
    """
    print(f"Creating virtual environment '{name}'...")
    try:
        # Use subprocess to call the 'python3 -m venv' command.
        subprocess.run(['python3', '-m', 'venv', name], check=True, capture_output=True, text=True)
        print(f"Successfully created virtual environment '{name}'.")
        print(f"To activate, run: 'source {name}/bin/activate'")
    except FileNotFoundError:
        print("Error: 'python3' command not found. Make sure Python 3 is installed and in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating environment: {e.stderr}")
        print(f"Failed to create '{name}'. Please check for existing directories with the same name.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def delete_venv(name):
    """
    Deletes a virtual environment by removing its directory.
    """
    if not os.path.exists(name):
        print(f"Error: Virtual environment '{name}' does not exist.")
        return

    confirm = input(f"Are you sure you want to delete the virtual environment '{name}'? (y/n): ")
    if confirm.lower() == 'y':
        try:
            # Use shutil to remove the entire directory and its contents.
            shutil.rmtree(name)
            print(f"Successfully deleted virtual environment '{name}'.")
        except OSError as e:
            print(f"Error: Failed to delete directory '{name}': {e}")
    else:
        print("Deletion cancelled.")

def main():
    """
    Main function to parse command-line arguments and call the appropriate function.
    """
    parser = argparse.ArgumentParser(
        description="A simple command-line tool to manage Python virtual environments."
    )

    # Use subparsers to handle different commands like 'list', 'create', and 'delete'.
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create the parser for the "list" command.
    list_parser = subparsers.add_parser('list', help='List all virtual environments in the current directory.')

    # Create the parser for the "create" command.
    create_parser = subparsers.add_parser('create', help='Create a new virtual environment.')
    create_parser.add_argument('name', type=str, help='The name for the new virtual environment.')

    # Create the parser for the "delete" command.
    delete_parser = subparsers.add_parser('delete', help='Delete an existing virtual environment.')
    delete_parser.add_argument('name', type=str, help='The name of the virtual environment to delete.')

    args = parser.parse_args()

    # Check which command was provided and execute the corresponding function.
    if args.command == 'list':
        list_venvs()
    elif args.command == 'create':
        create_venv(args.name)
    elif args.command == 'delete':
        delete_venv(args.name)
    else:
        # If no command is given, show the help message.
        parser.print_help()

# Entry point of the script.
if __name__ == "__main__":
    main()
