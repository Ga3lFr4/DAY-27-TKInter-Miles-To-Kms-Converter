from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(pady=20, padx=20)


def miles_to_km():
    new_text = int(entry.get()) * 1.609
    converted_int_label.config(text=str(new_text))


def km_to_miles():
    new_text = round((int(entry.get()) / 1.609), 3)
    converted_int_label.config(text=str(new_text))


def km_conversion():
    window.title("Km to Miles Converter")
    to_convert_label.config(text="Km")
    converted_label.config(text="Miles")
    converted_int_label.config(text=0)
    calc_button.config(command=km_to_miles)
    change_conversion_button.config(text="Miles to Km", command=miles_conversion)


def miles_conversion():
    window.title("Miles to Km Converter")
    to_convert_label.config(text="Miles")
    converted_label.config(text="Km")
    converted_int_label.config(text=0)
    calc_button.config(command=miles_to_km)
    change_conversion_button.config(text="Km to Miles", command=km_conversion)



entry = Entry(width=10)
entry.grid(column=1, row=0)

to_convert_label = Label(text="Miles")
to_convert_label.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

converted_int_label = Label(text=0)
converted_int_label.grid(column=1, row=1)

converted_label = Label(text="Km")
converted_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)

change_conversion_button = Button(text="Km to Miles", command=km_conversion)
change_conversion_button.grid(column=0, row=2)

window.mainloop()
