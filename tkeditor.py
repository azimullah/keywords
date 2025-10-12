from tkinter import *
from tkinter .filedialog import askopenfilename, asksaveasfilename, askopenfilename, asksaveasfilename

window = Tk()
window.title("Text Editor")
window.geometry("600x500")
window.rowconfigure(0,minsize = 600, weight=1)
window.columnconfigure(1,minsize = 600, weight=1)

def open_file():
    global txt_edit
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"Text Editor - {filepath}")

def save_file():
    global txt_edit
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
        window.title(f"Text Editor - {filepath}")

txt_edit = Text(window)
fr_button = Frame(window, relief=RAISED, bd=2)
button_open = Button(fr_button, text="Open", command=open_file)
button_save = Button(fr_button, text="Save As...", command=save_file)

button_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_button.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()