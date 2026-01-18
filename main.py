#!/usr/bin/env python3
"""
First Fit Memory Management Simulator - Main Entry Point
Operating Systems Lab Project

This is the main entry point for the First Fit Memory Management MVP.
Run this file to start the interactive CLI interface.
"""

import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cli_interface import main as cli_main


def display_welcome():
    """Display welcome message and project information."""
    print("="*70)
    print("FIRST FIT MEMORY MANAGEMENT SIMULATOR")
    print("Operating Systems Lab Project - MVP Implementation")
    print("="*70)
    print()
    print("This simulator demonstrates First Fit memory allocation algorithm")
    print("used in operating systems for process memory management.")
    print()
    print("Features:")
    print("• First Fit allocation algorithm")
    print("• Memory deallocation with block merging")
    print("• Fragmentation analysis and reporting")
    print("• Interactive command-line interface")
    print("• Comprehensive logging and status display")
    print()
    print("Usage:")
    print("  python main.py [memory_size]")
    print("  python main.py 2000    # Start with 2000 units of memory")
    print()
    print("="*70)
    print()


def main():
    """Main entry point with enhanced user experience."""
    display_welcome()
    
    # Check for help flag
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        print("HELP - First Fit Memory Management Simulator")
        print()
        print("This program simulates the First Fit memory allocation algorithm.")
        print()
        print("Command line options:")
        print("  python main.py              # Use default 1000 units")
        print("  python main.py <size>       # Specify memory size")
        print("  python main.py --help       # Show this help")
        print()
        print("Interactive Commands:")
        print("  1. Allocate Memory    - Assign memory to a process")
        print("  2. Deallocate Memory  - Free memory from a process")
        print("  3. Display Status     - Show memory utilization")
        print("  4. Display Memory Map - Show detailed memory layout")
        print("  5. Show Log          - View allocation/deallocation history")
        print("  6. Fragmentation Info - Analyze memory fragmentation")
        print("  7. Exit              - Quit the program")
        print()
        print("Algorithm Details:")
        print("• First Fit scans memory blocks sequentially")
        print("• Allocates the first free block large enough for the request")
        print("• Splits blocks when allocated size < block size")
        print("• Merges adjacent free blocks during deallocation")
        print("• Tracks internal and external fragmentation")
        return
    
    try:
        # Start the CLI interface
        cli_main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please check your input and try again.")


if __name__ == "__main__":
    main()