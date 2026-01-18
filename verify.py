#!/usr/bin/env python3
import sys
print("Python version:", sys.version)
print("Testing basic functionality...")

try:
    from memory_manager import FirstFitMemoryManager
    print("✓ Memory manager imported successfully")
    
    mm = FirstFitMemoryManager(100)
    print("✓ Memory manager created")
    
    result = mm.allocate_memory(1, 50)
    print(f"✓ Allocation result: {result}")
    
    status = mm.get_memory_status()
    print(f"✓ Status retrieved: {status['total_allocated']} allocated")
    
    print("All basic tests passed!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()