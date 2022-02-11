"""Program that asks for finishing times of a 200m race, and outputs all the
times entered, fastest time, and the average time.
Created by Janna Lei Eugenio
11/02/2022
"""

# variables
race_times = []
race_time = ""

while True:
    race_time = float(input("Enter finishing time: "))
    if race_time == -1:
        break
    race_times.append(race_time)

# prints all the scores
print("\nRace times entered:")
for race_time in race_times:
    print(race_time)
print()

# sorts list from shortest time to longest
race_times.sort()
# calculates the average
average_time = sum(race_times) / len(race_times)

# print output
print(f"The fastest time was {race_times[0]}")
print(f"The average time was {average_time}")
