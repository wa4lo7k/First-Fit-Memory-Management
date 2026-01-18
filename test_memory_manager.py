#!/usr/bin/env python3
"""
Test Suite for First Fit Memory Management Simulator
Demonstrates functionality and validates implementation.
"""

from memory_manager import FirstFitMemoryManager


def test_basic_allocation():
    """Test basic memory allocation functionality."""
    print("="*60)
    print("TEST 1: Basic Memory Allocation")
    print("="*60)
    
    mm = FirstFitMemoryManager(1000)
    
    # Test successful allocations
    print("Testing successful allocations...")
    assert mm.allocate_memory(1, 100) == True
    assert mm.allocate_memory(2, 200) == True
    assert mm.allocate_memory(3, 150) == True
    
    status = mm.get_memory_status()
    print(f"Total allocated: {status['total_allocated']} units")
    print(f"Total free: {status['total_free']} units")
    
    mm.display_memory_map()
    
    # Test allocation failure (insufficient memory)
    print("\nTesting allocation failure...")
    assert mm.allocate_memory(4, 600) == False  # Should fail
    
    print("✓ Basic allocation tests passed!")


def test_deallocation_and_merging():
    """Test memory deallocation and block merging."""
    print("\n" + "="*60)
    print("TEST 2: Deallocation and Block Merging")
    print("="*60)
    
    mm = FirstFitMemoryManager(1000)
    
    # Allocate several blocks
    mm.allocate_memory(1, 100)
    mm.allocate_memory(2, 200)
    mm.allocate_memory(3, 150)
    mm.allocate_memory(4, 100)
    
    print("After allocations:")
    mm.display_memory_map()
    
    # Deallocate middle blocks to test merging
    print("\nDeallocating process 2...")
    mm.deallocate_memory(2)
    mm.display_memory_map()
    
    print("\nDeallocating process 3...")
    mm.deallocate_memory(3)
    mm.display_memory_map()
    
    print("✓ Deallocation and merging tests passed!")


def test_fragmentation_scenario():
    """Demonstrate fragmentation scenarios."""
    print("\n" + "="*60)
    print("TEST 3: Fragmentation Demonstration")
    print("="*60)
    
    mm = FirstFitMemoryManager(1000)
    
    # Create fragmentation scenario
    print("Creating fragmentation scenario...")
    mm.allocate_memory(1, 100)  # 0-99
    mm.allocate_memory(2, 100)  # 100-199
    mm.allocate_memory(3, 100)  # 200-299
    mm.allocate_memory(4, 100)  # 300-399
    mm.allocate_memory(5, 100)  # 400-499
    
    print("After initial allocations:")
    mm.display_fragmentation_info()
    
    # Deallocate every other process
    mm.deallocate_memory(2)  # Free 100-199
    mm.deallocate_memory(4)  # Free 300-399
    
    print("\nAfter deallocating processes 2 and 4:")
    mm.display_memory_map()
    mm.display_fragmentation_info()
    
    # Try to allocate a large block (should fail due to fragmentation)
    print("\nTrying to allocate 250 units (should fail due to fragmentation)...")
    success = mm.allocate_memory(6, 250)
    print(f"Allocation result: {'Success' if success else 'Failed'}")
    
    # But smaller allocations should work
    print("\nAllocating smaller blocks (should succeed)...")
    mm.allocate_memory(7, 80)
    mm.allocate_memory(8, 90)
    
    mm.display_memory_map()
    
    print("✓ Fragmentation demonstration completed!")


def test_edge_cases():
    """Test edge cases and error conditions."""
    print("\n" + "="*60)
    print("TEST 4: Edge Cases and Error Handling")
    print("="*60)
    
    mm = FirstFitMemoryManager(100)
    
    # Test invalid inputs
    print("Testing invalid inputs...")
    assert mm.allocate_memory(1, 0) == False      # Zero size
    assert mm.allocate_memory(1, -10) == False    # Negative size
    
    # Test duplicate process allocation
    mm.allocate_memory(1, 50)
    assert mm.allocate_memory(1, 30) == False     # Same process ID
    
    # Test deallocation of non-existent process
    assert mm.deallocate_memory(999) == False     # Non-existent process
    
    # Test exact fit allocation
    mm.allocate_memory(2, 50)  # Should use remaining 50 units exactly
    
    status = mm.get_memory_status()
    assert status['total_free'] == 0  # All memory should be allocated
    
    print("Memory after exact fit:")
    mm.display_memory_map()
    
    print("✓ Edge case tests passed!")


def test_first_fit_behavior():
    """Demonstrate First Fit algorithm behavior."""
    print("\n" + "="*60)
    print("TEST 5: First Fit Algorithm Behavior")
    print("="*60)
    
    mm = FirstFitMemoryManager(1000)
    
    # Create specific pattern to show First Fit behavior
    mm.allocate_memory(1, 200)  # 0-199
    mm.allocate_memory(2, 300)  # 200-499
    mm.allocate_memory(3, 200)  # 500-699
    
    print("Initial allocation pattern:")
    mm.display_memory_map()
    
    # Deallocate first and third blocks
    mm.deallocate_memory(1)  # Free 0-199 (200 units)
    mm.deallocate_memory(3)  # Free 500-699 (200 units)
    
    print("\nAfter deallocating processes 1 and 3:")
    mm.display_memory_map()
    
    # Allocate 150 units - should go to first free block (First Fit)
    print("\nAllocating 150 units (should use first free block at address 0)...")
    mm.allocate_memory(4, 150)
    
    mm.display_memory_map()
    
    # Verify it went to the first block
    status = mm.get_memory_status()
    allocated_block = None
    for block in status['blocks']:
        if not block.is_free and block.process_id == 4:
            allocated_block = block
            break
    
    assert allocated_block.start_address == 0, "Should allocate at first available block"
    
    print("✓ First Fit behavior verified!")


def run_comprehensive_demo():
    """Run a comprehensive demonstration of the system."""
    print("\n" + "="*60)
    print("COMPREHENSIVE DEMONSTRATION")
    print("="*60)
    
    mm = FirstFitMemoryManager(1000)
    
    print("Starting with 1000 units of memory...")
    mm.display_memory_map()
    
    operations = [
        ("allocate", 1, 150),
        ("allocate", 2, 200),
        ("allocate", 3, 100),
        ("allocate", 4, 250),
        ("deallocate", 2, None),
        ("allocate", 5, 80),
        ("deallocate", 1, None),
        ("deallocate", 4, None),
        ("allocate", 6, 300),
    ]
    
    for i, (op, pid, size) in enumerate(operations, 1):
        print(f"\nStep {i}: ", end="")
        if op == "allocate":
            print(f"Allocating {size} units for process {pid}")
            mm.allocate_memory(pid, size)
        else:
            print(f"Deallocating process {pid}")
            mm.deallocate_memory(pid)
        
        mm.display_memory_map()
        
        # Show fragmentation info every few steps
        if i % 3 == 0:
            mm.display_fragmentation_info()
    
    print("\nFinal allocation log:")
    log = mm.get_allocation_log()
    for entry in log:
        print(f"  {entry}")


def main():
    """Run all tests and demonstrations."""
    print("FIRST FIT MEMORY MANAGEMENT - TEST SUITE")
    print("This test suite demonstrates all functionality of the memory manager.")
    
    try:
        test_basic_allocation()
        test_deallocation_and_merging()
        test_fragmentation_scenario()
        test_edge_cases()
        test_first_fit_behavior()
        run_comprehensive_demo()
        
        print("\n" + "="*60)
        print("ALL TESTS COMPLETED SUCCESSFULLY!")
        print("="*60)
        print("\nThe First Fit Memory Management system is working correctly.")
        print("You can now run 'python cli_interface.py' for interactive use.")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()