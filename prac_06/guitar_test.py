"""
Estimated time: 40 minutes
Actual time: 32 minutes
"""
from prac_06.guitar import Guitar

CURRENT_YEAR = 2025

def run_tests():
    """Tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2016, 1512.9)