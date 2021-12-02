from collections import defaultdict


def read_input(file_path="input/input.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
    return lines


def get_solution1(
    submarine_motions, forwards_cmd="forward", down_cmd="down", up_cmd="up"
):
    total_motion = defaultdict(int)

    for motion in submarine_motions:
        direction, value = motion.split(" ")
        total_motion[direction] += int(value)

    forwards_motion = total_motion[forwards_cmd]
    downwards_motion = total_motion[down_cmd] - total_motion[up_cmd]
    print(f"solution1: {forwards_motion*downwards_motion}")


def get_solution2(submarine_motions):

    total_motion = defaultdict(int)

    for motion in submarine_motions:
        direction, value = motion.split(" ")
        value = int(value)
        
        if direction == "down":
            total_motion["aim"] += value
        elif direction == "up":
            total_motion["aim"] -= value

        elif direction == "forward":
            total_motion["horizontal"] += value
            total_motion["depth"] += value * total_motion["aim"]

    print(f"solution2: {total_motion['horizontal'] * total_motion['depth']}")


def main():
    sub_directions = read_input()

    get_solution1(sub_directions)
    get_solution2(sub_directions)


if __name__ == "__main__":
    main()
