from symPy import symbols 
from tkinter import *
# import lab_calc
root= Tk()

print(2*symbols("x"))
root.title="labs calculation"
header_label=Label(root, text="Labs Calculator")
header_label.grid(row=0, column=0)

sigma_e=Entry(root)
entry1.pack()
entry1.insert(0, "Enter data")

# def call_back():
#     data=entry1.get().split(",")
#     for item in data:
#         print (item)

button1=Button(root, text="click", command=call_back)
button1.pack()



root.mainloop()
