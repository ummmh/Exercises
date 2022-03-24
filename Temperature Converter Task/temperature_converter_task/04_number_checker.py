# Code to check that a number is valid

def temp_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a number: "))
            if response < low:
                print("Too cold!")
            else:
                return response

        except ValueError:
            print("Please enter a number")


# Main routine
# Set up to run this code twice (for two valid responses in test plan)
number = temp_check(-273)  # Celsius
print(f"You entered {number}")

number = temp_check(-459)  # Fahrenheit
print(f"You entered {number}")
