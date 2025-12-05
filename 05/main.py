from pprint import pprint

from aocd import get_data
from dotenv import load_dotenv

with open("05/example_input.txt", "r") as infile:
    example_input = infile.read()


def parse(puzzle_input: str) -> tuple[list[tuple[int, int]], list[int]]:
    """Parse input."""
    fresh_ingredient_id_ranges, available_ingredient_ids = puzzle_input.strip().split("\n\n")

    fresh_ingredient_id_ranges = [tuple(map(int, x.split("-"))) for x in fresh_ingredient_id_ranges.splitlines()]
    available_ingredient_ids = [int(x) for x in available_ingredient_ids.splitlines()]

    return (fresh_ingredient_id_ranges, available_ingredient_ids)


def part1(data: tuple[list[tuple[int, int]], list[int]]) -> int:
    """Solve and return the answer to part 1.
    ID ranges are inclusive.
    An ingredient is considered fresh if it is found in any of the ranges.
    """
    fresh_ingredient_id_ranges, available_ingredient_ids = data

    fresh_count = 0

    for ingredient in available_ingredient_ids:
        fresh = False

        for start, end in fresh_ingredient_id_ranges:
            _range = range(start, end + 1)  # Add one to end to make sure that `end` is actually included
            if ingredient in _range:
                fresh = True
                break

        if fresh:
            fresh_count += 1

    return fresh_count


def part2(data):
    """Solve and return the answer to part 2."""
    pass


def solve(puzzle_input) -> tuple:
    """Solve the puzzle for the given input. Returns a tuple containing the answers to part 1 and part 2."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    load_dotenv()
    # solutions = solve(example_input)
    puzzle_input = get_data(day=5, year=2025)
    solutions = solve(puzzle_input)

    print("\n".join(str(solution) for solution in solutions))
