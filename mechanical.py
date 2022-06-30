import tkinter as tk
from tkinter import ttk
# from PIL import Image, ImageTk
from math import pi,sqrt

root = tk.Tk()
root.title('Fluid flow rate')
root.geometry('1600x800')

# image = Image.open("engineering.jpg")
# photo = ImageTk.PhotoImage(image)
lbl = ttk.Label(root)
lbl.pack()

def get_value():
    P1 = float(a.get())
    D1 = float(b.get())
    P2 = float(e.get())
    D2 = float(f.get())
    density = float(i.get())
    g = float(j.get())
   
    A1 = (pi*(D1**2))/4

    A2 = (pi*(D2**2))/4

    k = A1/A2

    PH = (P1-P2)/(density*g)

    PH_3 = 0.03*PH

    PH_97 = 0.97*PH

    nume = 2*g*PH_97
    deno = (k**2)-1
    
    square_root = (nume/deno)**0.5
    Q = (A1*square_root)*1000

    Area1.set(str(A1))
    Area2.set(str(A2))
    Area_ratio.set(str(k))
    Pressure_head_3.set(str(PH_3))
    Pressure_head_97.set(str(PH_97))
    Pressure_head.set(str(PH))
    Flow_rate.set(str(Q))


Area1=tk.StringVar()    
Area2=tk.StringVar()
Area_ratio=tk.StringVar()
Pressure_head_3=tk.StringVar()
Pressure_head_97=tk.StringVar()
Pressure_head=tk.StringVar()
Flow_rate=tk.StringVar()

       
a = tk.StringVar()#
b = tk.StringVar()#
e = tk.StringVar()#
f = tk.StringVar()#
i = tk.StringVar()#
j = tk.StringVar()#


Top_label = tk.Label(root,text='MEASUREMENT OF FLOW RATE',bd=5,
               font=('arial',12,'bold'))
Top_label.pack(side='top')

#--------------------------The calculate button------------------------------------------------
btn = tk.Button(root,text='SOLVE',command=get_value,bg='midnightblue',bd=7,width=15)
btn.place(x=600,y=300)

# --------------------------P1 is pressure1--------------------- 
lbl = tk.Label(root,text='Pressure 1',font=('arial',12,'bold'),
               bd=5,fg='green')
lbl.place(x=0,y=80)#pady padx

p1 = tk.Entry(root,textvariable=a,width=20,font=('arial',12,'bold'),
              bd=5,fg='black',insertwidth=5)
p1.place(x=160,y=80)

lbl = tk.Label(root,text='Pa',font=('arial',12,'bold'),bd=5,fg='green')
lbl.place(x=370,y=80)

# --------------------D1 is diameter1-------------------------------- 
lbl = tk.Label(root,text='Diameter 1',font=('arial',12,'bold'),
               bd=5,fg='green')
lbl.place(x=0,y=160)

d1 = tk.Entry(root,width=20,textvariable=b,font=('arial',12,'bold'),
              bd=5,fg='black',insertwidth=5)
d1.place(x=160,y=160)

lbl = tk.Label(root,text='m',font=('arial',12,'bold'),bd=5,fg='green')
lbl.place(x=370,y=160)

# -----------------------A1 is area1----------------------------------- 
lbl = tk.Label(root,text='Area 1',font=('arial',12,'bold'),bd=5,fg='blue')
lbl.place(x=0,y=240)

a1 = tk.Entry(root,width=20,text=Area1,font=('arial',12,'bold'),
              bd=5,fg='black',insertwidth=5)
a1.place(x=160,y=240)

lbl = tk.Label(root,text='m²',font=('arial',12,'bold'),bd=5,fg='blue')
lbl.place(x=370,y=240)

# ---------------------K is diameter1----------------------------- 
lbl = tk.Label(root,text='K',font=('arial',12,'bold'),bd=5,fg='blue')
lbl.place(x=0,y=320)

K = tk.Entry(root,width=20,text=Area_ratio,font=('arial',12,'bold'),
             bd=5,fg='black',insertwidth=5)
K.place(x=160,y=320)

# -------------p_h is 3% pressure head--------------------- 
lbl = tk.Label(root,text='3% pressure head', font=('arial',12,'bold')
               ,bd=5,fg='blue')
lbl.place(x=0,y=400)

p_h = tk.Entry(root,width=20,text=Pressure_head_3,font=('arial',12,'bold'),
               bd=5,fg='black',insertwidth=5)
p_h.place(x=160,y=400)

lbl = tk.Label(root,text='m',font=('arial',12,'bold'),bd=5,fg='blue')
lbl.place(x=370,y=400)

# -------------D is Density--------------------- 
lbl = tk.Label(root,text='Density',font=('arial',12,'bold'),
               bd=5,fg='green')
lbl.place(x=0,y=480)

D = tk.Entry(root,textvariable=i,width=20,font=('arial',12,'bold'),
             bd=5,fg='black',insertwidth=5)
D.place(x=160,y=480)

lbl = tk.Label(root,text='kg/m³',font=('arial',12,'bold'),bd=5,fg='green')
lbl.place(x=370,y=480)

#-----------------------Right handside--------------------------------------------------

# -------------P2 is pressure1--------------------- 
lbl = tk.Label(root,text='Pressure 2',font=('arial',12,'bold'),bd=5,fg='green')
lbl.place(x=850,y=80)

p2 = tk.Entry(root,textvariable=e,width=20,font=('arial',12,'bold'),
              bd=5,fg='black',insertwidth=5)
p2.place(x=1020,y=80)

lbl = tk.Label(root,text='Pa',font=('arial',12,'bold'),bd=5,fg='green')
lbl.place(x=1230,y=80)

# -------------D2 is diameter1--------------------- 
lbl = tk.Label(root,text='Diameter 2',font=('arial',12,'bold'),
               bd=5,fg='green')
lbl.place(x=850,y=160)

d2 = tk.Entry(root,textvariable=f,width=20,font=('arial',12,'bold'),
              bd=5,fg='black',insertwidth=5)
d2.place(x=1020,y=160)

lbl = tk.Label(root,text='m',font=('arial',12,'bold'),bd=5,fg='green')
lbl.place(x=1230,y=160)

# -------------A2 is area2--------------------- 
lbl = tk.Label(root,text='Area 2',font=('arial',12,'bold'),bd=5,
               fg='blue')
lbl.place(x=850,y=240)

a2 = tk.Entry(root,width=20,text=Area2,font=('arial',12,'bold'),
              bd=5,fg='black',insertwidth=5)
a2.place(x=1020,y=240)

lbl = tk.Label(root,text='m²',font=('arial',12,'bold'),bd=5,fg='blue')
lbl.place(x=1230,y=240)

# -------------P_H is pressure head--------------------- 
lbl = tk.Label(root,text='Pressure head',font=('arial',12,'bold'),
               bd=5,fg='blue')
lbl.place(x=850,y=320)

P_H = tk.Entry(root,width=20,text=Pressure_head,font=('arial',12,'bold'),
               bd=5,fg='black',insertwidth=5)
P_H.place(x=1020,y=320)

lbl = tk.Label(root,text='m',font=('arial',12,'bold'),bd=5,fg='blue')
lbl.place(x=1230,y=320)

# -------------ph is 97% pressure head--------------------- 
lbl = tk.Label(root,text='97% pressure head',font=('arial',12,'bold'),
               bd=5,fg='blue')
lbl.place(x=850,y=400)

ph = tk.Entry(root,width=20,text=Pressure_head_97,font=('arial',12,'bold'),
              bd=5,fg='black',insertwidth=5)
ph.place(x=1020,y=400)

lbl = tk.Label(root,text='m',font=('arial',12,'bold'),bd=5,fg='blue')
lbl.place(x=1230,y=400)

# -------------G is Gravity--------------------- 
lbl = tk.Label(root,text='Gravity',font=('arial',12,'bold'),bd=5,fg='green')
lbl.place(x=850,y=480)

G = tk.Entry(root,textvariable=j,width=20,font=('arial',12,'bold'),
             bd=5,fg='black',insertwidth=5)
G.place(x=1020,y=480)

lbl = tk.Label(root,text='m/s²',font=('arial',12,'bold'),bd=5,fg='green')
lbl.place(x=1230,y=480)

#-------------F_R is flow rate--------------------- 
lbl = tk.Label(root,text='Flow rate',font=('arial',12,'bold'),bd=6,fg='indigo')
lbl.place(x=380,y=600)

F_R = ttk.Entry(root,width=24,text=Flow_rate,font=('arial',18,'bold'))
F_R.place(x=470,y=600)

lbl = tk.Label(root,text='litre/s',font=('arial',12,'bold'),bd=6,fg='indigo')
lbl.place(x=800,y=600)

root.mainloop()

