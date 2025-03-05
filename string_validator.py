import re

def is_valid_string(s):
    """
    Checks if the given string meets the specified criteria:
    - At least 6 characters long
    - Contains 2 to 3 numbers
    - Numbers must be separated by at least one non-numeric character
    
    :param s: Input string to check
    :return: Tuple (bool, message) where bool is True if valid, otherwise False,
             and message explains why.
    """
    if len(s) < 6:
        return False, f"Invalid: The string '{s}' is too short (must be at least 6 characters)."

    # Finding all numbers in the string
    numbers = re.findall(r'\d', s)
    num_count = len(numbers)

    # Checking if there are at least 2 but no more than 3 numbers
    if not (2 <= num_count <= 3):
        return False, f"Invalid: The string '{s}' contains {num_count} numbers (must be between 2 and 3)."

    # Checking that numbers are separated by at least one non-numeric character
    if re.search(r'\d{2,}', s):
        return False, f"Invalid: The numbers in '{s}' are not separated by at least one non-numeric character."

    return True, f"Valid: The string '{s}' contains {num_count} numbers, separated correctly."

# Example of test cases
test_cases = ["a1b2c3", "123abc", "a1b2c", "a1bcdef2", "a1b2c3d4", "dhskj8sdb"]

for test in test_cases:
    result, message = is_valid_string(test)
    print(message)
