from tkinter import *

COEF = 1.609344
PRECISION = 2

# Creating a new window and configurations
window = Tk()
window.title("Miles to km Converter")
window.minsize(width=100, height=100)

# Labels
label_miles = Label(text="Miles")
label_miles.grid(row=1, column=3)
label_equal = Label(text="is equal to")
label_equal.grid(row=2, column=1)
label_result = Label(text="0")
label_result.grid(row=2, column=2)
label_km = Label(text="km")
label_km.grid(row=2, column=3)

# Entries
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="0")
# Gets text in entry
entry.grid(row=1, column=2)


# Buttons
def action():
    miles_value = int(entry.get())
    # print(entry.get())
    km_value = round(miles_value * COEF, PRECISION)
    # print(miles_value)
    label_result.config(text=km_value)


# calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(row=3, column=2)

window.mainloop()
