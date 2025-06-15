from checker.rules import check_length, check_for_uppercase, check_for_lowercase

def main():
    """ 
    Main entry point for the password strength checker.
    
    Handles user input, runs pre-defined password check functions while using an evaluation helper function.
    """
    user_password = input("Type the password to check it's strength: ")
    
    print(f"You entered: {user_password}")
    print("") # Empty print for spacing
    
    print("Checking password strength...")
    print("")
    
    
    # Check if the password matches the password rule for length
    evaluate_and_report_check(check_length, user_password, "8-letter Check")
    
    # Check if the password contains an uppercase
    evaluate_and_report_check(check_for_uppercase, user_password, "Uppercase Check")
    
    # Check if the password contains a lowercase 
    evaluate_and_report_check(check_for_lowercase, user_password, "Lowercase Check")





def evaluate_and_report_check(check_function, password, print_message): # Helper Function
    """ 
    Evalute a password rule and print the result to the console.
    
    Args:
        check_function (function): A function that takes a password and returns a boolean result.
        password (str): The user input password to check.
        print_message (str): A label describing the rules being checked.
    """
    check_result = check_function(password)
    
    if check_result == True:
        print(f"{print_message}: PASSED")
    else:
        print(f"{print_message}: FAILED")
        


# Ensures that the main function only runs when the script is directly executed, not when imported.
if __name__ == "__main__":
    main()