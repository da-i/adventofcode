from typing import Counter

def read_input(file_path="day6/input/input.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]

    return lines


def clean_input(input):
    input = input[0]
    input = input.split(",")
    input = [int(x) for x in input]
    return input


def update_fish(fish):
    for i, repro in enumerate(fish):
        if repro == 0:
            fish[i] = 7
            fish.append(9)

    fish = [x - 1 for x in fish]
    return fish


def fish_dict(fish):
    """"Use a dict to track number of fish at each dev stage"""
    next_fish = {}
    update = 0
    for k, v in fish.items():
        if k == 0:
            update = v
        else:
            next_fish[k - 1] = v

    if update:
        if 6 in next_fish.keys():
            next_fish[6] += update
            next_fish[8] = update
        else:
            next_fish[6] = update
            next_fish[8] = update

    return next_fish


def main():
    # input = read_input("day6/input/test_input.txt")
    input = read_input()

    fish = clean_input(input)
    for i in range(80):
        fish = update_fish(fish)
    print(len(fish))

    ### PART 2: Use a dict
    # input = read_input("day6/input/test_input.txt")
    input = read_input()
    fish = clean_input(input)
    fish = Counter(fish)
    for i in range(256):
        fish = fish_dict(fish)

    print(sum(fish.values()))


if __name__ == "__main__":
    main()
