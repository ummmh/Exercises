""" Converting Celsius to Fahrenheit v1
Converting from degrees celsius to fahrenheit
Function takes in a value, does the conversion and put answer into a list
"""


def to_f(from_c):
    fahrenheit = (from_c * 9 / 5) + 32
    return fahrenheit


# Main routine
temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_f(item)
    ans_statement = f"{item}° Celsius is {answer}° Fahrenheit"
    converted.append(ans_statement)

for item in converted:
    print(item)
