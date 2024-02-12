import tkinter

window = tkinter.Tk()
window.title("Test on tkinter.")
window.minsize(width=500, height=250)
window.config(padx=50, pady=50)

# Add labels
label = tkinter.Label(text="Hello World!")
label.grid(column=0, row=0) # Add the label to the window

def buttom_clicked():
  label.config(text=entry.get())


# Add buttom
buttom = tkinter.Button(text="Click", command=buttom_clicked)
buttom.grid(column= 2, row=1)

# Add new buttom
buttomSecondary = tkinter.Button(text="Click 2", command=buttom_clicked)
buttomSecondary.grid(column= 3, row= 0)

# Add entry
entry =tkinter.Entry(width=10)
entry.grid(column= 4, row= 2)


window.mainloop()
