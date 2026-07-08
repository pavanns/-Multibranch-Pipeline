# app.py
"""
Simple sample script to verify the Jenkins multibranch pipeline
is correctly checking out code and executing build/test steps.
"""

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def greet(name):
    return f"Hello, {name}! This build ran successfully done."

if __name__ == "__main__":
    print(greet("Jenkins"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")
