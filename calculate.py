from tkinter import *

window = Tk()
window.title("Calculator")

e1 = Entry(window, width=35, borderwidth=5)
e1.grid(row=0, column=0, columnspan=4)

def clicked(number):
    current = e1.get()
    e1.delete(0, END)
    e1.insert(0, str(current) + str(number))


def button_clear():
    e1.delete(0, END)

def addition():
    first_num = e1.get()
    global first_number
    global math
    math = "addition"
    first_number = int(first_num)
    e1.delete(0, END)


def subtraction():
    first_num = e1.get()
    global first_number
    global math
    math = "subtraction"
    first_number = int(first_num)
    e1.delete(0, END)

def multiply():
    first_num = e1.get()
    global first_number
    global math
    math = "multiply"
    first_number = int(first_num)
    e1.delete(0, END)

def divide():
    first_num = e1.get()
    global first_number
    global math
    math = "divide"
    first_number = int(first_num)
    e1.delete(0, END)

def equals():
    second_num = e1.get()
    e1.delete(0, END)
    if math == "addition":
        e1.insert(0, first_number + int(second_num))
    if math == "subtraction":
        e1.insert(0, first_number - int(second_num))
    if math == "multiply":
        e1.insert(0, first_number * int(second_num))
    if math == "divide":
        e1.insert(0, first_number / int(second_num))



b1 = Button(window, text="7", width=8, command=lambda: clicked(7))
b1.grid(row=1, column=0)

b2 = Button(window, text="8", width=8, command=lambda: clicked(8))
b2.grid(row=1, column=1)

b3 = Button(window, text="9", width=8, command=lambda: clicked(9))
b3.grid(row=1, column=2)

b4 = Button(window, text="/", width=8, command=divide)
b4.grid(row=1, column=3)

b5 = Button(window, text="4", width=8, command=lambda: clicked(4))
b5.grid(row=2, column=0)

b6 = Button(window, text="5", width=8, command=lambda: clicked(5))
b6.grid(row=2, column=1)

b7 = Button(window, text="6", width=8, command=lambda: clicked(6))
b7.grid(row=2, column=2)

b8 = Button(window, text="*", width=8, command=multiply)
b8.grid(row=2, column=3)

b9 = Button(window, text="1", width=8, command=lambda: clicked(1))
b9.grid(row=3, column=0)

b10 = Button(window, text="2", width=8, command=lambda: clicked(2))
b10.grid(row=3, column=1)

b11 = Button(window, text="3", width=8, command=lambda: clicked(3))
b11.grid(row=3, column=2)

b12 = Button(window, text="+", width=8, command=addition)
b12.grid(row=3, column=3)

b13 = Button(window, text="C", width=8, command=button_clear)
b13.grid(row=4, column=0)

b14 = Button(window, text="0", width=8, command=lambda: clicked(0))
b14.grid(row=4, column=1)

b15 = Button(window, text="=", width=8, command=equals)
b15.grid(row=4, column=2)

b16 = Button(window, text="-", width=8, command=subtraction)
b16.grid(row=4, column=3)

window.mainloop()