measurements = []


def read_input():
    file = open("input.in", 'r')

    for line in file.readlines():
        measurements.append(int(line))

    return measurements


def count_windows():
    counter = 0

    for i, number in enumerate(measurements):
        sum_fst_window = sum(measurements[i:i+3])
        sum_snd_window = sum(measurements[i+1:i+4])

        if sum_snd_window > sum_fst_window:
            counter += 1

    return counter


def main():
    read_input()
    print(count_windows())


main()
