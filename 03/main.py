from pprint import pprint

from aocd import get_data
from dotenv import load_dotenv

with open("03/example_input.txt", "r") as infile:
    example_input = infile.read()


def parse(puzzle_input: str) -> list[list[int]]:
    """Parse input."""
    result = puzzle_input.strip().split("\n")
    result = [[int(n) for n in line] for line in result]

    # pprint(result[-3:])
    # print()
    return result


def part1(data: list[list[int]]):
    """Solve and return the answer to part 1."""
    max_joltages = []
    for bank in data:
        # Find highest digit (that isn't the last battery in the bank). Find first index of that digit in the bank.
        highest_number = max(bank[:-1])
        highest_number_index = bank.index(highest_number)

        # Find the highest digit from that index+1 until the end of the bank
        next_highest_number = max(bank[highest_number_index + 1 :])

        # Put the two numbers together and add to max_joltages
        joltage = int(str(highest_number) + str(next_highest_number))
        max_joltages.append(joltage)

    return sum(max_joltages)


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
    puzzle_input = get_data(day=3, year=2025)
    solutions = solve(puzzle_input)

    print("\n".join(str(solution) for solution in solutions))
