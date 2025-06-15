# Password Strength Checker (CLI)

A Python-based command-line application to evaluate the strength of a user's password based on customizable rules.  
Built with clean, modular code and designed for future extensibility (Web, GUI, or API).  

## Getting Started 

### Dependencies
- Python 3.8+
- Must have cloned this repository

### Running the Program 

```bash
python main.py
```

#### Project Structure

```
password_strength_checker/
|   checker/
|   |----__init__.py
|   |----rules.py # Contains password rule functions
|
|   main.py # CLI entry point
|   requirements.txt
|   README.md
```

## Features Implemented

- Password input via command-line
- Minimum length check (currently set to 8)
- Uppercase letter check
- DRY helper function to evaluate and report checks 
- Descriptive docstrings and inline comments for maintainability


## Feature Roadmap

- Add rules for lowercase, digits, and special characters 
- Password scoring and strength grading system
- Ability to custom change password length (8 or 12 or 16 length)
- Email scoring and strength grading system
- Suggest strong password
- Integrate Have I Been Pwned (HIBP) API to check for password breach
- Ability to download strong password 
- Create user accounts
- Create a password vault 
 