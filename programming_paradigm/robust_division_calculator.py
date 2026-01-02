def safe_divide(numerator, denominator):
    """
    Performs division with robust error handling.
    
    Args:
        numerator (str or float): The numerator value
        denominator (str or float): The denominator value

    Returns:
        str: Result of division or error message
    """
    try:
        # Convert to float
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
