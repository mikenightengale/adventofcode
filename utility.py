"""
Advent of Code 2025 - Utility Functions
A comprehensive collection of commonly used functions for solving AoC puzzles.
"""

import re
import requests
from pathlib import Path
from typing import Callable, TypeVar, Iterable, Any, Optional
from collections import defaultdict, deque
from dataclasses import dataclass
import itertools
import numpy as np
from functools import wraps
import time

# Type variables for generic functions
T = TypeVar('T')
U = TypeVar('U')

# ============================================================================
# File I/O and Input Handling
# ============================================================================

def read_input(filepath: str) -> str:
    """Read the entire input file as a string."""
    return Path(filepath).read_text().strip()


def read_lines(filepath: str, strip: bool = True) -> list[str]:
    """Read input file as a list of lines."""
    with open(filepath) as f:
        lines = f.readlines()
        return [line.strip() for line in lines] if strip else lines


def read_grid(filepath: str) -> list[list[str]]:
    """Read input as a 2D grid of characters."""
    lines = read_lines(filepath)
    return [list(line) for line in lines]


def read_int_grid(filepath: str) -> list[list[int]]:
    """Read input as a 2D grid of integers."""
    lines = read_lines(filepath)
    return [[int(c) for c in line] for line in lines]


def read_as_numpy(filepath: str, dtype='U1') -> np.ndarray:
    """Read input as a NumPy array (useful for grids)."""
    lines = read_lines(filepath)
    grid = [list(line) for line in lines]
    return np.array(grid, dtype=dtype)


def read_blocks(filepath: str) -> list[list[str]]:
    """Read input separated by blank lines into blocks."""
    content = read_input(filepath)
    blocks = content.split('\n\n')
    return [block.split('\n') for block in blocks]


def download_input(year: int, day: int, session_cookie: str, output_path: Optional[str] = None) -> str:
    """
    Download puzzle input from Advent of Code.
    
    Args:
        year: Year of the puzzle
        day: Day of the puzzle (1-25)
        session_cookie: Your session cookie from adventofcode.com
        output_path: Optional path to save the input
        
    Returns:
        The puzzle input as a string
    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {"User-Agent": "github.com/adventofcode/2025 by user"}
    cookies = {"session": session_cookie}
    
    response = requests.get(url, headers=headers, cookies=cookies)
    response.raise_for_status()
    
    if output_path:
        Path(output_path).write_text(response.text)
    
    return response.text.strip()


# ============================================================================
# Parsing Utilities
# ============================================================================

def parse_numbers(text: str) -> list[int]:
    """Extract all integers (including negative) from a string."""
    return [int(x) for x in re.findall(r'-?\d+', text)]


def parse_words(text: str) -> list[str]:
    """Extract all words from a string."""
    return re.findall(r'[a-zA-Z]+', text)


def split_by_delimiter(text: str, delimiter: str = ',') -> list[str]:
    """Split text by delimiter and strip whitespace."""
    return [part.strip() for part in text.split(delimiter)]


# ============================================================================
# Grid and Coordinate Utilities
# ============================================================================

@dataclass(frozen=True)
class Point:
    """Immutable 2D point/coordinate."""
    x: int
    y: int
    
    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: int) -> 'Point':
        return Point(self.x * scalar, self.y * scalar)
    
    def manhattan_distance(self, other: 'Point') -> int:
        """Calculate Manhattan distance to another point."""
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    def neighbors4(self) -> list['Point']:
        """Return 4 orthogonal neighbors (N, E, S, W)."""
        return [
            Point(self.x, self.y - 1),  # North
            Point(self.x + 1, self.y),  # East
            Point(self.x, self.y + 1),  # South
            Point(self.x - 1, self.y),  # West
        ]
    
    def neighbors8(self) -> list['Point']:
        """Return 8 neighbors including diagonals."""
        return [
            Point(self.x + dx, self.y + dy)
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
            if dx != 0 or dy != 0
        ]


# Common direction vectors
NORTH = Point(0, -1)
EAST = Point(1, 0)
SOUTH = Point(0, 1)
WEST = Point(-1, 0)
DIRECTIONS_4 = [NORTH, EAST, SOUTH, WEST]
DIRECTIONS_8 = [Point(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]


def in_bounds(point: Point, width: int, height: int) -> bool:
    """Check if a point is within grid bounds."""
    return 0 <= point.x < width and 0 <= point.y < height


def find_in_grid(grid: list[list[Any]], target: Any) -> Point | None:
    """Find the first occurrence of a value in a grid."""
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == target:
                return Point(x, y)
    return None


def find_all_in_grid(grid: list[list[Any]], target: Any) -> list[Point]:
    """Find all occurrences of a value in a grid."""
    points = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == target:
                points.append(Point(x, y))
    return points


def print_grid(grid: list[list[Any]], separator: str = '') -> None:
    """Pretty print a grid."""
    for row in grid:
        print(separator.join(str(cell) for cell in row))


# ============================================================================
# Graph and Search Algorithms
# ============================================================================

def bfs(start: T, is_goal: Callable[[T], bool], get_neighbors: Callable[[T], Iterable[T]]) -> tuple[T | None, dict[T, Optional[T]]]:
    """
    Breadth-first search.
    
    Returns:
        - The goal node (or None if not found)
        - A dict mapping each visited node to its parent (for path reconstruction)
    """
    visited: dict[T, Optional[T]] = {start: None}
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        if is_goal(current):
            return current, visited
        
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)
    
    return None, visited


def bfs_shortest_path(start: T, goal: T, get_neighbors: Callable[[T], Iterable[T]]) -> list[T] | None:
    """Find shortest path from start to goal using BFS."""
    goal_node, visited = bfs(start, lambda n: n == goal, get_neighbors)
    
    if goal_node is None:
        return None
    
    # Reconstruct path
    path = []
    current = goal_node
    while current is not None:
        path.append(current)
        current = visited[current]
    
    return list(reversed(path))


def dfs(start: T, is_goal: Callable[[T], bool], get_neighbors: Callable[[T], Iterable[T]]) -> tuple[T | None, set[T]]:
    """
    Depth-first search.
    
    Returns:
        - The goal node (or None if not found)
        - A set of all visited nodes
    """
    visited = set()
    stack = [start]
    
    while stack:
        current = stack.pop()
        
        if current in visited:
            continue
            
        visited.add(current)
        
        if is_goal(current):
            return current, visited
        
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                stack.append(neighbor)
    
    return None, visited


def dijkstra(start: T, is_goal: Callable[[T], bool], get_neighbors: Callable[[T], list[tuple[T, int]]]) -> tuple[T | None, dict[T, int]]:
    """
    Dijkstra's shortest path algorithm.
    
    Args:
        start: Starting node
        is_goal: Function to check if a node is the goal
        get_neighbors: Function returning list of (neighbor, cost) tuples
        
    Returns:
        - The goal node (or None if not found)
        - A dict mapping nodes to their minimum distance from start
    """
    import heapq
    
    distances = {start: 0}
    heap = [(0, start)]
    
    while heap:
        current_dist, current = heapq.heappop(heap)
        
        if current_dist > distances.get(current, float('inf')):
            continue
            
        if is_goal(current):
            return current, distances
        
        for neighbor, cost in get_neighbors(current):
            new_dist = current_dist + cost
            if new_dist < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    return None, distances


# ============================================================================
# Math and Number Theory
# ============================================================================

def lcm(a: int, b: int) -> int:
    """Least common multiple."""
    from math import gcd
    return abs(a * b) // gcd(a, b)


def lcm_list(numbers: list[int]) -> int:
    """LCM of a list of numbers."""
    from functools import reduce
    return reduce(lcm, numbers)


def gcd_list(numbers: list[int]) -> int:
    """GCD of a list of numbers."""
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_factors(n: int) -> list[int]:
    """Return list of prime factors of n."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


# ============================================================================
# Collection Utilities
# ============================================================================

def flatten(nested_list: Iterable[Iterable[T]]) -> list[T]:
    """Flatten a nested list."""
    return [item for sublist in nested_list for item in sublist]


def chunk(iterable: Iterable[T], size: int) -> list[list[T]]:
    """Split an iterable into chunks of given size."""
    result = []
    chunk_list = []
    for item in iterable:
        chunk_list.append(item)
        if len(chunk_list) == size:
            result.append(chunk_list)
            chunk_list = []
    if chunk_list:
        result.append(chunk_list)
    return result


def transpose(matrix: list[list[T]]) -> list[list[T]]:
    """Transpose a 2D list (swap rows and columns)."""
    return list(map(list, zip(*matrix)))


def rotate_grid_cw(grid: list[list[T]]) -> list[list[T]]:
    """Rotate a grid 90 degrees clockwise."""
    return [list(row) for row in zip(*grid[::-1])]


def rotate_grid_ccw(grid: list[list[T]]) -> list[list[T]]:
    """Rotate a grid 90 degrees counter-clockwise."""
    return [list(row) for row in zip(*grid)][::-1]


def count_occurrences(iterable: Iterable[T]) -> dict[T, int]:
    """Count occurrences of each element."""
    counts = defaultdict(int)
    for item in iterable:
        counts[item] += 1
    return dict(counts)


# ============================================================================
# Debugging and Timing
# ============================================================================

def timeit(func: Callable) -> Callable:
    """Decorator to time function execution."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


def debug_print(obj: Any, label: Optional[str] = None) -> None:
    """Pretty print an object for debugging."""
    if label:
        print(f"=== {label} ===")
    # Print as grid if it's a list of lists
    if isinstance(obj, list) and obj and all(isinstance(row, list) for row in obj):
        print_grid(obj)
    else:
        from pprint import pprint
        pprint(obj)
    if label:
        print("=" * (len(label) + 8))


# ============================================================================
# Range and Interval Utilities
# ============================================================================

def ranges_overlap(r1: tuple[int, int], r2: tuple[int, int]) -> bool:
    """Check if two ranges [start, end) overlap."""
    return r1[0] < r2[1] and r2[0] < r1[1]


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping ranges."""
    if not ranges:
        return []
    
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]
    
    for current in sorted_ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    
    return merged


# ============================================================================
# String and Pattern Utilities
# ============================================================================

def hamming_distance(s1: str, s2: str) -> int:
    """Calculate Hamming distance between two strings."""
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def levenshtein_distance(s1: str, s2: str) -> int:
    """Calculate Levenshtein (edit) distance between two strings."""
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]


# ============================================================================
# Testing Utilities
# ============================================================================

def run_test(func: Callable, input_data: Any, expected: Any, description: str = "") -> bool:
    """Run a test case and print results."""
    result = func(input_data)
    passed = result == expected
    status = "✓" if passed else "✗"
    desc_str = f" ({description})" if description else ""
    print(f"{status} Test{desc_str}: Expected {expected}, got {result}")
    return passed


def run_tests(func: Callable, test_cases: list[tuple[Any, Any]], descriptions: Optional[list[str]] = None) -> bool:
    """Run multiple test cases."""
    if descriptions is None:
        descriptions = [f"Case {i+1}" for i in range(len(test_cases))]
    
    results = []
    for (input_data, expected), desc in zip(test_cases, descriptions):
        results.append(run_test(func, input_data, expected, desc))
    
    passed = sum(results)
    total = len(results)
    print(f"\nPassed {passed}/{total} tests")
    return all(results)
