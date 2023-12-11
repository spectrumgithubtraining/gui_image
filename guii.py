# from tkinter import *


# root = Tk()

 

# def motion(event):

#     x, y = event.x, event.y

#     print('{}, {}'.format(x, y))

#     return x

 

# m=root.bind('<B1-Motion>', motion)

# print(m)

# root.mainloop()


# from tkinter import *              #import tkinter package


# master = Tk(className='SampleTkinter')
# master.mainloop()


# To resize the main Window:
# master.geometry("500x500")
#label widget
# from tkinter import *


# root = Tk()
# root.geometry("450x300")

# # the label for user_name
# user_name = Label(root,
# 				text = "Username").place(x = 40,
# 										y = 60)

# # the label for user_password
# user_password = Label(root,
# 					text = "Password").place(x = 40,
# 											y = 100)

# # submit_button = Button(root,
# # 					text = "Submit").place(x = 40,
# # 											y = 130)

# user_name_input_area = Entry(root,
# 							width = 30).place(x = 110,
# 											y = 60)

# user_password_entry_area = Entry(root,
# 								width = 30).place(x = 110,
# 												y = 100)
	
# root.mainloop()

#button widgets
# from tkinter import *
# root=Tk()
# root.geometry("450x300")

# def button_action():
# 	print("Hi")


# butt_obj=Button(root,text="CLICK",command=button_action)#tkinter button with specific action to be done.


# butt_obj.pack()#to get our particular widget to our tkinter  window
# root.mainloop()

#image display
from tkinter import *
root=Tk()
root.geometry("450x350")
photo = PhotoImage(file="png-clipart-lavender-flowers-lavender-thumbnail.png")#to display image

lbl = Label(root,image=photo).place(x=100,y=100)


root.mainloop()

