from taxi import Taxi


def main():
    # Create a new taxi object
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km
    my_taxi.drive(40)

    # Print taxi details and the current fare
    print(my_taxi)
    print(f"The current fare: ${my_taxi.get_fare():.2f}")

    # Restart the meter
    my_taxi.start_fare()

    # Drive the car 100 km
    my_taxi.drive(100)

    # Print the details and the current fare
    print(my_taxi)
    print(f"The current fare: ${my_taxi.get_fare():.2f}")


main()
