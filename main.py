from tkinter import *
from tkinter import ttk
import pyperclip
import definitions

root = Tk()
root.title("Library")



easyAccessButtons = Frame(master=root).grid(row=1, column=1)

copysign = Button(master=easyAccessButtons, text=" \u00a9 ", command=definitions.copyCopySign).grid(row=1, column=1, sticky=(N,E,S,W), padx=5, pady=5)
micro = Button(master=easyAccessButtons, text=" \u03bc ", command=definitions.copyMicro).grid(row=1, column=2, sticky=(N,E,S,W), padx=5, pady=5)
theta = Button(master=easyAccessButtons, text=" \u03b8 ", command=definitions.copyTheta).grid(row=1, column=3, sticky=(N,E,S,W), padx=5, pady=5)
ohm = Button(master=easyAccessButtons, text=" \u03a9 ", command=definitions.copyOhm).grid(row=1, column=4, sticky=(N,E,S,W), padx=5, pady=5)
angstrom = Button(master=easyAccessButtons, text=" \u00c5 ", command=definitions.copyAngstrom).grid(row=1, column=5, sticky=(N,E,S,W), padx=5, pady=5)
plusminus = Button(master=easyAccessButtons, text=" \u00b1 ", command=definitions.copyPlusMinus).grid(row=2, column=1, sticky=(N,E,S,W), padx=5, pady=5)
permille = Button(master=easyAccessButtons, text=" \u2030 ", command=definitions.copyPermille).grid(row=2, column=2, sticky=(N,E,S,W), padx=5, pady=5)
sqrt = Button(master=easyAccessButtons, text=" \u221a ", command=definitions.copySqrt).grid(row=2, column=3, sticky=(N,E,S,W), padx=5, pady=5)
acute = Button(master=easyAccessButtons, text=" \u02ca ", command=definitions.copyAcute).grid(row=2, column=4, sticky=(N,E,S,W), padx=5, pady=5)
grave = Button(master=easyAccessButtons, text=" \u02cb ", command=definitions.copyGrave).grid(row=2, column=5, sticky=(N,E,S,W), padx=5, pady=5)
section = Button(master=easyAccessButtons, text=" \u00a7 ", command=definitions.copySection).grid(row=3, column=1, sticky=(N,E,S,W), padx=5, pady=5)
cent = Button(master=easyAccessButtons, text=" \u00a2 ", command=definitions.copyCent).grid(row=3, column=2, sticky=(N,E,S,W), padx=5, pady=5)









root.mainloop()