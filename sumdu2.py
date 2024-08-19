import time
import sys
import os

def effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    numbers = [1, 3, 5, 9, 17]

    effect(f"{'Number':<10}{'Square':<10}{'Cube':<10}")
    effect("-" * 30)

    for number in numbers:
        square = number ** 2
        cube = number ** 3
        effect(f"{number:<10}{square:<10}{cube:<10}")

if __name__ == "__main__":
    main()
