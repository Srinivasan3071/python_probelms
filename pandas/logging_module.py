import logging

logging.basicConfig(level=logging.DEBUG)

def add(a, b):
    logging.debug(f"Adding {a} and {b}")
    return a + b

result = add(1, 2)
logging.info(f"Result: {result}")
