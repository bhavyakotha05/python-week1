"""
Personal Information Manager
This program stores and displays user's personal details.
"""

#Getting user input
name = input("Enter your name:")
age = input("Enter your age:")
city = input("Enter your city:")
hobbies = input("enter your hobbies (comma separated):")

#Displaying formatted information
print("\n--- Personal Information ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Hobbies: {hobbies}")

