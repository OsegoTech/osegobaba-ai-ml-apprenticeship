# Simple calculator

# TODO: Prompt user for the first number
# TODO: Prompt user for the second number
# TODO: Prompt user for the operator (+, -, *, /)
# TODO: Perform the calculation based on user input
# TODO: Print the result
def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ✗ Invalid number. Please try again.\n")


def get_operator():
    """Keep asking until the user enters a valid operator."""
    valid = {"+", "-", "*", "/"}
    while True:
        op = input("Enter operator (+, -, *, /): ").strip()
        if op in valid:
            return op
        print("  ✗ Invalid operator. Choose from +  -  *  /\n")


def calculate(a, op, b):
    """Perform the calculation and return the result."""
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        if b == 0:
            return None  # signal division-by-zero
        return a / b


def format_result(n):
    """Show integers without a decimal point (e.g. 6 not 6.0)."""
    return int(n) if n == int(n) else n


def main():
    print("=" * 36)
    print("   Simple Command-Line Calculator")
    print("=" * 36)
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        # --- get first number (or exit) ---
        raw = input("Enter first number (or 'exit'): ").strip()
        if raw.lower() == "exit":
            break
        try:
            a = float(raw)
        except ValueError:
            print("  ✗ Invalid number. Please try again.\n")
            continue

        # --- get operator ---
        op = get_operator()

        # --- get second number ---
        b = get_number("Enter second number: ")

        # --- calculate ---
        result = calculate(a, op, b)

        if result is None:
            print("  ✗ Error: Division by zero is undefined.\n")
        else:
            print(f"\n  ➜  {format_result(a)} {op} {format_result(b)} = {format_result(result)}\n")

    print("\nGooduubye! 👋")


if __name__ == "__main__":
    main()
