from tkinter import *


def miles_to_km():
    miles = miles_input.get()
    km = float(miles) * 1.609
    converted.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

converted = Label(text="0")
converted.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=2,row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()
