import math
from pprint import pprint

from aocd import get_data
from dotenv import load_dotenv

with open("04/example_input.txt", "r") as infile:
    example_input = infile.read()


NEIGHBORS = (
    -1j,  # N
    -1j + 1,  # NE
    1,  # E
    1 + 1j,  # SE
    1j,  # S
    1j - 1,  # SW
    -1,  # W
    -1 - 1j,  # NW
)


def parse(puzzle_input: str) -> set[complex]:
    """Parse input.

    Coordinates are represented by complex numbers in the form x+yi.
    The imaginary number i is represented as 1j in Python.

    The top left of the grid is treated as coordinate 0+0j
    x coordinates (real part) increase as you move to the right
    y coordinates (imaginary part) increase as you move down
    """
    ROLL_OF_PAPER = "@"
    result = set()

    grid = puzzle_input.strip().split("\n")

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == ROLL_OF_PAPER:
                coordinate = x + y * 1j
                result.add(coordinate)

    # pprint(grid[-3:])
    # print()
    return result


def is_accessible(roll_of_paper: complex, data: set[complex]) -> bool:
    neighbor_count = 0
    for n in NEIGHBORS:
        if roll_of_paper + n in data:
            neighbor_count += 1

    return True if neighbor_count < 4 else False


def part1(data: set[complex]) -> int:
    """Solve and return the answer to part 1."""

    accessible = 0

    for roll_of_paper in data:
        if is_accessible(roll_of_paper, data):
            accessible += 1

    return accessible


def part2(data: set[complex]) -> int:
    """Solve and return the answer to part 2."""
    total_removed = 0
    removed = math.inf

    while removed > 0:
        removed = 0
        temp_data = data.copy()

        for roll_of_paper in data:
            if is_accessible(roll_of_paper, data):
                removed += 1
                temp_data.remove(roll_of_paper)

        data = temp_data
        total_removed += removed

    return total_removed


def solve(puzzle_input) -> tuple:
    """Solve the puzzle for the given input. Returns a tuple containing the answers to part 1 and part 2."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    load_dotenv()
    # solutions = solve(example_input)
    puzzle_input = get_data(day=4, year=2025)
    solutions = solve(puzzle_input)

    print("\n".join(str(solution) for solution in solutions))
