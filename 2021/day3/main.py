import numpy as np


def read_input(file_path="input/input.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
    return lines


def get_solution1(raw_diag):
    """find the most and least occuring bit in a list of list of bits"""
    matrix = np.zeros((len(raw_diag), len(raw_diag[0])))
    for i, bits in enumerate(raw_diag):
        for j, bit in enumerate(bits):
            if bit == "1":
                matrix[i][j] = 1
    matrix = matrix.T

    gamma = ""
    epsilon = ""
    for row in matrix:
        ratio = np.sum(row) / len(row)
        if ratio > 0.5:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    gamma_int = int(gamma, 2)
    epsilon_int = int(epsilon, 2)
    print(f"solution1: {gamma_int*epsilon_int}")


def get_rating(raw_diag, target_func):

    relevant_observations = raw_diag
    for i in range(len(raw_diag[0])):
        obs_sum = sum([int(obs[i]) for obs in relevant_observations])
        ratio = obs_sum / len(relevant_observations)

        target = target_func(ratio)
        new_relevant_observations = []
        for obs in relevant_observations:
            if obs[i] == target:
                new_relevant_observations.append(obs)
        relevant_observations = new_relevant_observations

        if len(relevant_observations) == 1:
            return int(relevant_observations[0], 2)


def get_co2_target(ratio):
    if ratio >= 0.5:
        target = "0"
    else:
        target = "1"
    return target


def get_oxygen_target(ratio):
    if ratio < 0.5:
        target = "0"
    else:
        target = "1"
    return target


def get_solution2(raw_diag):
    """The diff between oxygen and co2 is how we define the target number for each location in the binary num.
    We use that to pass a general function a target getter.
    """
    target_func = get_oxygen_target
    oxygen_rating = get_rating(raw_diag, target_func)

    target_func = get_co2_target
    co2_scrub_rating = get_rating(raw_diag, target_func)
    print(f"solution2: {oxygen_rating*co2_scrub_rating}")


def main():
    raw_diagnostics = read_input()

    get_solution1(raw_diagnostics)
    get_solution2(raw_diagnostics)


if __name__ == "__main__":
    main()
