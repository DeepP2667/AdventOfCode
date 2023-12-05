with open("input.txt", 'r') as file:
    lines = file.readlines()

# PART 1
total_calibration = 0
for line in lines:
    # Digits
    first = -1
    second = -1

    # Pointers
    start = 0
    end = len(line) - 1

    while end != -1:
        if first == -1 and line[start].isdigit():
            first = int(line[start])
        if second == -1 and line[end].isdigit():
            second = int(line[end])
        start += 1
        end -= 1
    total_calibration += first * 10 + second


# PART 2
starts = {"t": {"two", "three"}, "o": {"one"}, "f": {"four", "five"}, "s": {"six", "seven"}, "e": {"eight"}, "n":{"nine"}}
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def check_number(line, start_index):
    char = line[start_index]
    if char in starts:
        n = starts[char]
        for num in n:
            if line[start_index:start_index+len(num)] == num:
                return numbers[num]
    return -1

total_calibration = 0
for line in lines:
    first = -1
    second = -1

    # Pointers
    start = 0
    end = len(line) - 1

    while end != -1:
        if first == -1:
            char = line[start]
            if char.isdigit():
                first = int(line[start])
            else:
                first = check_number(line, start)
                
        if second == -1:
            char = line[end]
            if line[end].isdigit():
                second = int(line[end])
            else:
                second = check_number(line, end)
            
        start += 1
        end -= 1
    total_calibration += first * 10 + second

print(total_calibration)