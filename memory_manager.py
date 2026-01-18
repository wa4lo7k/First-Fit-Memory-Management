#!/usr/bin/env python3
"""
First Fit Memory Management Simulator
Operating Systems Lab Project - MVP Implementation

This module implements a First Fit memory allocation algorithm simulation
suitable for academic evaluation and understanding of OS memory management.
"""

class MemoryBlock:
    """Represents a single memory block in the system."""
    
    def __init__(self, start_address, size, is_free=True, process_id=None):
        self.start_address = start_address
        self.size = size
        self.is_free = is_free
        self.process_id = process_id
    
    def __str__(self):
        status = "FREE" if self.is_free else f"ALLOCATED (PID: {self.process_id})"
        return f"Block[{self.start_address}-{self.start_address + self.size - 1}]: {self.size} units - {status}"


class FirstFitMemoryManager:
    """
    First Fit Memory Management System
    
    Implements First Fit allocation algorithm with support for:
    - Memory allocation using first available block
    - Memory deallocation with adjacent block merging
    - Fragmentation tracking and reporting
    """
    
    def __init__(self, total_memory=1000):
        """Initialize memory manager with specified total memory size."""
        self.total_memory = total_memory
        self.memory_blocks = [MemoryBlock(0, total_memory, True)]
        self.allocation_log = []
    
    def allocate_memory(self, process_id, size):
        """
        Allocate memory using First Fit algorithm.
        
        Args:
            process_id (int): Unique identifier for the process
            size (int): Amount of memory requested
            
        Returns:
            bool: True if allocation successful, False otherwise
        """
        if size <= 0:
            self.allocation_log.append(f"ERROR: Invalid size {size} for process {process_id}")
            return False
        
        # Check if process already has memory allocated
        for block in self.memory_blocks:
            if not block.is_free and block.process_id == process_id:
                self.allocation_log.append(f"ERROR: Process {process_id} already has memory allocated")
                return False
        
        # First Fit: Find first free block large enough
        for i, block in enumerate(self.memory_blocks):
            if block.is_free and block.size >= size:
                # Allocate the block
                block.is_free = False
                block.process_id = process_id
                
                # Split block if there's remaining space
                if block.size > size:
                    remaining_size = block.size - size
                    block.size = size
                    
                    # Create new free block for remaining space
                    new_block = MemoryBlock(
                        block.start_address + size,
                        remaining_size,
                        True
                    )
                    self.memory_blocks.insert(i + 1, new_block)
                
                self.allocation_log.append(
                    f"SUCCESS: Allocated {size} units to process {process_id} "
                    f"at address {block.start_address}"
                )
                return True
        
        self.allocation_log.append(
            f"ERROR: Cannot allocate {size} units for process {process_id} - "
            f"No suitable free block found"
        )
        return False
    
    def deallocate_memory(self, process_id):
        """
        Deallocate memory for a specific process.
        
        Args:
            process_id (int): Process identifier to deallocate
            
        Returns:
            bool: True if deallocation successful, False otherwise
        """
        # Find the allocated block for this process
        for i, block in enumerate(self.memory_blocks):
            if not block.is_free and block.process_id == process_id:
                # Free the block
                block.is_free = True
                block.process_id = None
                
                self.allocation_log.append(
                    f"SUCCESS: Deallocated memory for process {process_id} "
                    f"({block.size} units at address {block.start_address})"
                )
                
                # Merge with adjacent free blocks
                self._merge_free_blocks()
                return True
        
        self.allocation_log.append(f"ERROR: Process {process_id} has no allocated memory")
        return False
    
    def _merge_free_blocks(self):
        """Merge adjacent free blocks to reduce external fragmentation."""
        i = 0
        while i < len(self.memory_blocks) - 1:
            current = self.memory_blocks[i]
            next_block = self.memory_blocks[i + 1]
            
            # Merge if both blocks are free and adjacent
            if (current.is_free and next_block.is_free and 
                current.start_address + current.size == next_block.start_address):
                
                current.size += next_block.size
                self.memory_blocks.pop(i + 1)
                self.allocation_log.append(
                    f"INFO: Merged free blocks at {current.start_address} "
                    f"(total size: {current.size})"
                )
            else:
                i += 1
    
    def get_memory_status(self):
        """
        Get current memory status and fragmentation information.
        
        Returns:
            dict: Memory status including blocks, fragmentation data
        """
        total_free = sum(block.size for block in self.memory_blocks if block.is_free)
        total_allocated = sum(block.size for block in self.memory_blocks if not block.is_free)
        
        # Calculate fragmentation
        free_blocks = [block for block in self.memory_blocks if block.is_free]
        external_fragmentation = len(free_blocks) - (1 if free_blocks else 0)
        
        # Internal fragmentation is minimal in this simulation
        # (would occur with fixed-size blocks in real systems)
        internal_fragmentation = 0
        
        return {
            'blocks': self.memory_blocks,
            'total_memory': self.total_memory,
            'total_free': total_free,
            'total_allocated': total_allocated,
            'free_block_count': len(free_blocks),
            'external_fragmentation': external_fragmentation,
            'internal_fragmentation': internal_fragmentation,
            'memory_utilization': (total_allocated / self.total_memory) * 100
        }
    
    def display_memory_map(self):
        """Display current memory map in a formatted table."""
        print("\n" + "="*70)
        print("MEMORY MAP")
        print("="*70)
        print(f"{'Start':<8} {'End':<8} {'Size':<8} {'Status':<12} {'Process ID':<10}")
        print("-"*70)
        
        for block in self.memory_blocks:
            end_addr = block.start_address + block.size - 1
            status = "FREE" if block.is_free else "ALLOCATED"
            pid = "-" if block.is_free else str(block.process_id)
            
            print(f"{block.start_address:<8} {end_addr:<8} {block.size:<8} "
                  f"{status:<12} {pid:<10}")
        
        print("-"*70)
    
    def display_fragmentation_info(self):
        """Display detailed fragmentation information."""
        status = self.get_memory_status()
        
        print("\n" + "="*50)
        print("FRAGMENTATION ANALYSIS")
        print("="*50)
        print(f"Total Memory: {status['total_memory']} units")
        print(f"Allocated Memory: {status['total_allocated']} units")
        print(f"Free Memory: {status['total_free']} units")
        print(f"Memory Utilization: {status['memory_utilization']:.1f}%")
        print(f"Free Block Count: {status['free_block_count']}")
        print(f"External Fragmentation: {status['external_fragmentation']} extra blocks")
        print(f"Internal Fragmentation: {status['internal_fragmentation']} units")
        print("="*50)
    
    def get_allocation_log(self):
        """Return the allocation/deallocation log."""
        return self.allocation_log.copy()