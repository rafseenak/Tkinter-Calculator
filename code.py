from tkinter import *

window = Tk()
window.geometry("520x550")
window.title("CALCULATOR")
window.configure(bg="gray")





def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def btequal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")


def btclr():
    global expression
    expression = ""
    input_text.set("")



expression = ""
input_text = StringVar()

input_frame = Frame(window, width=600, height=50, bd=0, bg="gray")
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 20, 'bold'), textvariable=input_text, width=25, justify=RIGHT)
input_field.pack(ipady=200, ipadx=200)
input_field.grid(row=0, column=0, pady=30)

btn_frame = Frame(window, width=312, height=280, bg="grey")
btn_frame.pack()

b1 = Button(btn_frame, text=1, width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click(1))
b1.grid(row=1, column=0, pady=20, padx=10)

b2 = Button(btn_frame, text=2, width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click(2))
b2.grid(row=1, column=1, pady=20, padx=10)

b3 = Button(btn_frame, text=3, width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click(3))
b3.grid(row=1, column=2, pady=20, padx=10)

b4 = Button(btn_frame, text=4, width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click(4))
b4.grid(row=2, column=0, pady=20, padx=10)

b5 = Button(btn_frame, text=5, width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click(5))
b5.grid(row=2, column=1, pady=20, padx=10)

b6 = Button(btn_frame, text=6, width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click(6))
b6.grid(row=2, column=2, pady=20, padx=10)

b7 = Button(btn_frame, text=7, width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click(7))
b7.grid(row=3, column=0, pady=20, padx=10)

b8 = Button(btn_frame, text=8, width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click(8))
b8.grid(row=3, column=1, pady=20, padx=10)

b9 = Button(btn_frame, text=9, width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click(9))
b9.grid(row=3, column=2, pady=20, padx=10)

bdot = Button(btn_frame, text=".", width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click("."))
bdot.grid(row=4, column=0, pady=20, padx=10)

b0 = Button(btn_frame, text=0, width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click(0))
b0.grid(row=4, column=1, pady=20, padx=10)

bequal = Button(btn_frame, text="=", width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=btequal)
bequal.grid(row=4, column=2, pady=20, padx=10)

bplus = Button(btn_frame, text="+", width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click("+"))
bplus.grid(row=1, column=3, pady=20, padx=10)

bmin = Button(btn_frame, text="-", width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click("-"))
bmin.grid(row=2, column=3, pady=20, padx=10)

bdiv = Button(btn_frame, text="/", width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click("/"))
bdiv.grid(row=3, column=3, pady=20, padx=10)

bmul = Button(btn_frame, text="X", width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=lambda: btn_click("*"))
bmul.grid(row=4, column=3, pady=20, padx=10)

bclr = Button(btn_frame, text="CLR", width=10, height=2, background="black", fg="white", font=('arial', 12, 'bold'), command=btclr)
bclr.grid(row=5, columnspan=4, pady=20, padx=10)




window.mainloop()