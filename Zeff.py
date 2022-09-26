from tkinter import *
from tkinter import ttk
import math

def Schatzler():
	w1=(int(a1.get())*int(n1.get()))/(int(a1.get())*int(n1.get())+int(n2.get())*int(a2.get()))
	w2=(int(a2.get())*int(n2.get()))/(int(a1.get())*int(n1.get())+int(n2.get())*int(a2.get()))
	z=(int(z1.get())*w1)+(int(z2.get())*w2)
	kq1.set(round(z,6))

def Harding():
	w1=(int(a1.get())*int(n1.get()))/(int(a1.get())*int(n1.get())+int(n2.get())*int(a2.get()))
	w2=(int(a2.get())*int(n2.get()))/(int(a1.get())*int(n1.get())+int(n2.get())*int(a2.get()))
	z=math.sqrt(((w1/int(a1.get()))*(int(z1.get())**3)+(w2/int(a2.get()))*(int(z2.get())**3))/((w1/int(a1.get()))*int(z1.get())+(w2/int(a2.get()))*int(z2.get())))
	kq2.set(round(z,6))

def TSAI():
	w1=(int(a1.get())*int(n1.get()))/(int(a1.get())*int(n1.get())+int(n2.get())*int(a2.get()))
	w2=(int(a2.get())*int(n2.get()))/(int(a1.get())*int(n1.get())+int(n2.get())*int(a2.get()))
	x=(w1/int(a1.get()))*int(z1.get())+(w2/int(a2.get()))*int(z2.get())
	z=pow((w1/int(a1.get()))*int(z1.get())*pow(int(z1.get()),3.4)/x+(w2/int(a2.get()))*int(z2.get())*pow(int(z2.get()),3.4)/x,1/3.4)
	kq3.set(round(z,6))

def clicked():
     messagebox.showinfo('Can\'t Run', 'Data Error!')

win=Tk()
win.title("Zeff-2")
win.geometry('300x260')
win.configure(bg='thistle')
win.resizable(0,0)
win.iconbitmap(r"C:\đề tài\Khoá luận tốt nghiệp\Zeff\incon.ico")
kq1=StringVar()
kq2=StringVar()
kq3=StringVar()

tab_control=ttk.Notebook(win)
tab1=ttk.Frame(tab_control)
tab2=ttk.Frame(tab_control)
tab3=ttk.Frame(tab_control)

tab_control.add(tab1, text='Schatzler')
tab_control.add(tab2, text='Harding',)
tab_control.add(tab3, text=' TSAI ')

fr1=Frame(win, bg='thistle')
fr1.pack(fill=X)
lb1=Label(fr1, text='Z1',width=5,bg='thistle')
lb1.pack(side=LEFT, padx=5,pady=5)
z1=Entry(fr1)
z1.pack(padx=10 ,expand=True)

fr2=Frame(win,bg='thistle')
fr2.pack(fill=X)
lb2=Label(fr2, text='Z2', width=5,bg='thistle')
lb2.pack(side=LEFT, padx=5,pady=5)
z2=Entry(fr2)
z2.pack(padx=10, expand=True)

fr3=Frame(win,bg='thistle')
fr3.pack(fill=X)
lb3=Label(fr3, text='A1', width=5,bg='thistle')
lb3.pack(side=LEFT, padx=5,pady=5)
a1=Entry(fr3)
a1.pack(padx=10, expand=True)

fr4=Frame(win,bg='thistle')
fr4.pack(fill=X)
lb4=Label(fr4, text='A2', width=5,bg='thistle')
lb4.pack(side=LEFT, padx=5,pady=5)
a2=Entry(fr4)
a2.pack(expand=True)

fr5=Frame(win,bg='thistle')
fr5.pack(fill=X)
lb5=Label(fr5, text='n1', width=5,bg='thistle')
lb5.pack(side=LEFT, padx=5,pady=5)
n1=Entry(fr5)
n1.pack(padx=10, expand=True)

fr6=Frame(win,bg='thistle')
fr6.pack(fill=X)
lb6=Label(fr6, text='n2', width=5,bg='thistle')
lb6.pack(side=LEFT, padx=5,pady=5)
n2=Entry(fr6)
n2.pack(expand=True)

sovle=Button(win, text='=',font=("Tahoma",15),command=lambda:[Schatzler(),Harding(),TSAI()])
sovle.pack(side=RIGHT, padx=5, pady=15)

fr7=Frame(tab1)
fr7.pack(fill=X)
lb7=Label(fr7, text='Result', width=5)
lb7.pack(side=LEFT,padx=10,pady=15)
en=Entry(fr7, textvariable=kq1, width=25, bg='lavender').pack(pady=15,expand=True)


fr8=Frame(tab2)
fr8.pack(fill=X)
lb8=Label(fr8, text='Result', width=5)
lb8.pack(side=LEFT,padx=10,pady=15)
en2=Entry(fr8, textvariable=kq2, width=25, bg='bisque').pack(pady=15,expand=True)


fr9=Frame(tab3)
fr9.pack(fill=X)
lb9=Label(fr9, text='Result', width=5)
lb9.pack(side=LEFT,padx=10,pady=15)
en3=Entry(fr9, textvariable=kq3, width=25, bg='lightcoral').pack(pady=15,expand=True)


z1.focus()
tab_control.pack(expand=1, fill='both')

win.mainloop()