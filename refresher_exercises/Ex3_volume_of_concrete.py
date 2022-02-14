# Program to calculate the volume of concrete needed for each job
# 8/02/2022

commercial = 0.5
residential = 0.25

depth = 0
length = 0
width = 0

total_volume = []

while True:
    build_type = input("Enter building type (commercial or residential): ")\
        .lower()
    if build_type == "commercial":
        depth = commercial
    elif build_type == "residential":
        depth = commercial
    elif build_type == "x":
        break
    else:
        print("Please select one of the two options\n")
        continue
    
    while True:
        try:
            length = float(input("Enter length (in m): "))
            width = float(input("Enter width (in m): "))
        except ValueError:
            print("Please input a valid number")
            continue
        break

    volume = length * width * depth
    total_volume.append(volume)

    print(f"\nThe volume of concrete required for slab with a length of "
          f"{length}m and width of {width}m and a depth of {depth}m is "
          f"{volume} cubic metres.\n")

volume_sum = sum(total_volume)
print(f"\nTotal amount of volume needed: {volume_sum} cubic metres")
