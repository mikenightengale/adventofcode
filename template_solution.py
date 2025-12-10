#!/usr/bin/env python3
"""
Advent of Code 2025 - Day X: [Puzzle Title]
Solution template showing utility usage
"""

import sys
from pathlib import Path

# Add parent directory to path to import utility
sys.path.append(str(Path(__file__).parent.parent.parent))
from utility import *


def parse_input(data: list[str]):
    """Parse the input data into a useful format."""
    # Example: Parse numbers from each line
    # return [parse_numbers(line) for line in data]
    pass


@timeit
def part1(data: list[str]) -> int:
    """Solve Part 1 of the puzzle."""
    parsed = parse_input(data)
    
    # Your solution here
    result = 0
    
    return result


@timeit
def part2(data: list[str]) -> int:
    """Solve Part 2 of the puzzle."""
    parsed = parse_input(data)
    
    # Your solution here
    result = 0
    
    return result


def main():
    # Read input file
    input_file = Path(__file__).parent / "input.txt"
    data = read_lines(str(input_file))
    
    # Test with example if available
    example = [
        # Add example input here
    ]
    
    if example:
        print("=== Testing with example ===")
        expected_result = 0  # Set this to the correct expected result for the example
        run_test(part1, example, expected_result, "Part 1 Example")
        # run_test(part2, example, expected_result, "Part 2 Example")
    
    # Solve actual puzzle
    print("\n=== Part 1 ===")
    answer1 = part1(data)
    print(f"Answer: {answer1}")
    
    print("\n=== Part 2 ===")
    answer2 = part2(data)
    print(f"Answer: {answer2}")


if __name__ == "__main__":
    main()
