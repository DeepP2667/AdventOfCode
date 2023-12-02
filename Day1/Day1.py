with open("input.txt", 'r') as file:
    lines = file.readlines()


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
    
print(total_calibration)