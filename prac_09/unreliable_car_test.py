"""
Prac 09 - UnreliableCar tests
"""

from unreliable_car import UnreliableCar


def main():
    """Test Unreliable Car Class."""
    test_car = UnreliableCar("Test", 1000, 30)

    success_count = 0

    for i in range(100):
        distance_driven = test_car.drive(1)
        if distance_driven > 0:
            success_count += 1

    print("Attempt to drive a car with 30% reliability")
    print(f"Out of 100 times, the test car drove {success_count} times.")

    main()
