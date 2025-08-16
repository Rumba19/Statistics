"""
Python Statistics Calculator - Object-Oriented Approach
"""

from typing import List, Tuple, Union
from collections import Counter


class StatisticsCalculator:
    """
    A class to calculate basic statistics (mean, median, mode) on a list of integers.
    Demonstrates object-oriented programming principles with encapsulation.
    """
    
    def __init__(self, data: List[int] = None):
        """
        Initialize the StatisticsCalculator with optional data.
        
        Args:
            data: List of integers to analyze
        """
        self._data = data if data is not None else []
        self._original_data = self._data.copy()  # Keep original for reference
    
    def set_data(self, data: List[int]) -> None:
        """
        Set new data for analysis.
        
        Args:
            data: List of integers to analyze
        """
        self._data = data.copy()
        self._original_data = data.copy()
    
    def get_data(self) -> List[int]:
        """
        Get a copy of the current data.
        
        Returns:
            Copy of the current data list
        """
        return self._data.copy()
    
    def calculate_mean(self) -> float:
        """
        Calculate the mean (average) of the data.
        
        Returns:
            The mean as a float, or 0.0 if data is empty
        """
        if not self._data:
            return 0.0
        
        return sum(self._data) / len(self._data)
    
    def calculate_median(self) -> float:
        """
        Calculate the median (middle value) of the data.
        
        Returns:
            The median as a float, or 0.0 if data is empty
        """
        if not self._data:
            return 0.0
        
        sorted_data = sorted(self._data)
        n = len(sorted_data)
        
        if n % 2 == 0:
            # Even number of elements - average of two middle values
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2.0
        else:
            # Odd number of elements - middle value
            return float(sorted_data[n // 2])
    
    def calculate_mode(self) -> Tuple[List[int], int]:
        """
        Calculate the mode(s) (most frequently occurring value(s)) of the data.
        
        Returns:
            Tuple containing:
            - List of mode values (sorted)
            - Maximum frequency
        """
        if not self._data:
            return ([], 0)
        
        # Count frequencies using Counter
        frequency_counter = Counter(self._data)
        max_frequency = max(frequency_counter.values())
        
        # Find all values with maximum frequency
        modes = [value for value, freq in frequency_counter.items() 
                if freq == max_frequency]
        
        return (sorted(modes), max_frequency)
    
    def get_all_statistics(self) -> dict:
        """
        Calculate all statistics at once.
        
        Returns:
            Dictionary containing mean, median, and mode information
        """
        modes, mode_frequency = self.calculate_mode()
        
        return {
            'data': self.get_data(),
            'mean': self.calculate_mean(),
            'median': self.calculate_median(),
            'modes': modes,
            'mode_frequency': mode_frequency,
            'count': len(self._data)
        }
    
    def display_statistics(self) -> None:
        """Display all statistics in a formatted way."""
        stats = self.get_all_statistics()
        
        print(f"Data: {stats['data']}")
        print(f"Mean: {stats['mean']:.2f}")
        print(f"Median: {stats['median']:.2f}")
        
        if stats['modes']:
            modes_str = ', '.join(map(str, stats['modes']))
            print(f"Mode: {modes_str} (frequency: {stats['mode_frequency']})")
        else:
            print("Mode: No data")
        print()
    
    def add_value(self, value: int) -> None:
        """
        Add a single value to the dataset.
        
        Args:
            value: Integer value to add
        """
        self._data.append(value)
    
    def remove_value(self, value: int) -> bool:
        """
        Remove the first occurrence of a value from the dataset.
        
        Args:
            value: Integer value to remove
            
        Returns:
            True if value was found and removed, False otherwise
        """
        try:
            self._data.remove(value)
            return True
        except ValueError:
            return False
    
    def reset_data(self) -> None:
        """Reset data to the original dataset."""
        self._data = self._original_data.copy()
    
    def clear_data(self) -> None:
        """Clear all data."""
        self._data = []
        self._original_data = []
    
    def __str__(self) -> str:
        """String representation of the calculator."""
        return f"StatisticsCalculator(data={self._data})"
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"StatisticsCalculator(data={self._data}, count={len(self._data)})"


def demonstrate_oop_features():
    """Demonstrate object-oriented features of the StatisticsCalculator."""
    print("=== Object-Oriented Programming Features Demonstration ===\n")
    
    # Create calculator instance
    calc = StatisticsCalculator([1, 2, 2, 3, 3, 3, 4, 5])
    print(f"Initial calculator: {calc}")
    print("Initial statistics:")
    calc.display_statistics()
    
    # Add a value
    print("Adding value 3...")
    calc.add_value(3)
    calc.display_statistics()
    
    # Remove a value
    print("Removing value 2...")
    if calc.remove_value(2):
        print("Value removed successfully")
    calc.display_statistics()
    
    # Reset to original data
    print("Resetting to original data...")
    calc.reset_data()
    calc.display_statistics()


def main():
    """Main function to demonstrate the StatisticsCalculator."""
    print("=== Python Statistics Calculator (Object-Oriented Approach) ===\n")
    
    # Test datasets
    test_datasets = [
        [1, 2, 3, 4, 5],
        [1, 2, 2, 3, 4, 4, 4],
        [5, 5, 3, 3, 1, 1],
        [10]
    ]
    
    # Process each dataset
    for i, data in enumerate(test_datasets, 1):
        print(f"Test {i}:")
        calc = StatisticsCalculator(data)
        calc.display_statistics()
    
    # Demonstrate OOP features
    demonstrate_oop_features()


if __name__ == "__main__":
    main()