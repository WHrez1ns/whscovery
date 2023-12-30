import sys
from main import main

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except Exception as error:
        print(f"Usage: python whscovery.py <host>")