# my_script.py
import sys

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name_to_greet = sys.argv[1]
        greet(name_to_greet)
    else:
        print("Hello there!")
