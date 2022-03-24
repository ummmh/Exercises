# Display output using rounding for floats only

to_round = [1/1, 1/2, 1/3]
print("***** NUMBERS TO ROUND *****")
print(to_round)

print()
print("***** ROUNDED NUMBERS *****")

for item in to_round:
    if item.is_integer():
        print(f"{item:.0f}")
    else:
        print(f"{int(item):.1f}")
