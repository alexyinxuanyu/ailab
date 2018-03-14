from Tkinter import *
import tkMessageBox as messagebox
import pandas as pd
import seaborn as sns
from sklearn import datasets
import matplotlib.pyplot as plt

# iris = datasets.load_iris()

root = Tk()
root.title("hello world")
root.geometry('450x300')         


l1 = Label(root, text="xls name:")
l1.grid(row=0, column=0)
# l1.pack() 
xls_text = StringVar()
xls = Entry(root, textvariable = xls_text)
xls_text.set(" ")
# xls.pack()
xls.grid(row=0, column=1)


l2 = Label(root, text="sheet name:")
# l2.pack()  
l2.grid(row=1, column=0)
sheet_text = StringVar()
sheet = Entry(root, textvariable = sheet_text)
sheet_text.set(" ")
# sheet.pack()
sheet.grid(row=1, column=1)

l3 = Label(root, text="loop time:")
# l3.pack()  
l3.grid(row=2, column=0)

loop_text = StringVar()
loop = Entry(root, textvariable = loop_text)
loop_text.set(" ")
# loop.pack()
loop.grid(row=2, column=1)




l4 = Label(root, text="sleep time:")
# l4.pack()  
l4.grid(row=3, column=0)
sleep_text = StringVar()
sleep = Entry(root, textvariable = sleep_text)
sleep_text.set(" ")
# sleep.pack()
sleep.grid(row=3, column=1)

def on_click():
    x = xls_text.get()
    s = sheet_text.get()
    l = loop_text.get()
    sl = sleep_text.get()
    string = str("xls name:%s sheet name:%s loop time:%s sleep time:%s " %(x, s, l, sl))
    print("xls name:%s sheet name:%s loop time:%s sleep time:%s " %(x, s, l, sl))
    messagebox.showinfo(title='aaa', message = string)
def on_click1():
    sns.set(style="white",color_codes=True)
    iris=pd.read_csv("D:/dataset/iristraining.csv")
    iris.head()
    sns.FacetGrid(iris,hue="Species",size=4).map(plt.scatter,"SepalLengthCm","SepalWidthCm").add_legend()
    plt.show() 
    
def on_clickDT():
    sns.set(style="white",color_codes=True)
    iris=pd.read_csv("D:/dataset/decisiontreereal.csv")
    iris.head()
    sns.FacetGrid(iris,hue="Species",size=4).map(plt.scatter,"SepalLengthCm","SepalWidthCm").add_legend()
    plt.show()     
#     x = xls_text.get()
#     s = sheet_text.get()
#     l = loop_text.get()
#     sl = sleep_text.get()
#     string = str("xls name:%s sheet name:%s loop time:%s sleep time:%s " %(x, s, l, sl))
#     print("xls name:%s sheet name:%s loop time:%s sleep time:%s " %(x, s, l, sl))
#     messagebox.showinfo(title='aaa', message = string)


#Decision Tree
LK = Label(root, text="Decisiontree:")
LK.grid(row=4, column=0)    
LK = Label(root, text="IRIS DATABASE:")
LK.grid(row=4, column=1)    
b1=Button(root, text="press", compound='left',command = on_click,anchor='w')#.pack()
b1.grid(row=4, column=2,sticky=W)
# b1.configure(width=30,height=3)
# b1.pack()  

b2=Button(root, text="press2", compound='left',command = on_clickDT)#.pack()
b2.grid(row=4, column=3,sticky=W)
b3=Button(root, text="press3",compound='left', command = on_click)#.pack()
b3.grid(row=4, column=4,sticky=W)
b4=Button(root, text="press4",compound='left', command = on_click)#.pack()
b4.grid(row=4, column=5,sticky=W)

#KNN
LK = Label(root, text="KNN:")
LK.grid(row=5, column=0)    
LK = Label(root, text="IRIS DATABASE:")
LK.grid(row=5, column=1)    
b1=Button(root, text="press", compound='left',command = on_click,anchor='w')#.pack()
b1.grid(row=5, column=2,sticky=W)
# b1.configure(width=30,height=3)
# b1.pack()  

b2=Button(root, text="press2", compound='left',command = on_click1)#.pack()
b2.grid(row=5, column=3,sticky=W)
b3=Button(root, text="press3",compound='left', command = on_click)#.pack()
b3.grid(row=5, column=4,sticky=W)
b4=Button(root, text="press4",compound='left', command = on_click)#.pack()
b4.grid(row=5, column=5,sticky=W)


    

root.mainloop()