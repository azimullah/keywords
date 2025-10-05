from tkinter import *

window = Tk()
window.title("number pad")
window.geometry("250x430")

num = [
    [9,8,7,],
    [6,5,4,],
    [3,2,1,],
    ['#' ,0,"*"]
]


for i in range(4):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for J in range(3):
        frame = Frame(
            master=window,
            relief=SUNKEN,
            borderwidth=1)
        frame.grid(row=i, column=J)
        label=Label(master=frame, text=num[i][J])

        label.pack(padx=1, pady=1)

window.mainloop()