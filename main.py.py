from tkinter import *


FONT = ("Georgia", 18)
PADDING = 10


def convert():
    miles = float(miles_num.get())
    km = round(miles * 1.609344, 2)
    kilometers_num.config(text=str(km))


window = Tk()
window.title("My first GUI App")
window.minsize(width=500, height=400)
window.maxsize(width=1000, height=800)
window.config(padx=40, pady=40)


miles_str = Label(text="Miles", font=FONT)
miles_str.grid(column=2, row=0)
miles_str.config(padx=PADDING, pady=PADDING)

is_equal_to = Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=PADDING, pady=PADDING)

kilometers_num = Label(text="0", font=FONT)
kilometers_num.grid(column=1, row=1)
kilometers_num.config(padx=PADDING, pady=PADDING)


kilometers_str = Label(text="Km", font=FONT)
kilometers_str.grid(column=2, row=1)
kilometers_str.config(padx=PADDING, pady=PADDING)

miles_num = Entry()
miles_num.grid(column=1, row=0)
miles_num.config(width=10)


calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)
calculate.config(padx=PADDING, pady=PADDING)

window.mainloop()
