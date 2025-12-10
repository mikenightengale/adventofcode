# Advent of Code 2025 - Python

Welcome to my Advent of Code 2025 solutions repository! This repository contains my solutions written in Python.

## Repository Structure

```
.
├── utility.py          # Common utility functions
├── 2025/
│   ├── Day 1/
│   │   ├── input.txt   # Puzzle input
│   │   ├── solution.py # Solution code
│   │   └── ...
│   └── Day 2/
│       └── ...
└── README.md
```

## Utility Functions

The `utility.py` file contains commonly used functions for solving Advent of Code puzzles. Below is a summary organized by category:

### 📁 File I/O and Input Handling

- **`read_input(filepath)`** - Read entire input file as string
- **`read_lines(filepath, strip=True)`** - Read input as list of lines
- **`read_grid(filepath)`** - Read input as 2D character grid
- **`read_int_grid(filepath)`** - Read input as 2D integer grid
- **`read_as_numpy(filepath, dtype='U1')`** - Read input as NumPy array
- **`read_blocks(filepath)`** - Read input separated by blank lines
- **`download_input(year, day, session_cookie, output_path)`** - Download puzzle input from AOC

### 🔍 Parsing Utilities

- **`parse_numbers(text)`** - Extract all integers from string (including negative)
- **`parse_words(text)`** - Extract all words from string
- **`split_by_delimiter(text, delimiter=',')`** - Split and strip text by delimiter

### 🗺️ Grid and Coordinate Utilities

- **`Point` class** - Immutable 2D coordinate with operations
  - `.manhattan_distance(other)` - Calculate Manhattan distance
  - `.neighbors4()` - Get 4 orthogonal neighbors
  - `.neighbors8()` - Get 8 neighbors including diagonals
- **`in_bounds(point, width, height)`** - Check if point is within grid
- **`find_in_grid(grid, target)`** - Find first occurrence of value
- **`find_all_in_grid(grid, target)`** - Find all occurrences of value
- **`print_grid(grid, separator='')`** - Pretty print a grid

Direction constants: `NORTH`, `EAST`, `SOUTH`, `WEST`, `DIRECTIONS_4`, `DIRECTIONS_8`

### 🔎 Graph and Search Algorithms

- **`bfs(start, is_goal, get_neighbors)`** - Breadth-first search
- **`bfs_shortest_path(start, goal, get_neighbors)`** - Find shortest path with BFS
- **`dfs(start, is_goal, get_neighbors)`** - Depth-first search
- **`dijkstra(start, is_goal, get_neighbors)`** - Dijkstra's algorithm for weighted graphs

### 🔢 Math and Number Theory

- **`lcm(a, b)`** / **`lcm_list(numbers)`** - Least common multiple
- **`gcd_list(numbers)`** - Greatest common divisor of list
- **`is_prime(n)`** - Check if number is prime
- **`prime_factors(n)`** - Get list of prime factors

### 📦 Collection Utilities

- **`flatten(nested_list)`** - Flatten nested lists
- **`chunk(iterable, size)`** - Split into chunks
- **`transpose(matrix)`** - Transpose 2D list
- **`rotate_grid_cw(grid)`** / **`rotate_grid_ccw(grid)`** - Rotate grids
- **`count_occurrences(iterable)`** - Count element occurrences

### 🐛 Debugging and Timing

- **`@timeit`** - Decorator to time function execution
- **`debug_print(obj, label=None)`** - Pretty print for debugging

### 📏 Range and Interval Utilities

- **`ranges_overlap(r1, r2)`** - Check if ranges overlap
- **`merge_ranges(ranges)`** - Merge overlapping ranges

### 📝 String and Pattern Utilities

- **`hamming_distance(s1, s2)`** - Hamming distance
- **`levenshtein_distance(s1, s2)`** - Edit distance

### ✅ Testing Utilities

- **`run_test(func, input_data, expected, description)`** - Run single test
- **`run_tests(func, test_cases, descriptions)`** - Run multiple tests

## Example Usage

```python
from utility import *

# Read input
data = read_lines("2025/Day 1/input.txt")

# Parse numbers from text
numbers = parse_numbers("There are 42 apples and -7 oranges")
# Result: [42, -7]

# Working with grids
grid = read_grid("input.txt")
start = find_in_grid(grid, 'S')
neighbors = start.neighbors4()

# BFS pathfinding
def get_valid_neighbors(pos):
    return [n for n in pos.neighbors4() if in_bounds(n, width, height)]

path = bfs_shortest_path(start, goal, get_valid_neighbors)

# Timing your solution
@timeit
def solve_part1(data):
    # Your solution here
    pass

result = solve_part1(data)
```

## Common Patterns in Advent of Code

### Reading Different Input Formats

```python
# Simple list of integers
numbers = [int(x) for x in read_lines("input.txt")]

# Grid of characters
grid = read_grid("input.txt")

# Blocks separated by blank lines
blocks = read_blocks("input.txt")

# Extract all numbers from mixed text
all_nums = parse_numbers(read_input("input.txt"))
```

### Grid Traversal

```python
grid = read_grid("input.txt")
height, width = len(grid), len(grid[0])

# Find starting position
start = find_in_grid(grid, 'S')

# Explore neighbors
for neighbor in start.neighbors4():
    if in_bounds(neighbor, width, height):
        value = grid[neighbor.y][neighbor.x]
        # Process neighbor...
```

### BFS for Shortest Path

```python
def solve_maze(grid):
    start = find_in_grid(grid, 'S')
    goal = find_in_grid(grid, 'E')
    
    def get_neighbors(pos):
        neighbors = []
        for n in pos.neighbors4():
            if in_bounds(n, width, height) and grid[n.y][n.x] != '#':
                neighbors.append(n)
        return neighbors
    
    path = bfs_shortest_path(start, goal, get_neighbors)
    return len(path) - 1  # Number of steps
```

## Requirements

```bash
pip install numpy requests
```

## Tips for Advent of Code

1. **Start Simple** - Get the basic solution working first, optimize later
2. **Use Test Cases** - Verify your solution with the provided examples
3. **Print Intermediate Results** - Use `debug_print()` to visualize data structures
4. **Time Your Code** - Use the `@timeit` decorator to identify bottlenecks
5. **Read the Problem Carefully** - Many mistakes come from misunderstanding requirements
6. **Part 2 Often Scales Up** - Design your Part 1 solution with scalability in mind

## Resources

- [Advent of Code Website](https://adventofcode.com/)
- [Advent of Code Subreddit](https://www.reddit.com/r/adventofcode/)
- [Python Documentation](https://docs.python.org/3/)

## License

This repository is for educational purposes. Advent of Code is created by [Eric Wastl](http://was.tl/).
