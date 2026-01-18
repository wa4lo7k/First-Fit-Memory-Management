#!/usr/bin/env python3
"""
Command Line Interface for First Fit Memory Management Simulator
Provides interactive menu-driven interface for memory operations.
"""

import sys
from memory_manager import FirstFitMemoryManager


class MemoryManagerCLI:
    """Command Line Interface for the Memory Management System."""
    
    def __init__(self, total_memory=1000):
        """Initialize CLI with memory manager."""
        self.memory_manager = FirstFitMemoryManager(total_memory)
        self.running = True
    
    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*60)
        print("FIRST FIT MEMORY MANAGEMENT SIMULATOR")
        print("="*60)
        print("1. Allocate Memory")
        print("2. Deallocate Memory")
        print("3. Display Memory Status")
        print("4. Display Memory Map")
        print("5. Show Allocation Log")
        print("6. Display Fragmentation Info")
        print("7. Exit Program")
        print("="*60)
    
    def get_user_input(self, prompt, input_type=str, validation=None):
        """
        Get validated user input.
        
        Args:
            prompt (str): Input prompt message
            input_type (type): Expected input type (int, str, etc.)
            validation (function): Optional validation function
            
        Returns:
            Validated user input
        """
        while True:
            try:
                user_input = input(prompt)
                
                if input_type == int:
                    value = int(user_input)
                else:
                    value = user_input
                
                if validation and not validation(value):
                    print("Invalid input. Please try again.")
                    continue
                
                return value
                
            except ValueError:
                print(f"Please enter a valid {input_type.__name__}.")
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                return None
    
    def handle_allocate_memory(self):
        """Handle memory allocation request."""
        print("\n--- ALLOCATE MEMORY ---")
        
        process_id = self.get_user_input(
            "Enter Process ID: ",
            int,
            lambda x: x > 0
        )
        
        if process_id is None:
            return
        
        memory_size = self.get_user_input(
            "Enter Memory Size (units): ",
            int,
            lambda x: x > 0
        )
        
        if memory_size is None:
            return
        
        print(f"\nAttempting to allocate {memory_size} units for process {process_id}...")
        success = self.memory_manager.allocate_memory(process_id, memory_size)
        
        if success:
            print("✓ Memory allocation successful!")
        else:
            print("✗ Memory allocation failed!")
        
        # Show recent log entry
        log = self.memory_manager.get_allocation_log()
        if log:
            print(f"Log: {log[-1]}")
    
    def handle_deallocate_memory(self):
        """Handle memory deallocation request."""
        print("\n--- DEALLOCATE MEMORY ---")
        
        process_id = self.get_user_input(
            "Enter Process ID to deallocate: ",
            int,
            lambda x: x > 0
        )
        
        if process_id is None:
            return
        
        print(f"\nAttempting to deallocate memory for process {process_id}...")
        success = self.memory_manager.deallocate_memory(process_id)
        
        if success:
            print("✓ Memory deallocation successful!")
        else:
            print("✗ Memory deallocation failed!")
        
        # Show recent log entry
        log = self.memory_manager.get_allocation_log()
        if log:
            print(f"Log: {log[-1]}")
    
    def handle_display_status(self):
        """Display current memory status."""
        print("\n--- MEMORY STATUS ---")
        status = self.memory_manager.get_memory_status()
        
        print(f"Total Memory: {status['total_memory']} units")
        print(f"Allocated: {status['total_allocated']} units")
        print(f"Free: {status['total_free']} units")
        print(f"Utilization: {status['memory_utilization']:.1f}%")
        print(f"Number of blocks: {len(status['blocks'])}")
        print(f"Free blocks: {status['free_block_count']}")
    
    def handle_display_memory_map(self):
        """Display detailed memory map."""
        self.memory_manager.display_memory_map()
    
    def handle_show_log(self):
        """Display allocation/deallocation log."""
        print("\n--- ALLOCATION LOG ---")
        log = self.memory_manager.get_allocation_log()
        
        if not log:
            print("No operations performed yet.")
            return
        
        print(f"Showing last {min(10, len(log))} entries:")
        print("-" * 60)
        
        for entry in log[-10:]:
            print(entry)
        
        if len(log) > 10:
            print(f"\n... and {len(log) - 10} earlier entries")
    
    def handle_fragmentation_info(self):
        """Display fragmentation analysis."""
        self.memory_manager.display_fragmentation_info()
    
    def run(self):
        """Main CLI loop."""
        print("Welcome to First Fit Memory Management Simulator!")
        print(f"Initialized with {self.memory_manager.total_memory} units of memory.")
        
        while self.running:
            try:
                self.display_menu()
                
                choice = self.get_user_input(
                    "Select an option (1-7): ",
                    int,
                    lambda x: 1 <= x <= 7
                )
                
                if choice is None:
                    continue
                
                if choice == 1:
                    self.handle_allocate_memory()
                elif choice == 2:
                    self.handle_deallocate_memory()
                elif choice == 3:
                    self.handle_display_status()
                elif choice == 4:
                    self.handle_display_memory_map()
                elif choice == 5:
                    self.handle_show_log()
                elif choice == 6:
                    self.handle_fragmentation_info()
                elif choice == 7:
                    self.running = False
                    print("\nThank you for using the Memory Management Simulator!")
                    print("Goodbye!")
                
                if self.running and choice != 7:
                    input("\nPress Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\nExiting program...")
                self.running = False
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                print("Please try again.")


def main():
    """Main entry point for the CLI application."""
    # Allow custom memory size via command line argument
    total_memory = 1000
    
    if len(sys.argv) > 1:
        try:
            total_memory = int(sys.argv[1])
            if total_memory <= 0:
                raise ValueError("Memory size must be positive")
        except ValueError as e:
            print(f"Invalid memory size: {e}")
            print("Using default size of 1000 units.")
            total_memory = 1000
    
    # Create and run CLI
    cli = MemoryManagerCLI(total_memory)
    cli.run()


if __name__ == "__main__":
    main()