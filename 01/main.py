from pprint import pprint

from aocd import get_data
from dotenv import load_dotenv

with open("01/example_input.txt", "r") as infile:
    example_input = infile.read()


def parse(puzzle_input: str):
    """Parse input."""
    result = puzzle_input.split("\n")

    pprint(result[-3:])
    print()
    return result


def part1(data: list[str]) -> int:
    """Solve and return the answer to part 1."""
    safe = list(range(100))  # [0, 1, ... 98, 99]
    dial_index = 50
    num_of_zeroes = 0

    for rotation in data:
        direction = rotation[0]
        distance = int(rotation[1:])

        dial_index += distance if direction == "R" else -distance
        dial_position = safe[dial_index % 100]
        if dial_position == 0:
            num_of_zeroes += 1

    return num_of_zeroes


def part2(data):
    """Solve and return the answer to part 2."""
    safe = list(range(100))  # [0, 1, ... 98, 99]
    dial_index = 50
    num_of_zeroes = 0

    for rotation in data:
        direction = rotation[0]
        distance = int(rotation[1:])

        for _ in range(distance):
            dial_index += 1 if direction == "R" else -1
            dial_position = safe[dial_index % 100]

            if dial_position == 0:
                num_of_zeroes += 1

    return num_of_zeroes


def solve(puzzle_input) -> tuple:
    """Solve the puzzle for the given input. Returns a tuple containing the answers to part 1 and part 2."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    load_dotenv()
    # solutions = solve(example_input)
    puzzle_input = get_data(day=1, year=2025)
    solutions = solve(puzzle_input)

    print("\n".join(str(solution) for solution in solutions))
