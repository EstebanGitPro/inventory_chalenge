import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_positive_int(prompt):
    """Prompts for a positive integer input."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Error: Value must be non-negative.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

def validate_non_empty_string(prompt):
    """Prompts for a non-empty string input."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("Error: Input cannot be empty.")
        else:
            return value

def print_table(headers, rows):
    """Prints a formatted table without emojis."""
    if not rows:
        print("No data available.")
        return

    # Calculate column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Create format string
    fmt = " | ".join([f"{{:<{w}}}" for w in col_widths])
    separator = "-+-".join(["-" * w for w in col_widths])

    print(fmt.format(*headers))
    print(separator)
    for row in rows:
        print(fmt.format(*[str(cell) for cell in row]))
