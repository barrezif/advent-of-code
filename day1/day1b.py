with open("day1.txt") as fp:
    lines = [int(line) for line in fp.readlines()]
    curr_window = [lines[0], lines[1], lines[2]]
    count = 0

    for line in lines[3:]:
        new_window = curr_window[1:] + [line]
        curr_sum = curr_window[0] + curr_window[1] + curr_window[2]
        new_sum = new_window[0] + new_window[1] + new_window[2]
        curr_window = new_window

        if new_sum > curr_sum:
            count += 1

    print(count)