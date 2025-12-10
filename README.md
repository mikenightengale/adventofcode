# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) challenges, written in Python.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/mikenightengale/adventofcode.git
cd adventofcode

# Install dependencies
pip install numpy requests

# Run a solution (example)
python 2025/Day\ 1/solution.py
```

## 📚 Documentation

- **[Utility Functions Guide](README_UTILITY.md)** - Complete documentation of all helper functions
- **[Quick Reference](QUICKREF.md)** - Cheat sheet for common patterns
- **[Example Usage](example_usage.py)** - Practical examples of using the utilities
- **[Solution Template](template_solution.py)** - Template for new puzzles

## 🛠️ Utility Functions

This repository includes a comprehensive `utility.py` module with commonly used functions for AoC puzzles:

- **File I/O**: Read inputs as lines, grids, blocks, or NumPy arrays
- **Parsing**: Extract numbers, words, and patterns from text
- **Grid Operations**: 2D coordinate system with pathfinding helpers
- **Search Algorithms**: BFS, DFS, and Dijkstra implementations
- **Math Functions**: LCM, GCD, prime factorization
- **Collections**: Flatten, chunk, transpose, and rotate operations
- **Debugging Tools**: Timing decorators and pretty-printing utilities

See [README_UTILITY.md](README_UTILITY.md) for full documentation.

## 📁 Repository Structure

```
.
├── utility.py              # Reusable utility functions
├── template_solution.py    # Template for new solutions
├── example_usage.py        # Examples of utility usage
├── README_UTILITY.md       # Complete utility documentation
├── QUICKREF.md            # Quick reference guide
└── 2025/
    ├── Day 1/
    │   ├── input.txt
    │   └── solution.py
    └── ...
```

## 🎯 Progress

| Day | Part 1 | Part 2 | Stars |
|-----|--------|--------|-------|
| 1   | ⭐     | ⭐     | ⭐⭐   |

## 📝 Notes

Solutions prioritize clarity and demonstrating utility function usage over optimization. Each solution includes:
- Clear problem parsing
- Well-documented functions
- Example test cases where applicable
- Timing information

## 🔗 Resources

- [Advent of Code](https://adventofcode.com/)
- [r/adventofcode](https://www.reddit.com/r/adventofcode/)
- [Python Documentation](https://docs.python.org/3/)

## 📄 License

This repository is for educational purposes. Advent of Code is created by [Eric Wastl](http://was.tl/).
