import logging

# Basic logging for SRE concept
logging.basicConfig(level=logging.INFO)

def add(a, b):
    logging.info(f"Performing addition for {a} and {b}")
    return a + b

if __name__ == "__main__":
    print(add(2, 3))