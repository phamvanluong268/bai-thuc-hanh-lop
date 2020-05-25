from tkinter import*
def NewFile():
  print("New File!")
def OpenFile():
  print("Open File!")
def ExitFile():
  print("Exit File!")
def TextInsert():
  print("Text Insert!")
def PictureInsert():
  print("Picture Insert!")
def About():
  print("This is a simple example of a menu")
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)
filemenu=Menu(menu)
menu.add_cascade(label="Insert",menu=filemenu)
filemenu.add_command(label="Text", command=TextInsert)
filemenu.add_command(label="Picture", command=PictureInsert)
helpmenu=Menu(menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About...",command=About)
mainloop()
