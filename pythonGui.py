import tkinter
from math import *



def calculate(event):
    gleichung = t.get()
    print(gleichung)
    global ergebnis
    
    ergebnis = str(eval(gleichung))
    t.delete(0,tkinter.END)
    t.insert(0,ergebnis)
 
    
    

top = tkinter.Tk()

t = tkinter.Entry(top)
t.grid(row=0,columnspan = 4)

b1 = tkinter.Button(top, text="1")
b1.grid(row=1,column=0)

b2 = tkinter.Button(top, text="2")
b2.grid(row=1,column=1)

b3 = tkinter.Button(top, text="3")
b3.grid(row=1,column=2)

bp = tkinter.Button(top, text="+")
bp.grid(row=1,column=3)



b4 = tkinter.Button(top, text="4")
b4.grid(row=2,column=0)

b5 = tkinter.Button(top, text="5")
b5.grid(row=2,column=1)

b6 = tkinter.Button(top, text="6")
b6.grid(row=2,column=2)


bm = tkinter.Button(top, text="-")
bm.grid(row=2,column=3)




b7 = tkinter.Button(top, text="7")
b7.grid(row=3,column=0)

b8 = tkinter.Button(top, text="8")
b8.grid(row=3,column=1)

b9 = tkinter.Button(top, text="9")
b9.grid(row=3,column=2)

bg = tkinter.Button(top, text="/")
bg.grid(row=3,column=3)




bb = tkinter.Button(top, text="Berechnen")
bb.grid(row=4,column=1)

b1.bind('<Button-1>', lambda x: t.insert(tkinter.END, "1"))
b2.bind('<Button-1>', lambda x: t.insert(tkinter.END, "2"))
b3.bind('<Button-1>', lambda x: t.insert(tkinter.END, "3"))
b4.bind('<Button-1>', lambda x: t.insert(tkinter.END, "4"))
b5.bind('<Button-1>', lambda x: t.insert(tkinter.END, "5"))
b6.bind('<Button-1>', lambda x: t.insert(tkinter.END, "6"))
b7.bind('<Button-1>', lambda x: t.insert(tkinter.END, "7"))
b8.bind('<Button-1>', lambda x: t.insert(tkinter.END, "8"))
b9.bind('<Button-1>', lambda x: t.insert(tkinter.END, "9"))

bp.bind('<Button-1>', lambda x: t.insert(tkinter.END, "+"))
bm.bind('<Button-1>', lambda x: t.insert(tkinter.END, "-"))
bg.bind('<Button-1>', lambda x: t.insert(tkinter.END, "/"))

bb.bind('<Button-1>', calculate)


top.mainloop()