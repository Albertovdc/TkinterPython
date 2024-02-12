import tkinter

def convert():
  miles = int(milesEntry.get())
  kilometers = miles * 1.60934
  kilometersOutput.config(text=f"{round(kilometers, 2)}")


# This mini project converts miles to kilometers
window = tkinter.Tk()
window.title("Miles to Kilometers")
window.minsize(width=300, height=100)
window.config(pady=50, padx=100)
# Add entry
milesEntry = tkinter.Entry(width=10)
milesEntry.grid(column=1, row=0)

# Add label km
kilometersOutput = tkinter.Label(text="0")
kilometersOutput.grid(column=1, row=1)

# Add the buttom
buttomCalculate = tkinter.Button(text="Calculate", command=convert)
buttomCalculate.grid(column=1, row=2)

# Add the labels
text1 = tkinter.Label(text="is equal to")
text2 = tkinter.Label(text="Miles")
text3 = tkinter.Label(text="Km")
text1.grid(column=0, row=1)
text2.grid(column=2, row=0)
text3.grid(column=2, row=1)




window.mainloop()