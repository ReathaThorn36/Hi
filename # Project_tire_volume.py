# tire_volume.py

import math
from datetime import datetime

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive integer.")

# Get user input
print("Tire Volume Calculator")
width = get_positive_int("Enter the width of the tire in mm (e.g., 205): ")
aspect_ratio = get_positive_int("Enter the aspect ratio of the tire (e.g., 60): ")
diameter = get_positive_int("Enter the diameter of the wheel in inches (e.g., 15): ")

# Calculate the volume
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10_000_000_000
print(f"The approximate volume is {volume:.2f} liters.")

# Optional: Alert for unusual sizes
if volume < 10:
    print("Note: This seems smaller than expected.")
elif volume > 100:
    print("Note: This seems larger than expected.")

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Optionally collect user contact
name = input("Enter your name (optional): ").strip()
phone = input("Enter your phone number (optional): ").strip()

# Log data to file
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {name}, {phone}\n")
