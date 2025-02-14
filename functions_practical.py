# Function with parameter and return value
def add(a, b):
    return a + b


# Function with parameter and no return value
def print_sum(a, b):
    print(f"The sum of {a} and {b} is {a + b}")


# Function without parameter and with return value
def get_greeting():
    return "Hello, World!"


# Function without parameter and no return value
def print_greeting():
    print("Hello, World!")


# Example usage
if __name__ == "__main__":
    result = add(5, 3)
    print(f"Result of add function: {result}")

    print_sum(5, 3)

    greeting = get_greeting()
    print(f"Greeting from get_greeting function: {greeting}")

    print_greeting()
