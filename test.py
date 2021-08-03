from tkinter import *
parent=Tk()    
name = Label(parent,text="name").grid(row=0,column=0)
e1 = Entry(parent).grid(row = 0, column = 1)
email = Label(parent, text = "Email").grid(row=1, column = 0)
e2 = Entry(parent).grid(row = 1, column = 1)  
password = Label(parent,text = "Password").grid(row =2 , column = 0)  
e2 = Entry(parent).grid(row = 2, column = 1)
checkvar1 = IntVar()  
  
checkvar2 = IntVar()  
  
checkvar3 = IntVar()  
  
chkbtn1 = Checkbutton(parent, text = "C", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
chkbtn2 = Checkbutton(parent, text = "C++", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
chkbtn3 = Checkbutton(parent, text = "python", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
chkbtn1.grid()  
  
chkbtn2.grid()  
  
chkbtn3.grid()  
parent.mainloop()


