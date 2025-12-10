#!/usr/bin/env python3
"""
Advent of Code 2025 - Example: Using Utility Functions
This example demonstrates common utility function usage patterns.
"""

import sys
from pathlib import Path

# Add parent directory to path to import utility
sys.path.append(str(Path(__file__).parent.parent))
from utility import *


def example_file_reading():
    """Demonstrate different ways to read input files."""
    print("=== File Reading Examples ===\n")
    
    # Read as single string
    content = read_input("2025/Day 1/input.txt")
    print(f"Read {len(content)} characters")
    
    # Read as lines
    lines = read_lines("2025/Day 1/input.txt")
    print(f"Read {len(lines)} lines")
    
    # Read as grid (for 2D puzzles)
    # grid = read_grid("input.txt")
    # print(f"Grid size: {len(grid)}x{len(grid[0])}")


def example_parsing():
    """Demonstrate parsing utilities."""
    print("\n=== Parsing Examples ===\n")
    
    text = "The answer is 42, not -17 or 99"
    numbers = parse_numbers(text)
    print(f"Numbers extracted: {numbers}")  # [42, -17, 99]
    
    text = "Hello world from Python"
    words = parse_words(text)
    print(f"Words extracted: {words}")  # ['Hello', 'world', 'from', 'Python']


def example_grid_operations():
    """Demonstrate grid and coordinate utilities."""
    print("\n=== Grid Operations ===\n")
    
    # Create a simple grid
    grid = [
        ['#', '.', '.', '#'],
        ['.', 'S', '.', '.'],
        ['#', '.', 'E', '.'],
        ['.', '.', '.', '#']
    ]
    
    print("Grid:")
    print_grid(grid)
    
    # Find positions
    start = find_in_grid(grid, 'S')
    end = find_in_grid(grid, 'E')
    print(f"\nStart: {start}")
    print(f"End: {end}")
    
    # Work with coordinates
    print(f"\nManhattan distance: {start.manhattan_distance(end)}")
    
    # Get neighbors
    neighbors = start.neighbors4()
    print(f"\n4 neighbors of start: {neighbors}")
    
    # Check which neighbors are valid (in bounds and not walls)
    width, height = len(grid[0]), len(grid)
    valid_neighbors = [
        n for n in neighbors 
        if in_bounds(n, width, height) and grid[n.y][n.x] != '#'
    ]
    print(f"Valid neighbors: {valid_neighbors}")


def example_bfs():
    """Demonstrate BFS pathfinding."""
    print("\n=== BFS Pathfinding ===\n")
    
    # Simple maze
    grid = [
        ['#', '#', '#', '#', '#'],
        ['#', 'S', '.', '.', '#'],
        ['#', '#', '#', '.', '#'],
        ['#', '.', '.', '.', '#'],
        ['#', '.', 'E', '#', '#'],
    ]
    
    print("Maze:")
    print_grid(grid)
    
    start = find_in_grid(grid, 'S')
    end = find_in_grid(grid, 'E')
    width, height = len(grid[0]), len(grid)
    
    def get_neighbors(pos):
        """Get valid neighboring positions."""
        neighbors = []
        for n in pos.neighbors4():
            if in_bounds(n, width, height) and grid[n.y][n.x] != '#':
                neighbors.append(n)
        return neighbors
    
    # Find shortest path
    path = bfs_shortest_path(start, end, get_neighbors)
    
    if path:
        print(f"\nShortest path found: {len(path) - 1} steps")
        print(f"Path: {' -> '.join(str(p) for p in path)}")
    else:
        print("\nNo path found!")


def example_math_functions():
    """Demonstrate math utilities."""
    print("\n=== Math Functions ===\n")
    
    # LCM and GCD
    nums = [12, 18, 24]
    print(f"Numbers: {nums}")
    print(f"LCM: {lcm_list(nums)}")
    print(f"GCD: {gcd_list(nums)}")
    
    # Prime numbers
    num = 17
    print(f"\nIs {num} prime? {is_prime(num)}")
    
    num = 60
    factors = prime_factors(num)
    print(f"Prime factors of {num}: {factors}")


def example_collections():
    """Demonstrate collection utilities."""
    print("\n=== Collection Utilities ===\n")
    
    # Flatten nested lists
    nested = [[1, 2], [3, 4, 5], [6]]
    flat = flatten(nested)
    print(f"Flattened: {flat}")
    
    # Chunk a list
    data = list(range(10))
    chunks = chunk(data, 3)
    print(f"Chunked {data} into groups of 3: {chunks}")
    
    # Transpose matrix
    matrix = [[1, 2, 3], [4, 5, 6]]
    transposed = transpose(matrix)
    print(f"Transposed: {transposed}")
    
    # Count occurrences
    items = ['a', 'b', 'a', 'c', 'a', 'b']
    counts = count_occurrences(items)
    print(f"Counts: {counts}")


def example_range_operations():
    """Demonstrate range utilities."""
    print("\n=== Range Operations ===\n")
    
    # Check overlap
    r1 = (1, 5)
    r2 = (3, 7)
    r3 = (8, 10)
    
    print(f"Do {r1} and {r2} overlap? {ranges_overlap(r1, r2)}")
    print(f"Do {r1} and {r3} overlap? {ranges_overlap(r1, r3)}")
    
    # Merge overlapping ranges
    ranges = [(1, 3), (2, 6), (8, 10), (15, 18)]
    merged = merge_ranges(ranges)
    print(f"\nOriginal ranges: {ranges}")
    print(f"Merged ranges: {merged}")


def example_testing():
    """Demonstrate testing utilities."""
    print("\n=== Testing ===\n")
    
    def add_numbers(nums):
        return sum(nums)
    
    # Single test
    run_test(add_numbers, [1, 2, 3], 6, "Sum of 1,2,3")
    
    # Multiple tests
    test_cases = [
        ([1, 2, 3], 6),
        ([10, 20], 30),
        ([], 0),
    ]
    run_tests(add_numbers, test_cases, ["Test 1", "Test 2", "Empty list"])


def main():
    """Run all examples."""
    print("=" * 60)
    print("Advent of Code 2025 - Utility Functions Examples")
    print("=" * 60)
    
    example_file_reading()
    example_parsing()
    example_grid_operations()
    example_bfs()
    example_math_functions()
    example_collections()
    example_range_operations()
    example_testing()
    
    print("\n" + "=" * 60)
    print("Examples complete! Check utility.py for more functions.")
    print("=" * 60)


if __name__ == "__main__":
    main()
