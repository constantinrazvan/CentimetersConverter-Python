import math
from tkinter import *

# You can use math.floor(height_converted) if you want an integer
# Do not forget! The library is already imported!

#TODO: Import Tkinter and make a GUI

print("*****************************************************************")
print("*********************** HEIGHT CONVERTER ************************")
print("**** Convert your centimeters to inches, yards, meters, feet ****")
print("*****************************************************************")

root = Tk()
frame = Frame(root)

root.title("Centimeter Converter")

welcome_text = Label(root, text ='Welcome!', font = "50")
print("Hi! Thank you for trying this height converter")
height_converter = str(input("What height you want to convert? (inches, feet, meters, yards) \n"))

if height_converter == "inches":
    height_value = int(input("What value of height you want to convert? \n Value: "))
    height_converted = height_value / 2.54
    print(f"Your height converted in inches is:", height_converted, "in")

elif height_converter == "feet":
    height_value = int(input("What value of height you want to convert? \n Value:"))
    height_converted = height_value / 30.48
    print(f"Your height converted in feet is:", height_converted, "ft")

elif height_converter == "meters":
    height_value = int(input("What value of height you want to convert? \n Value:"))
    height_converted = height_value / 100
    print(f"Your height converted in meters is:", height_converted, "m")

elif height_converter == "yards":
    height_value = int(input("What value of height you want to convert? \n Value:"))
    height_converted = height_value *  0.010936133
    print(f"Your height converted in yards is:", height_converted, "y")

else:
    print(f"Your input is invalid")

root.mainloop()
