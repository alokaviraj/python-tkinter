from tkinter import * 
parent = Tk()  
name = Label(parent,text = "Name").grid(row = 00, column = 00)  
e1 = Entry(parent).grid(row = 0, column = 1)  
password = Label(parent,text = "Password").grid(row = 1, column = 00)  
e2 = Entry(parent).grid(row = 1, column = 1)  
submit = Button(parent, text = "Submit").grid(row = 40, column = 00)  
parent.mainloop()  
