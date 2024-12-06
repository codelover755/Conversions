from tkinter import *


open = Tk()
open.geometry("525x100")
open.title("Conversion")
open.config(background="gray20")

def calculations():
    kg = float(kginput.get())
    g = kg * 1000
    lb = kg * 2.205
    oz = kg * 35.274
    gtext.delete("1.0",END)
    ltext.delete("1.0",END)
    oztext.delete("1.0",END)
    gtext.insert(END,g)
    ltext.insert(END,lb)
    oztext.insert(END,oz)
    

kglabel = Label(open,text="Enter the weight in Kg",fg="black",font=("Comic Sans MS",11))
glabel = Label(open,text="Gram",fg="black",font=("Comic Sans MS",11))
lblabel = Label(open,text="Pounds",fg="black",font=("Comic Sans MS",11))
ozlabel = Label(open,text="Ounce",fg="black",font=("Comic Sans MS",11))

kginput = Entry(open)
gtext = Text(open, height=1,width=20)
ltext = Text(open, height=1, width=20)
oztext = Text(open, height=1, width=20)

show = Button(open,text="Convert",fg="black",command=calculations)

kglabel.grid(row=1,column=1,padx=5, pady=5)
kginput.grid(row=1,column=2,padx=5, pady=5)
show.grid(row=1,column=3,padx=5, pady=5)
glabel.grid(row=2,column=1,padx=5, pady=5)
lblabel.grid(row=2,column=2,padx=5, pady=5)
ozlabel.grid(row=2,column=3,padx=5, pady=5)
gtext.grid(row=3,column=1,padx=5, pady=5)
ltext.grid(row=3,column=2,padx=5, pady=5)
oztext.grid(row=3,column=3,padx=5, pady=5)

open.mainloop()