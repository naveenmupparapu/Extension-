# What: Adds two numbers and prints the result.
# Why: Provides a simple interactive sum of two numeric inputs.
# Reads/Writes: Reads two numeric inputs; writes the sum to stdout.
# Contracts: Caller supplies two numbers (or numeric strings); program prints their sum.
# Risks: Invalid or non-numeric input raises ValueError; no division-by-zero concern.

def main():
    a = float(input("First number: "))
    b = float(input("Second number: "))
    result = a + b
    print(result)


if __name__ == "__main__":
    main()
