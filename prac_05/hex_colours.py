COLOUR_TO_HEX = {"ALICEBLUE": "#f0f8ff",
                 "ANTIQUEWHITE": "#faebd7",
                 "AQUA": "#00ffff",
                 "BEIGE": "#f5f5dc",
                 "CORAL": "#ff7f50",
                 "CRIMSON": "#dc143c",
                 "DARKVIOLET": "#9400d3",
                 "FULVOUS": "#e48400",
                 "GRAY": "#bebebe",
                 "LEMON": "#fff700"}

colour_name = input("Enter a colour name: ").upper()
while colour_name != "":
    if colour_name in COLOUR_TO_HEX:
        print(f"The code for {colour_name} is {COLOUR_TO_HEX[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").upper()
