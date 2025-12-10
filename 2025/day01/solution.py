#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 1: Secret Entrance

PART ONE:
The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn the dial, it makes a small click noise as it reaches each number.
The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe.
A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers).
Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.
So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0.
Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.
So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.
The dial starts by pointing at 50.
You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy.
The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.

PART TWO:
As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

"Due to newer security protocols, please use password method 0x434C49434B until further notice."

You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0,
regardless of whether it happens during a rotation or at the end of one.

Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!
"""

import sys
from pathlib import Path

# Add parent directory to path to import utility
sys.path.append(str(Path(__file__).parent.parent.parent))
from utility import *


def parse_rotations(data: list[str]):
    """Parse rotation instructions into (direction, distance) tuples."""
    return [(line[0], int(line[1:])) for line in data]


@timeit
def part1(data: list[str]) -> int:
    """Solve Part 1 of the puzzle."""
    result = 0
    tracking_position = 50
    rotations = parse_rotations(data)

    for direction, distance in rotations:
        if direction == 'L':
            tracking_position = (tracking_position - distance) % 100
        elif direction == 'R':
            tracking_position = (tracking_position + distance) % 100

        if tracking_position == 0:
            result += 1

    return result
@timeit
def part2(data: list[str]) -> int:
    """Solve Part 2 of the puzzle."""
    result = 0
    tracking_position = 50
    rotations = parse_rotations(data)

    for direction, distance in rotations:
        if direction == 'R':
            for k in range(1, distance + 1):
                if (tracking_position + k) % 100 == 0:
                    result += 1
            tracking_position = (tracking_position + distance) % 100
        elif direction == 'L':
            for k in range(1, distance + 1):
                if (tracking_position - k) % 100 == 0:
                    result += 1
            tracking_position = (tracking_position - distance) % 100

    return result

def main():
    # Read input file
    input_file = Path(__file__).parent / "input.txt"
    data = read_lines(str(input_file))

    # Test with example if available
    example = [ "L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82" ]

    if example and len(example) > 0:
        print("=== Testing with example ===")
        run_test(part1, example, 3, "Part 1")
        run_test(part2, example, 6, "Part 2")

    # Solve actual puzzle
    print("\n=== Part 1 ===")
    answer1 = part1(data)
    print(f"Answer: {answer1}")

    print("\n=== Part 2 ===")
    answer2 = part2(data)
    print(f"Answer: {answer2}")


if __name__ == "__main__":
    main()
