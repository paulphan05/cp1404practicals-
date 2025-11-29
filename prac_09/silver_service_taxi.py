"""
Prac 09 - SilverServiceTaxi
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent Silver Service Taxi Object."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise Silver Service Taxi Object."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of Silver Service Taxi Object."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the fare including flagfall."""
        return self.flagfall + super().get_fare()
