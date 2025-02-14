#!/usr/bin/env python3
# Author ID: 113964225

def read_file(filename):
    """Reads a file and prints its contents line by line."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  # Remove extra newline
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except PermissionError:
        print(f"Error: No permission to read {filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    read_file('seneca2.txt')  # Modify with an actual file
