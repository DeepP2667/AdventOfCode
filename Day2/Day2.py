import re

with open("input.txt", 'r') as file:
    lines = file.readlines()

# PART 1

counts = {"red": 12, "green": 13, "blue": 14}
max_counts = {"red": 0, "green": 0, "blue": 0}
total = 0

for line in lines:
    valid = True
    game = int(line.split(": ")[0].split(" ")[1].strip())
    cubes = re.split(',|;',line.split(": ")[1])

    for s in cubes:
        s = s.strip()
        number = s.split(" ")[0].strip();
        color = s.split(" ")[1].strip();
        if int(number) > counts[color]:
            valid = False
            break;

    if valid:
        total += game

print(total)

# PART 2
max_counts = {"red": 0, "green": 0, "blue": 0}
total = 0
for line in lines:
    max_counts = {"red": 0, "green": 0, "blue": 0}

    game = int(line.split(": ")[0].split(" ")[1].strip())
    cubes = re.split(',|;',line.split(": ")[1])

    for s in cubes:
        s = s.strip()
        number = s.split(" ")[0].strip();
        color = s.split(" ")[1].strip();
        max_counts[color] = max(max_counts[color], int(number))

    total += max_counts["red"] * max_counts["blue"] * max_counts["green"]

print(total)