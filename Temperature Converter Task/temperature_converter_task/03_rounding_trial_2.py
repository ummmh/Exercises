# Display output using int/float

to_round = [1/1, 1/2, 1/3]
print("***** NUMBERS TO ROUND *****")
print(to_round)

print()
print("***** ROUNDED NUMBERS *****")

for item in to_round:
    if item % 1 == 0:
        print(f"{item:.0f}")
    else:
        print(f"{item:.1f}")
