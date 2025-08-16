# Statistics Calculator

A multi-language implementation of basic statistics calculations (mean, median, mode) demonstrating different programming paradigms.

## Project Structure

```
.
├── CProgramming/
│   └── statistics.c
├── python/
│   └── statistics.py
└── README.md
```

## Overview

This project implements a statistics calculator in two different programming languages, each showcasing different programming paradigms:

- **C (Procedural)**: Manual memory management, array manipulation, and step-by-step procedural logic
- **Python (Object-Oriented)**: Encapsulated class design with methods and data abstraction

Both implementations calculate:
- **Mean**: Average of all numbers
- **Median**: Middle value when numbers are sorted
- **Mode**: Most frequently occurring number(s)

## Requirements

### C Implementation
- GCC compiler (or any C99-compatible compiler)
- Standard C library

### Python Implementation  
- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation & Running

### C Implementation

1. Navigate to the C programming directory:
```bash
cd CProgramming
```

2. Compile the program:
```bash
gcc -o statistics statistics.c
```

3. Run the executable:
```bash
./statistics
```

**Alternative compilation with debugging symbols:**
```bash
gcc -g -Wall -Wextra -o statistics statistics.c
```

### Python Implementation

1. Navigate to the Python directory:
```bash
cd python
```

2. Run the program:
```bash
python3 statistics.py
```

**Or on systems where python3 is the default:**
```bash
python statistics.py
```

## Sample Output

Both implementations will produce similar output for the test datasets:

```
Test 1: [1, 2, 3, 4, 5]
Mean: 3.00
Median: 3.00
Mode: 1, 2, 3, 4, 5 (frequency: 1)

Test 2: [1, 2, 2, 3, 4, 4, 4]
Mean: 2.86
Median: 3.00
Mode: 4 (frequency: 3)

Test 3: [5, 5, 3, 3, 1, 1]
Mean: 3.00
Median: 3.00
Mode: 1, 3, 5 (frequency: 2)

Test 4: [10]
Mean: 10.00
Median: 10.00
Mode: 10 (frequency: 1)
```

## Implementation Details

### C Implementation (Procedural Paradigm)
- **Memory Management**: Manual allocation/deallocation using `malloc()` and `free()`
- **Sorting**: Uses standard library `qsort()` function
- **Data Structures**: Arrays and structs for organizing data
- **Approach**: Step-by-step procedural functions

**Key Functions:**
- `calculate_mean()` - Computes average using loop summation
- `calculate_median()` - Sorts array copy and finds middle value(s)
- `calculate_mode()` - Manually counts frequencies and finds maximum
- `print_array()` - Utility function for display

### Python Implementation (Object-Oriented Paradigm)
- **Encapsulation**: Private data members with public interface methods
- **Data Structures**: Lists and Counter from collections module
- **Approach**: Class-based design with method encapsulation

**Key Methods:**
- `calculate_mean()` - Uses built-in `sum()` and `len()`
- `calculate_median()` - Uses `sorted()` with list slicing
- `calculate_mode()` - Uses `Counter` for frequency analysis
- `get_all_statistics()` - Returns comprehensive results dictionary

## Features

### C Implementation
- ✅ Manual memory management
- ✅ Error handling for edge cases
- ✅ Memory-safe operations
- ✅ Efficient sorting and searching
- ✅ Multiple mode detection

### Python Implementation
- ✅ Object-oriented design
- ✅ Type hints for better documentation
- ✅ Dynamic data manipulation methods
- ✅ Comprehensive statistics output
- ✅ Method chaining capabilities
- ✅ Built-in error handling

## Customization

### Adding New Test Data

**C Implementation:**
Modify the test arrays in the `main()` function:
```c
int new_data[] = {your, numbers, here};
```

**Python Implementation:**
Add new datasets to the `test_datasets` list in `main()`:
```python
test_datasets = [
    [1, 2, 3, 4, 5],
    [your, new, data, here]
]
```

### Extending Functionality

**C Implementation:**
- Add new functions following the existing procedural pattern
- Remember to handle memory allocation/deallocation

**Python Implementation:**
- Add new methods to the `StatisticsCalculator` class
- Utilize existing private data members and helper methods

## Troubleshooting

### C Compilation Issues
- **Error: `gcc: command not found`**
  - Install GCC: `sudo apt install gcc` (Ubuntu/Debian) or `brew install gcc` (macOS)
- **Segmentation fault**
  - Run with debugging: `gcc -g -o statistics statistics.c && gdb ./statistics`

### Python Runtime Issues
- **Error: `python: command not found`**
  - Try `python3` instead of `python`
  - Install Python from python.org
- **Import errors**
  - All imports use standard library modules (no pip install needed)

## Performance Notes

- **C Implementation**: Faster execution, lower memory usage, manual optimization
- **Python Implementation**: Slower execution, higher memory usage, but more readable and maintainable

## License

This project is provided as educational material for demonstrating different programming paradigms.