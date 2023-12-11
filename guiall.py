#small GUI Window
# from tkinter import *

# root = Tk()
# root.mainloop()

#GUI Example
# from tkinter import *

# # creating root window 
# root = Tk()

# # customizing root window title 
# root.title("Welcome to Python Lobby")
# # customizing root window dimension 
# root.geometry('300x200')

# root.mainloop()

#Labels in Tkinter
# from tkinter import *

# # creating root window
# root = Tk()

# # customizing root window title
# root.title("Welcome to Python Lobby")
# # customizing root window dimension
# root.geometry('250x200')

# # placing label to our GUI app
# lbl = Label(root, text = "We are Python Lobby-ian")
# lbl.pack()

# root.mainloop()



# #Labels in GUI 
# from tkinter import *

# # creating root window
# root = Tk()

# # customizing root window title
# root.title("Welcome to Python Lobby")
# # customizing root window dimension
# root.geometry('250x200')

# # placing label to our GUI app
# name = "We are Python Lobby-ian"
# lbl = Label(root, text = name, font=("Helvetica", 12), fg = 'white' , bg='black')
# lbl.pack()

# root.mainloop()



#Button in python GUI
# from tkinter import *

# # creating root window
# root = Tk()
# root.title("Welcome to Python Lobby")
# # function defined which is called when button is clicked
# def clicked():
#     print("I am clicked")
# # placing Button to our GUI app
# btn = Button(root, text="Click me", command = clicked)
# btn.pack()
# root.geometry('250x200')
# root.mainloop()


# Entry Widget in GUI python
# from tkinter import *

# # creating root window
# root = Tk()
# root.title("Welcome to Python Lobby")

# # placing Entry widget to our GUI app
# entry = Entry(root)
# entry.pack()

# root.geometry('250x200')
# root.mainloop()



# geometry manager - pack
# from tkinter import *

# root = Tk()

# w = Label(root, text="Red Zone", bg="red", fg="white")
# w.pack()
# w = Label(root, text="Green Glossy", bg="light green", fg="white")
# w.pack()
# w = Label(root, text="Yellow Yuga", bg="yellow", fg="red")
# w.pack()

# root.geometry("250x140")
# root.mainloop()


# from tkinter import *

# root = Tk()
# root.title("PythonLobby")

# w = Label(root, text="Red Zone", bg="red", fg="white")
# w.grid(row=0, column=0)
# w = Label(root, text="Green Glossy", bg="light green", fg="white")
# w.grid(row=1, column=1)
# w = Label(root, text="Yellow", bg="yellow", fg="red")
# w.grid(row=2, column=2)

# root.geometry("250x150")
# root.mainloop()


#checkbutton
# from tkinter import *

# root = Tk()
# root.title("PythonLobby")
# w = Label(root, text='PythonLobby.Com', font="60")
# w.pack()

# Checkbox1 = IntVar()
# Checkbox2 = IntVar()

# Button0 = Checkbutton(root, text="Learning",
#                       variable=Checkbox1,
#                       onvalue=1,#checked
#                       offvalue=0,#unchecked
#                       height=3,
#                       width=12)

# Button1 = Checkbutton(root, text="Tutorial",
#                       variable=Checkbox2,
#                       onvalue=1,
#                       offvalue=0,
#                       height=3,
#                       width=12)

# Button0.pack()
# Button1.pack()

# root.geometry("320x220")
# mainloop() 


#radio button
# Importing Tkinter module
# from tkinter import *

# root = Tk()
# root.title("PythonLobby")

# # Tkinter string variable it can store any string value
# value1 = StringVar(root, "2")

# rbtn1 = Radiobutton(root, text="Radio Button 1", variable = value1 , value="1")
# rbtn1.pack()
# rbtn2 = Radiobutton(root, text="Radio Button 2", variable = value1 , value="2")
# rbtn2.pack()
# rbtn3 = Radiobutton(root, text="Radio Button 3", variable = value1 , value="3")
# rbtn3.pack()

# root.geometry("250x200")
# mainloop()

#combobox
# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# var = tk.StringVar()
# fruit = ttk.Combobox(root, width = 27, textvariable = var)

# # Adding combobox drop down list
# fruit['values'] = (' Guava', ' Mango', ' Apple', ' Banana',)

# fruit.pack(pady=20)

# # Setting Apple as a default
# fruit.current(2)

# root.geometry('350x250')
# root.title("PythonLobby")
# root.mainloop()

#spinbox
# from tkinter import *

# #creating root window
# root = Tk()

# year= IntVar()
# #creating spinbox
# sbox = Spinbox(root, from_ = 1990, to = 2018, textvariable = year)
# sbox.pack(pady=20)

# root.geometry('350x250')
# root.title("PythonLobby")
# root.mainloop()

#messagebox
# from tkinter import *
# from tkinter import messagebox

# #creating root window
# root = Tk()

# #function_definitions
# def callback():
#     messagebox.showinfo("Well Done Great !")
#     print("You Clicked Delete")

# #button 1
# button1 = Button(root, text="Delete", command = callback )
# button1.grid(row=0, column=0, padx=90, pady=50)

# root.geometry('350x250')
# root.title("PythonLobby")
# root.mainloop()

# from tkinter import *
# from tkinter import messagebox

# #creating root window
# root = Tk()

# #function_definitions
# def callback():
#     m_box = messagebox.askquestion("Delete", "Are you sure !", icon="warning")
#     if(m_box == "yes"):
#         print("Yes")
#     else:
#         print("No")

# #button 1
# button1 = Button(root, text="Info", command = callback )
# button1.grid(row=0, column=0, padx=90, pady=50)


# root.geometry('350x250')
# root.title("PythonLobby")
# root.mainloop()

#frame
# from tkinter import *

# #root window
# root = Tk()
# #label
# label = Label(root, text ='Python Lobby', font = "60")
# label.pack()
# #bottom frame
# bottom_frame = Frame(root, bg="green", width=120, height=100)
# bottom_frame.pack(side=LEFT, padx=20)
# #top_frame
# top_frame = Frame(root, bg="red", width=120, height=100)
# top_frame.pack(side=LEFT)

# root.geometry("300x150")
# root.mainloop()

#paned window
from tkinter import *
from tkinter import ttk

root = Tk()
#Paned Window
pw = ttk.PanedWindow(root, orient=HORIZONTAL)
pw.pack(fill=BOTH, expand=True)
frame1 = ttk.Frame(pw, relief=SUNKEN)
frame2 = ttk.Frame(pw, relief=SUNKEN)
pw.add(frame1, weight=1)
pw.add(frame2,weight=3)

root.geometry("400x240")
root.title("PythonLobby.com")
root.mainloop()