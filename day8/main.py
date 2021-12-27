from dataclasses import dataclass, field
from typing import List
from collections import defaultdict

"""
Notes:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

0: 6 (ABCEFG)
1: 2 (CF)
2: 5 (ACDEG)
3: 5 (ACDFG)
4: 4 (BCFF)
5: 5 (ABDFG)
6: 6 (ABDEFG)
7: 3 (ACF)
8: 7 (all)
9: 6 (ABCDFG)

Or in table format:
|   | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 0 | X | X | X |   | X | X | X |
| 1 |   |   | X |   |   | X |   |
| 2 | X |   | X | X | X |   | X |
| 3 | X |   | X | X |   | X | X |
| 4 |   | X | X | X |   | X |   |
| 5 | X | X |   | X |   | X | X |
| 6 | X | X |   | X | X | X | X |
| 7 | X |   | X |   |   | X |   |
| 8 | X | X | X | X | X | X | X |
| 9 | X | X | X | X |   | X | X |

so from the length you can find:
1
4
7
8

if you know 1:
3
(2,5 dont have segment C)
if you know 4:
9
if you know 1 and 9
6 and 0

if you know 3 or 6:
two and 5

"""
SEGMENTS = {
    0: "ABCEFG",
    1: "CF",
    2: "ACDEG",
    3: "ACDFG",
    4: "BCDF",
    5: "ABDFG",
    6: "ABDEFG",
    7: "ACF",
    8: "all",
    9: "ABCDFG",
}


@dataclass
class Entry:
    signal_pattern: List[str] = field(default_factory=list)
    output: List[str] = field(default_factory=list)


def create_entries(line: str) -> Entry:
    elements = line.split("|")
    signal = elements[0].strip().split(" ")
    output = elements[1].strip().split(" ")

    return Entry(signal, output)


def find_easy_digits(entry: Entry) -> int:
    """count the occurence of 1,4,7 and 8"""

    total = 0
    for digit in entry.output:
        if len(digit) in [2, 3, 4, 7]:
            total += 1
    return total


def read_input(file_path="day8/input/input.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()
        lines = [create_entries(x) for x in lines]

    return lines


def get_signal_by_len(signals, length):
    return list(filter(lambda sig: len(sig) == length, signals))


def filter_signal_by_subsignal(signals, subsig):
    new_sig = []
    rejects = []
    subsig = set([x for x in subsig])
    for sig in signals:
        results = []
        for sub in subsig:
            if sub in sig:
                results.append(True)
            else:
                results.append(False)
        if all(results):
            new_sig.append(sig)
        else:
            rejects.append(sig)
    return new_sig, rejects 

def get_zero(signal, one, nine):
    for sig in signal:
        if len(sig) == 6:
            if set(sig) == set(nine):
                continue
            if set(one).issubset(set(sig)):
                return sig


def get_six(signal, one, nine):
    for sig in signal:
        if len(sig) == 6:
            if set(sig) == set(nine):
                continue
            if not set(one).issubset(set(sig)):
                return sig


def get_two(signal, three, six):
    for sig in signal:
        if len(sig) == 5:
            if set(sig) == set(three):
                continue
            if not set(sig).issubset(set(six)):
                return sig


def get_five(signal, three, six):
    for sig in signal:
        if len(sig) == 5:
            if set(sig) == set(three):
                continue
            if set(sig).issubset(set(six)):
                return sig


def solve(entry):

    sig_1 = get_signal_by_len(entry.signal_pattern, 2)[0]
    sig_7 = get_signal_by_len(entry.signal_pattern, 3)[0]
    sig_4 = get_signal_by_len(entry.signal_pattern, 4)[0]
    sig_8 = 'abcdefg'

    pos_three, no_three = filter_signal_by_subsignal(entry.signal_pattern, sig_1)

    sig_3 = get_signal_by_len(pos_three, 5)[0]

    pos_nine, no_nine = filter_signal_by_subsignal(entry.signal_pattern, sig_4)
    sig_9 = get_signal_by_len(pos_nine, 6)[0]

    # 0 or 6
    sig_0 = get_zero(entry.signal_pattern, sig_1, sig_9)
    sig_6 = get_six(entry.signal_pattern, sig_1, sig_9)

    # two and five

    sig_2 = get_two(entry.signal_pattern, sig_1, sig_9)
    sig_5 = get_five(entry.signal_pattern, sig_1, sig_9)

    # ugly alpha sort, to normalize the signal
    sig_0 = ''.join(sorted(sig_0))
    sig_1 = ''.join(sorted(sig_1))
    sig_2 = ''.join(sorted(sig_2))
    sig_3 = ''.join(sorted(sig_3))
    sig_4 = ''.join(sorted(sig_4))
    sig_5 = ''.join(sorted(sig_5))
    sig_6 = ''.join(sorted(sig_6))
    sig_7 = ''.join(sorted(sig_7))
    sig_8 = ''.join(sorted(sig_8))
    sig_9 = ''.join(sorted(sig_9))


    translator = {
        sig_0: '0',
        sig_1: '1',
        sig_2: '2',
        sig_3: '3',
        sig_4: '4',
        sig_5: '5',
        sig_6: '6',
        sig_7: '7',
        sig_8: '8',
        sig_9: '9'
    }
    result = [translator[''.join(sorted(x))] for x in entry.output]
    result = int(''.join(result))
    return result


def main1():
    signal = read_input("day8/input/example.txt")
    easy_digits = [find_easy_digits(x) for x in signal]
    print(sum(easy_digits))

    signal = read_input("day8/input/input.txt")
    easy_digits = [find_easy_digits(x) for x in signal]
    print(sum(easy_digits))
    print("done")


def main2():
    signal = read_input("day8/input/example.txt")

    solution = 0
    for entry in signal:
        solve_signal = solve(entry)
        solution += solve_signal
    print(solution)

if __name__ == "__main__":
    # main1()
    main2()
