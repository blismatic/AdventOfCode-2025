from pprint import pprint

from aocd import get_data
from dotenv import load_dotenv

with open("02/example_input.txt", "r") as infile:
    example_input = infile.read()

"""
The product ID ranges are inclusive, meaning a range of 11-99 *includes* 11 and 99.
"""


def parse(puzzle_input: str) -> list[tuple[int, int]]:
    """Parse input."""
    result = puzzle_input.strip().split(",")
    result = [tuple(map(int, id_range.split("-"))) for id_range in result]

    pprint(result[-3:])
    print()
    return result


def part1(data: list[tuple[int, int]]) -> int:
    """Solve and return the answer to part 1.
    An invalid ID is any number consisting of a sequence of digits repeated twice
    (e.g. 55, 6464, 123123)
    """
    invalid_ids = set()

    for start, stop in data:
        start_len = len(str(start))
        stop_len = len(str(stop))

        # Construct sub-ranges of similar length numbers: e.g. 1-9, 10-99, 100-999, 1_000-9_999, etc...
        # but have it clamped to the overall start and stop ranges
        for i in range(start_len, stop_len + 1):
            if i % 2 == 1:
                continue  # Skip any odd length range groups since there can be no invalid IDs in these subranges

            subrange_start = max(start, 10 ** (i - 1))
            subrange_end = min(stop, 10**i - 1)

            # Take the first half of subrange_start and subrange_end: e.g. 2_877 - 9_999 => 28-99
            half = i // 2
            subrange_start_first_half = int(str(subrange_start)[:half])
            subrange_end_first_half = int(str(subrange_end)[:half])

            # Make a new range of each number in this "first half subrange" range
            for partial_num in range(subrange_start_first_half, subrange_end_first_half + 1):
                repeated = int(str(partial_num) * 2)
                if subrange_start <= repeated <= subrange_end:
                    invalid_ids.add(repeated)

    return sum(invalid_ids)


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
    puzzle_input = get_data(day=2, year=2025)
    solutions = solve(puzzle_input)

    print("\n".join(str(solution) for solution in solutions))
