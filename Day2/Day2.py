import re

with open("input.txt", 'r') as file:
    lines = file.readlines()


max_counts = {"red": 12, "green": 13, "blue": 14}
total = 0
for line in lines:
    valid = True
    game = int(line.split(": ")[0].split(" ")[1].strip())
    cubes = re.split(',|;',line.split(": ")[1])

    for s in cubes:
        s = s.strip()
        number = s.split(" ")[0].strip();
        color = s.split(" ")[1].strip();
        if int(number) > max_counts[color]:
            valid = False
            break;

    if valid:
        total += game

print(total)