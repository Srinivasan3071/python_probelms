import logging
# Basic configuration
logging.basicConfig(level=logging.DEBUG)
def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero")
        return None
    logging.info(f"Division result: {result}")
    return result
divide(10, 2)  # Successful division
divide(10, 0)  # Division by zero
