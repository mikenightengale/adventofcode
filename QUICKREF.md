# Advent of Code Utility Quick Reference

## Most Common Patterns

### 1. Reading Input
```python
# Lines of text
lines = read_lines("input.txt")

# Entire file as string
text = read_input("input.txt")

# Grid of characters
grid = read_grid("input.txt")

# Blocks separated by empty lines
blocks = read_blocks("input.txt")
```

### 2. Parsing
```python
# Extract all numbers from text
numbers = parse_numbers("abc 123 def -456")  # [123, -456]

# Extract words
words = parse_words("Hello, World!")  # ['Hello', 'World']
```

### 3. Grid Navigation
```python
# Create a point
pos = Point(x, y)

# Get neighbors
neighbors = pos.neighbors4()  # N, E, S, W
neighbors = pos.neighbors8()  # Including diagonals

# Check bounds
if in_bounds(pos, width, height):
    # Position is valid

# Find in grid
start = find_in_grid(grid, 'S')
all_walls = find_all_in_grid(grid, '#')
```

### 4. Pathfinding (BFS)
```python
def get_neighbors(pos):
    return [n for n in pos.neighbors4() 
            if in_bounds(n, width, height) and grid[n.y][n.x] != '#']

path = bfs_shortest_path(start, goal, get_neighbors)
steps = len(path) - 1
```

### 5. Common Math
```python
# LCM/GCD
lcm_result = lcm_list([12, 18, 24])
gcd_result = gcd_list([12, 18, 24])

# Prime factorization
factors = prime_factors(60)  # [2, 2, 3, 5]
```

### 6. Collection Operations
```python
# Flatten nested lists
flat = flatten([[1, 2], [3, 4]])  # [1, 2, 3, 4]

# Split into chunks
chunks = chunk(range(10), 3)  # [[0,1,2], [3,4,5], [6,7,8], [9]]

# Count occurrences
counts = count_occurrences(['a', 'b', 'a'])  # {'a': 2, 'b': 1}
```

### 7. Debugging
```python
# Time a function
@timeit
def solve():
    pass

# Pretty print
debug_print(my_grid, "Grid State")
```

## Cheat Sheet by Problem Type

### Graph/Maze Problems
```python
grid = read_grid("input.txt")
start = find_in_grid(grid, 'S')
goal = find_in_grid(grid, 'E')

def neighbors(p):
    return [n for n in p.neighbors4() if valid(n)]

path = bfs_shortest_path(start, goal, neighbors)
```

### Number Parsing Problems
```python
lines = read_lines("input.txt")
all_numbers = [parse_numbers(line) for line in lines]
```

### 2D Grid Problems
```python
grid = read_grid("input.txt")
height, width = len(grid), len(grid[0])

for y in range(height):
    for x in range(width):
        pos = Point(x, y)
        value = grid[pos.y][pos.x]
```

### Cycle Detection
```python
seen = {}
state = initial_state
step = 0

while state not in seen:
    seen[state] = step
    state = next_state(state)
    step += 1

cycle_start = seen[state]
cycle_length = step - cycle_start
```

### Range/Interval Problems
```python
ranges = [(1, 5), (3, 8), (10, 15)]
merged = merge_ranges(ranges)  # [(1, 8), (10, 15)]
```

## Function Categories

| Category | Key Functions |
|----------|--------------|
| **I/O** | `read_input`, `read_lines`, `read_grid`, `read_blocks` |
| **Parsing** | `parse_numbers`, `parse_words`, `split_by_delimiter` |
| **Grid** | `Point`, `find_in_grid`, `in_bounds`, `print_grid` |
| **Search** | `bfs`, `bfs_shortest_path`, `dfs`, `dijkstra` |
| **Math** | `lcm`, `gcd_list`, `is_prime`, `prime_factors` |
| **Collections** | `flatten`, `chunk`, `transpose`, `count_occurrences` |
| **Debug** | `@timeit`, `debug_print` |
| **Ranges** | `ranges_overlap`, `merge_ranges` |

## Tips

1. **Start with read_lines()** - Most problems use line-based input
2. **Use Point for coordinates** - Much cleaner than tuples
3. **BFS for shortest path** - Almost always the right choice for unweighted graphs
4. **Test with examples first** - Use `run_test()` to verify logic
5. **Time your solutions** - Use `@timeit` to find bottlenecks
6. **Print intermediate results** - Use `debug_print()` liberally while developing

## Common Imports
```python
from utility import *
from collections import defaultdict, deque, Counter
from itertools import combinations, permutations, product
import re
```
