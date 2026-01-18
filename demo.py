#!/usr/bin/env python3
"""
Quick demonstration of the First Fit Memory Manager
"""

from memory_manager import FirstFitMemoryManager

def main():
    print("First Fit Memory Management Demo")
    print("=" * 40)
    
    # Create memory manager with 1000 units
    mm = FirstFitMemoryManager(1000)
    
    print("Initial memory state:")
    mm.display_memory_map()
    
    # Allocate some memory
    print("\nAllocating memory:")
    mm.allocate_memory(1, 200)
    mm.allocate_memory(2, 150)
    mm.allocate_memory(3, 100)
    
    mm.display_memory_map()
    
    # Show status
    print("\nMemory status:")
    status = mm.get_memory_status()
    print(f"Total: {status['total_memory']}")
    print(f"Allocated: {status['total_allocated']}")
    print(f"Free: {status['total_free']}")
    
    # Deallocate middle process
    print("\nDeallocating process 2:")
    mm.deallocate_memory(2)
    mm.display_memory_map()
    
    # Show fragmentation
    mm.display_fragmentation_info()
    
    print("\nDemo completed successfully!")

if __name__ == "__main__":
    main()