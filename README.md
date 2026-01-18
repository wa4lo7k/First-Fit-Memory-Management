# First Fit Memory Management Simulator

A Python-based MVP implementation of the First Fit memory allocation algorithm used in operating systems. This project is designed for academic evaluation and provides a comprehensive simulation of memory management concepts.

## 🎯 Project Overview

This simulator demonstrates how operating systems manage memory allocation using the First Fit algorithm, including:

- **First Fit Allocation**: Finds the first available memory block large enough for a process
- **Memory Deallocation**: Frees memory and merges adjacent blocks to reduce fragmentation
- **Fragmentation Analysis**: Tracks and reports internal and external fragmentation
- **Interactive CLI**: User-friendly command-line interface for real-time interaction

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Running the Simulator

```bash
# Start with default 1000 units of memory
python main.py

# Start with custom memory size
python main.py 2000

# Run comprehensive tests
python test_memory_manager.py

# Get help
python main.py --help
```

## 📋 Features

### Core Functionality
- ✅ First Fit memory allocation algorithm
- ✅ Process-based memory deallocation
- ✅ Automatic adjacent block merging
- ✅ Real-time memory status display
- ✅ Comprehensive fragmentation analysis
- ✅ Operation logging and history

### User Interface
- 🖥️ Interactive command-line menu
- 📊 Formatted memory map display
- 📈 Fragmentation statistics
- 📝 Detailed operation logs
- ⚠️ Error handling and validation

## 🏗️ System Architecture

### Memory Representation
```
Memory Block Structure:
┌─────────────────┬──────┬─────────┬────────────┐
│ Start Address   │ Size │ Status  │ Process ID │
├─────────────────┼──────┼─────────┼────────────┤
│ 0               │ 150  │ ALLOC   │ 1          │
│ 150             │ 200  │ FREE    │ -          │
│ 350             │ 100  │ ALLOC   │ 2          │
└─────────────────┴──────┴─────────┴────────────┘
```

### Algorithm Implementation

#### First Fit Allocation
1. Scan memory blocks sequentially from start
2. Find first free block with size ≥ requested size
3. Allocate the block to the process
4. Split block if remaining space > 0
5. Log the allocation result

#### Deallocation Process
1. Locate the allocated block for the process
2. Mark the block as free
3. Merge with adjacent free blocks (left and right)
4. Log the deallocation and any merges

## 📖 Usage Guide

### Interactive Menu Options

1. **Allocate Memory**
   - Enter Process ID (positive integer)
   - Enter Memory Size (positive integer)
   - System finds first suitable free block

2. **Deallocate Memory**
   - Enter Process ID to free
   - System releases memory and merges blocks

3. **Display Memory Status**
   - Shows total, allocated, and free memory
   - Displays utilization percentage
   - Shows block count statistics

4. **Display Memory Map**
   - Detailed table of all memory blocks
   - Shows start/end addresses, sizes, and status
   - Identifies which process owns each block

5. **Show Allocation Log**
   - History of all operations
   - Success/failure status for each operation
   - Block merging notifications

6. **Display Fragmentation Info**
   - External fragmentation analysis
   - Memory utilization statistics
   - Free block distribution

### Example Session

```
FIRST FIT MEMORY MANAGEMENT SIMULATOR
====================================
1. Allocate Memory
2. Deallocate Memory
3. Display Memory Status
4. Display Memory Map
5. Show Allocation Log
6. Display Fragmentation Info
7. Exit Program
====================================

Select an option (1-7): 1

--- ALLOCATE MEMORY ---
Enter Process ID: 1
Enter Memory Size (units): 200

Attempting to allocate 200 units for process 1...
✓ Memory allocation successful!
Log: SUCCESS: Allocated 200 units to process 1 at address 0
```

## 🧪 Testing and Validation

### Automated Test Suite

Run the comprehensive test suite:
```bash
python test_memory_manager.py
```

The test suite includes:

1. **Basic Allocation Tests**
   - Successful allocations
   - Allocation failures
   - Input validation

2. **Deallocation and Merging Tests**
   - Memory release
   - Adjacent block merging
   - Block coalescing scenarios

3. **Fragmentation Demonstration**
   - External fragmentation creation
   - Impact on large allocations
   - Fragmentation measurement

4. **Edge Case Testing**
   - Invalid inputs (zero, negative sizes)
   - Duplicate process allocations
   - Non-existent process deallocation
   - Exact fit scenarios

5. **First Fit Behavior Verification**
   - Algorithm correctness
   - Sequential block scanning
   - First available block selection

### Sample Test Output

```
TEST 1: Basic Memory Allocation
==============================
Testing successful allocations...
Total allocated: 450 units
Total free: 550 units

MEMORY MAP
==========
Start    End      Size     Status       Process ID
--------------------------------------------------
0        99       100      ALLOCATED    1
100      299      200      ALLOCATED    2
300      449      150      ALLOCATED    3
450      999      550      FREE         -
--------------------------------------------------

✓ Basic allocation tests passed!
```

## 📊 Fragmentation Analysis

### Types of Fragmentation

1. **External Fragmentation**
   - Free memory split into small, non-contiguous blocks
   - Measured by counting extra free blocks
   - Reduced through block merging

2. **Internal Fragmentation**
   - Unused space within allocated blocks
   - Minimal in this variable-size implementation
   - Would be significant with fixed-size blocks

### Fragmentation Metrics

```
FRAGMENTATION ANALYSIS
======================
Total Memory: 1000 units
Allocated Memory: 450 units
Free Memory: 550 units
Memory Utilization: 45.0%
Free Block Count: 3
External Fragmentation: 2 extra blocks
Internal Fragmentation: 0 units
======================
```

## 🔧 Implementation Details

### File Structure

```
first-fit-memory-manager/
├── main.py                 # Main entry point
├── memory_manager.py       # Core algorithm implementation
├── cli_interface.py        # Command-line interface
├── test_memory_manager.py  # Comprehensive test suite
└── README.md              # This documentation
```

### Key Classes

#### `MemoryBlock`
- Represents individual memory blocks
- Stores address, size, status, and process ID
- Provides string representation for display

#### `FirstFitMemoryManager`
- Implements First Fit allocation algorithm
- Manages memory block list
- Handles allocation, deallocation, and merging
- Provides status and fragmentation analysis

#### `MemoryManagerCLI`
- Interactive command-line interface
- Input validation and error handling
- Menu-driven user interaction
- Formatted output display

### Algorithm Complexity

- **Allocation**: O(n) where n is the number of blocks
- **Deallocation**: O(n) for finding block + O(n) for merging
- **Space**: O(n) for storing block metadata

## 🎓 Educational Value

### Learning Objectives

This project demonstrates:

1. **Memory Management Concepts**
   - Dynamic memory allocation
   - Memory fragmentation issues
   - Block splitting and merging

2. **Algorithm Implementation**
   - First Fit vs other allocation strategies
   - Trade-offs between speed and efficiency
   - Real-world OS memory management

3. **Software Engineering Practices**
   - Modular code design
   - Comprehensive testing
   - User interface design
   - Documentation standards

### Comparison with Other Algorithms

| Algorithm | Speed | Fragmentation | Implementation |
|-----------|-------|---------------|----------------|
| First Fit | Fast  | Moderate      | Simple         |
| Best Fit  | Slow  | Low           | Complex        |
| Worst Fit | Slow  | High          | Complex        |

## 🔮 Future Enhancements

Potential improvements for extended versions:

1. **Additional Algorithms**
   - Best Fit implementation
   - Worst Fit implementation
   - Next Fit variant

2. **Advanced Features**
   - Memory compaction
   - Buddy system allocation
   - Paging simulation

3. **Visualization**
   - Graphical memory map
   - Real-time fragmentation charts
   - Animation of allocation process

4. **Performance Analysis**
   - Benchmark different algorithms
   - Statistical fragmentation analysis
   - Memory access pattern simulation

## 🐛 Known Limitations

1. **Simplified Model**
   - No virtual memory simulation
   - No memory protection mechanisms
   - Single-threaded operation only

2. **Algorithm Scope**
   - Only implements First Fit
   - No memory compaction
   - No garbage collection

3. **Interface Constraints**
   - Command-line only (no GUI)
   - Manual process management
   - Limited visualization options

## 📝 Academic Notes

### First Fit Algorithm Analysis

**Advantages:**
- Fast allocation (stops at first suitable block)
- Simple implementation
- Good performance for varied request sizes

**Disadvantages:**
- Can create small unusable fragments at beginning of memory
- May not utilize memory optimally
- External fragmentation increases over time

**Real-World Usage:**
- Used in many early operating systems
- Still employed in embedded systems
- Foundation for more advanced algorithms

### Memory Management Context

This simulator provides a foundation for understanding:
- Operating system memory management
- Process memory allocation strategies
- System performance optimization
- Resource management principles

## 🤝 Contributing

This is an academic project designed for learning. Suggestions for improvements:

1. Fork the repository
2. Create a feature branch
3. Implement enhancements
4. Add corresponding tests
5. Update documentation
6. Submit a pull request

## 📄 License

This project is created for educational purposes. Feel free to use and modify for academic assignments and learning.

---

**Author**: Operating Systems Lab Project  
**Purpose**: Academic demonstration of First Fit memory management  
**Language**: Python 3.6+  
**Status**: Complete MVP Implementation