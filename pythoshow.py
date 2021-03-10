import math
from tkinter import *
from pythogorean import calculate

def go():
    Label(window, text=" "*100).grid(row=4)
    global answer
    aval = a.get()
    bval = b.get()
    if aval and bval:
        answers = calculate(float(aval),float(bval))
        answer = Label(window, text="Answer: "+str(answers)).grid(row=3)

def exitt():
    exit(code="you suck")
window = Tk()
window.geometry("960x1080")
Label(window, text="What is A?").grid(row=0)
Label(window, text="What is B?").grid(row=1)
Button(window, text="Find Answer", command=go).grid(row=2)
Button(window, text="Exit", command=exitt)
a= Entry(window)
b = Entry(window)

a.grid(row=0, column=1)
b.grid(row=1, column=1)

window.mainloop()
