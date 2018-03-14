from Tkinter import *
def rtnkey(event=None):
    print(e.get())
root = Tk()
e = StringVar()
entry = Entry(root, validate='key', textvariable=e, width=50)
entry.pack()
entry.bind('<Return>', rtnkey)
root.title('get the entry')
root.mainloop()