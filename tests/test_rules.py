import os 
import sys

# Add parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from checker.rules import (
    check_length,
    check_for_uppercase,
    check_for_lowercase,
    check_for_digit,
    check_for_special_chars,
)

# --- Basic Functional Tests ---

def test_check_length() -> None:
    """ 
    Test minimum password length check.
    Should return True for length >= 8, and False otherwise.
    """
    assert check_length("12345678") == True
    assert check_length("short") == False


def test_check_for_uppercase() -> None:
    """ 
    Test if at least one uppercase character is detected.
    """
    assert check_for_uppercase("abcD") == True
    assert check_for_uppercase("abcd") == False


def test_check_for_lowercase() -> None:
    """ 
    Test if at least one lowercase character is detected.
    """
    assert check_for_lowercase("ABCd") == True
    assert check_for_lowercase("ABC") == False


def test_check_for_digit() -> None:
    """ 
    Test if at least one numeric digit is detected.
    """
    assert check_for_digit("abc1") == True
    assert check_for_digit("no_digits") == False


def test_check_for_special_chars() -> None:
    """ 
    Test if at least one special character is detected.
    """
    assert check_for_special_chars("abc@") == True
    assert check_for_special_chars("abc") == False
    

# --- Edge Case Tests ---

def test_empty_string_fails_all() -> None:
    """ 
    Test that an empty password input fails all rule checks.
    """
    assert check_length("") == False
    assert check_for_uppercase("") == False
    assert check_for_lowercase("") == False
    assert check_for_digit("") == False
    assert check_for_special_chars("") == False


def test_all_special_characters() -> None:
    """ 
    Test a password input made entirely of special characters.
    Should pass the special char rule but fail the others.
    """
    assert check_for_special_chars("!@#$%^&*()") == True
    assert check_for_uppercase("!@#$%^&*()") == False
    assert check_for_lowercase("!@#$%^&*()") == False
    assert check_for_digit("!@#$%^&*()") == False


def test_very_long_password() -> None:
    """ 
    Test a vary long password made of lowercase letters.
    Should pass length and lowercase check, but fail the rest.
    """
    long_password = "a" * 1000
    assert check_length(long_password) == True
    assert check_for_lowercase(long_password) == True
    assert check_for_uppercase(long_password) == False
    assert check_for_digit(long_password) == False
    assert check_for_special_chars(long_password) == False


def test_mixed_but_missing_some_rules() -> None:
    """ 
    Test inputs that satisfy some rules but miss others. 
    Validates accurate rule-by-rule evaluation.
    """
    assert check_length("12345678") == True
    assert check_for_digit("12345678") == True
    assert check_for_uppercase("12345678") == False
    assert check_for_lowercase("12345678") == False
    assert check_for_special_chars("12345678") == False

    assert check_for_uppercase("ABC123!@") == True
    assert check_for_lowercase("ABC123!@") == False
    assert check_for_digit("ABC123!@") == True
    assert check_for_special_chars("ABC123!@") == True