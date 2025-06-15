def check_length(password):
    """ 
    Check if the password is at least 8 characters long.
    
    Args:
        password (str): The user input password to check.
    
    Returns:
        bool: True if the password length is 8 or more, False otherwise.
    """
    # Ternary expression
    return True if len(password) >= 8 else False


def check_for_uppercase(password):
    """ 
    Check if the password contains at least one uppercase letter.
    
    Args:
        password (str): The user input password to check.
    
    Returns:
        bool: True if at least one uppercase character is found, False otherwise. 
    """    
    for character in password: # Iterate through the password checking for uppercase 
        if character.isupper():
            return True 
    return False # Scanned string and found no uppercase


def check_for_lowercase(password):
    """ 
    Check if the password contains at least one lowercase letter.
    
    Args:
        password (str): The user input password to check.
    
    Returns:
        bool: True if at least one lowercase character is found, False otherwise.
    """
    for character in password: # Iterate through the password checking for lowercase
        if character.islower(): 
            return True
    return False # Scanned entire password and found no lowercase letter


def check_for_digit(password):
    """ 
    Check if the password contains at least one numeric digit.
    
    Args:
        password (str): The user input password to check.
    
    Returns:
        bool: True if at least one digit is found, False otherwise.
    """
    for character in password: # Iterate through the password checking for a digit
        if character.isdigit():
            return True
    return False # Scanned entire password and found no digit