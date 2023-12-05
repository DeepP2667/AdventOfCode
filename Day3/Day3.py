with open("input.txt", 'r') as file:
    lines = file.readlines()

def find_number(line, index, numbers_found):
    numbers = []
    numbers.append(line[index])
    left = index - 1
    right = index + 1

    while left != -1 or right != -1:
        if left == -1 or not line[left].isdigit():
            left = -1
        if right == -1 or not line[right].isdigit() or right >= len(line):
            right = -1

        if (right != -1):       
            numbers.append(line[right])
            right += 1
        if (left != -1):
            numbers.insert(0, line[left])
            left -= 1

    number = int("".join(numbers))
    if number not in numbers_found:
        numbers_found.add(number)
        return number
    return 0

def add_to_max(m, num):
    if num != 0:
        m.append(num)

total = 0
part2_total = 0
for row, line in enumerate(lines):
    for i, char in enumerate(line.strip()):
        numbers_found_max = []
        if char.isdigit() or char == ".":
            continue
        else:
            # Get top 3, left, right, bottom 3
            # Top 3: row - 1, i, i-1, i+1
            if row > 0:
                numbers_found = set()
                top_line = lines[row - 1]           
                if top_line[i].isdigit():
                    number = find_number(top_line, i, numbers_found)
                    total += number
                    add_to_max(numbers_found_max, number)
                if i > 0 and top_line[i-1].isdigit():
                    number = find_number(top_line, i-1, numbers_found)
                    total += number
                    add_to_max(numbers_found_max, number)
                if i < len(top_line) - 1 and top_line[i+1].isdigit():
                    number = find_number(top_line, i+1, numbers_found)
                    total += number
                    add_to_max(numbers_found_max, number)
            # Bottom 3: row + 1, i, i-1, i+1
            if row < len(lines) - 1:
                numbers_found = set()
                bottom_line = lines[row + 1]     
                if bottom_line[i].isdigit():
                    number = find_number(bottom_line, i, numbers_found)
                    total += number
                    add_to_max(numbers_found_max, number)
                if i > 0 and bottom_line[i-1].isdigit():
                    number = find_number(bottom_line, i-1, numbers_found)
                    total += number
                    add_to_max(numbers_found_max, number)
                if i < len(bottom_line) - 1 and bottom_line[i+1].isdigit():
                    number = find_number(bottom_line, i+1, numbers_found)
                    total += number
                    add_to_max(numbers_found_max, number)
            # Left and right : row, i-1, i+1
            if i > 0:
                if line[i-1].isdigit():
                    number = find_number(line, i-1, numbers_found)
                    total += number
                    add_to_max(numbers_found_max, number)
            if i < len(line) - 1:
                if line[i+1].isdigit():
                    number = find_number(line, i+1, numbers_found)
                    total += number
                    add_to_max(numbers_found_max, number)

            if len(numbers_found_max) == 2:
                part2_total += numbers_found_max[0] * numbers_found_max[1]

print(total)
print(part2_total)