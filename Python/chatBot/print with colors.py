# Define color codes
class colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

# Print colored text
print(f"{colors.RED}This is red text!{colors.RESET}")
print(f"{colors.GREEN}This is green text!{colors.RESET}")