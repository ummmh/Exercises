""" Converting Fahrenheit to Celsius v1
Converting from degrees fahrenheit to celsius
Function takes in a value, does the conversion and put answer into a list
"""


def to_c(from_f):
    celsius = (from_f - 32) * 5/9
    return celsius


# Main routine
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = f"{item}° Fahrenheit is {answer}° Celsius"
    converted.append(ans_statement)

for item in converted:
    print(item)
