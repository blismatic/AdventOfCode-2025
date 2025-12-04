import math
from pprint import pprint

from aocd import get_data
from dotenv import load_dotenv

with open("02/example_input.txt", "r") as infile:
    example_input = infile.read()

"""
The product ID ranges are inclusive, meaning a range of 11-99 *includes* 11 and 99.
"""


def get_factors(n: int) -> list[int]:
    result = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)

    return sorted(result)


def generate_n_len_digits(n: int):
    start = 10 ** (n - 1)
    end = 10**n
    for i in range(start, end):
        yield i


def parse(puzzle_input: str) -> list[tuple[int, int]]:
    """Parse input."""
    result = puzzle_input.strip().split(",")
    result = [tuple(map(int, id_range.split("-"))) for id_range in result]

    # pprint(result[-3:])
    # print()
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


def part2(data: list[tuple[int, int]]) -> int:
    """Solve and return the answer to part 2."""
    invalid_ids = set()

    for start, stop in data:
        start_len = len(str(start))
        stop_len = len(str(stop))

        # Construct sub-ranges of similar length numbers: e.g. 1-9, 10-00, 100-999, 1_000-9_000, etc...
        # but have it clamped to the overall start and stop ranges
        for digit_len in range(start_len, stop_len + 1):
            # Get all the factors of the digit length, besides the digit length itself
            factors = [f for f in get_factors(digit_len) if f != digit_len]

            # Generate every possible number with a length = factor
            for f in factors:
                n_digit_numbers = generate_n_len_digits(f)

                for n in n_digit_numbers:
                    # Repeat each number, and add it to the set of invalid_ids if it is within the boundary.
                    # Stop processing if the number gets greater than the end of the original range.
                    repeated_num = int(str(n) * (digit_len // f))
                    if start <= repeated_num <= stop:
                        invalid_ids.add(repeated_num)
                    elif repeated_num > stop:
                        break

    return sum(invalid_ids)


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
