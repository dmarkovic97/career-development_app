from tkinter import *

# === Korisnicke funkcije pocetak


class DMMButton(Button):
    def __init__(self, master,**kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = 'aquamarine'

    def on_leave(self, e):
        self['background'] = self.defaultBackground

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=740,height=450)
    
def mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def ignore(event):
    return"break"

#**********************************************************************************************************
        #Uvod***
#************************************************************************************************
def korak0_1():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Opšte o karijeri",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')
     
     global img
     img=PhotoImage(file="slike\\opste_o_karijeri.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=pocetna,text='Početna',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak0_2,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)
     
def korak0_2():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Koraci u razvoju karijere",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\koraci_u_razvoju_karijere.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak0_1,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=pocetna,text = 'Početna', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

#**********************************************************************************************
#***  KORAK - 1 ***
#**********************************************************************************************
def korak1_1():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Pojam karijere",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak1_1.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=pocetna,text='Početna',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak1_2,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)
     
def korak1_2():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Karijera nekad i sad",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak1_2.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak1_1,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak1_3, text = 'Dalje',compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)
     
def korak1_3():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Teorije razvoja karijere",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak1_3.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak1_2,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak1_4, text = 'Dalje',compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)
     
def korak1_4():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Holland-ov heksagonalni model izbora karijere",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak1_4.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak1_3,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak1_5, text = 'Dalje',compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)
     
def korak1_5():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     # Omogućujemo skrolovanje
     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')
     canvas.bind_all("<MouseWheel>",mouse_wheel)
     main_frame1=Frame(canvas,bg='mediumturquoise')
     myscrollbar=Scrollbar(main_frame,orient="vertical",command=canvas.yview)
     canvas.configure(yscrollcommand=myscrollbar.set)
    
     myscrollbar.pack(side="right",fill="y")
     canvas.pack(side="left")
     canvas.create_window((0,0),window=main_frame1,anchor='nw')
     main_frame1.bind("<Configure>",myfunction)

     f4 = LabelFrame(main_frame1,bg='mediumturquoise', text="Karakteristike etapa razvoja karijere",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global img
     img=PhotoImage(file="slike\\korak1_5.png")
     im=Label(f4,image=img,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img3
     img3=PhotoImage(file="slike\\korak1_5_1.png")
     im3=Label(f4,image=img3,bd=10,bg='mediumturquoise')
     im3.grid(row=1, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak1_4,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=2, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=pocetna, text = 'Početna',compound = LEFT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=2, column=1)

#**********************************************************************************************
#***  KORAK - 2 ***
#**********************************************************************************************
def korak2_1():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Lični karijerni plan",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')
     
     global img
     img=PhotoImage(file="slike\\korak2_1.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=pocetna,text='Početna',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak2_2,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)
     
def korak2_2():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     # Omogućujemo skrolovanje
     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')
     canvas.bind_all("<MouseWheel>",mouse_wheel)

     main_frame1=Frame(canvas,bg='mediumturquoise')
     myscrollbar=Scrollbar(main_frame,orient="vertical",command=canvas.yview)
     canvas.configure(yscrollcommand=myscrollbar.set)

     myscrollbar.pack(side="right",fill="y")
     canvas.pack(side="left")
     canvas.create_window((0,0),window=main_frame1,anchor='nw')
     main_frame1.bind("<Configure>",myfunction)

     f4 = LabelFrame(main_frame1,bg='mediumturquoise', text="SWOT",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global img
     img=PhotoImage(file="slike\\korak2_2.png")
     im=Label(f4,image=img,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img3
     img3=PhotoImage(file="slike\\korak2_2_1.png")
     im3=Label(f4,image=img3,bd=10,bg='mediumturquoise')
     im3.grid(row=1, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak2_1,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=2, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak2_3, text = 'Dalje',compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=2, column=1)

def korak2_3():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Saznajte više o sebi",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak2_3.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak2_2,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak2_4, text = 'Dalje',compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak2_4():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Veštine, znanja, kompetencije",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak2_4.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak2_3,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak2_5, text = 'Dalje',compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak2_5():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Veštine koje je poželjno znati",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak2_5.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak2_4,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=pocetna, text = 'Početna',compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak3_1():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Zapošljivost",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak3_1.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=pocetna,text='Početna',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak3_2,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak3_2():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Osnovni pojmovi",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak3_2.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak3_1,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak3_3, text = 'Dalje',compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak3_3():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Ključna znanja, veštine i kompetencije koje vode zapošljavanju ",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak3_3.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak3_2,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak3_4, text = 'Dalje',compound = RIGHT,bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak3_4():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Ključna znanja, veštine i kompetencije koje vode zapošljavanju ",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak3_4.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak3_3,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak3_5, text = 'Dalje',compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)
     
def korak3_5():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     # Omogućujemo skrolovanje
     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')
     canvas.bind_all("<MouseWheel>",mouse_wheel)

     main_frame1=Frame(canvas,bg='mediumturquoise')
     myscrollbar=Scrollbar(main_frame,orient="vertical",command=canvas.yview)
     canvas.configure(yscrollcommand=myscrollbar.set)

     myscrollbar.pack(side="right",fill="y")
     canvas.pack(side="left")
     canvas.create_window((0,0),window=main_frame1,anchor='nw')
     main_frame1.bind("<Configure>",myfunction)

     f4 = LabelFrame(main_frame1,bg='mediumturquoise', text="Oblasti koje NSZ navodi kao prioritetne",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global img
     img=PhotoImage(file="slike\\korak3_5.png")
     im=Label(f4,image=img,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img3
     img3=PhotoImage(file="slike\\korak3_5_1.png")
     im3=Label(f4,image=img3,bd=10,bg='mediumturquoise')
     im3.grid(row=1, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak3_4,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=2, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak3_6, text = 'Dalje',compound = RIGHT,bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=2, column=1)

def korak3_6():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Najtraženija zanimanja narednih decenija ",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak3_6.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak3_5,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=pocetna, text = 'Početna',compound = RIGHT,bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)
     
def korak4_1():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="KOLIKO STE UPUĆENI U POJAM TRŽIŠTE RADA?",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak4_1.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=pocetna,text='Početna',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak4_2,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak4_2():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     # Omogućujemo skrolovanje
     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')
     canvas.bind_all("<MouseWheel>",mouse_wheel)

     main_frame1=Frame(canvas,bg='mediumturquoise')
     myscrollbar=Scrollbar(main_frame,orient="vertical",command=canvas.yview)
     canvas.configure(yscrollcommand=myscrollbar.set)

     myscrollbar.pack(side="right",fill="y")
     canvas.pack(side="left")
     canvas.create_window((0,0),window=main_frame1,anchor='nw')
     main_frame1.bind("<Configure>",myfunction)

     f4 = LabelFrame(main_frame1,bg='mediumturquoise', text="Karijerno vođenje",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global img
     img=PhotoImage(file="slike\\korak4_2.png")
     im=Label(f4,image=img,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img3
     img3=PhotoImage(file="slike\\korak4_2_1.png")
     im3=Label(f4,image=img3,bd=10,bg='mediumturquoise')
     im3.grid(row=1, column=0,columnspan=2)

     global img4
     img4=PhotoImage(file="slike\\korak4_2_2.png")
     im4=Label(f4,image=img4,bd=10,bg='mediumturquoise')
     im4.grid(row=2, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak4_1,text = 'Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=3, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak4_3, text = 'Dalje',compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=3, column=1)

def korak4_3():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Tipovi ličnosti",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak4_3.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak4_2,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak4_4,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak4_4():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Tehnički fakultet u Boru",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak4_4.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak4_3,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak4_5,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak4_5():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Rudarsko inženjerstvo",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak4_5.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak4_4,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak4_6,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak4_6():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Metalurško inženjerstvo",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak4_6.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak4_5,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak4_7,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak4_7():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Tehnološko inženjerstvo",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak4_7.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak4_6,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak4_8,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak4_8():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Inženjerski menadžment",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak4_8.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak4_7,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=pocetna,text = 'Početna', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak5_1():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Važni koraci u nalaženju prvog posla",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak5_1.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=pocetna,text='Početna',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak5_2,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak5_2():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Istraživanje pre podnošenja prijave za posao",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak5_2.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak5_1,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak5_3,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak5_3():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Mobilne aplikacije za pomoćpri traženju posla",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak5_3.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak5_2,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=pocetna,text = 'Početna', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak6_1():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     # Omogućujemo skrolovanje
     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')
     canvas.bind_all("<MouseWheel>",mouse_wheel)

     main_frame1=Frame(canvas,bg='mediumturquoise')
     myscrollbar=Scrollbar(main_frame,orient="vertical",command=canvas.yview)
     canvas.configure(yscrollcommand=myscrollbar.set)

     myscrollbar.pack(side="right",fill="y")
     canvas.pack(side="left")
     canvas.create_window((0,0),window=main_frame1,anchor='nw')
     main_frame1.bind("<Configure>",myfunction)

     f4 = LabelFrame(main_frame1,bg='mediumturquoise', text="Šta je to CV ili Curriculum vitae ?",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global img
     img=PhotoImage(file="slike\\korak6_1_1.png")
     im=Label(f4,image=img,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img3
     img3=PhotoImage(file="slike\\korak6_1_2.png")
     im3=Label(f4,image=img3,bd=10,bg='mediumturquoise')
     im3.grid(row=1, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=pocetna, text = 'Početna',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=2, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak6_2, text = 'Dalje',compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=2, column=1)

def korak6_2():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Lični podaci ",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak6_2.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak6_1,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak6_3,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak6_3():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Formalno obrazovanje",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak6_3.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak6_2,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak6_4,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak6_4():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Radno iskustvo",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak6_4.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak6_3,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak6_5,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak6_5():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Poznavanje stranih jezika",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak6_5.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak6_4,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak6_6,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak6_6():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Lične osobine/ Veštine/ Sposobnosti",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak6_6.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak6_5,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak6_7,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak6_7():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Ostalo (hobiji, interesovanja, dodatne sposobnosti)",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak6_7.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak6_6,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak6_8,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)
     
     canvas.bind_all("<MouseWheel>",ignore)

def korak6_8():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     # Omogućujemo skrolovanje
     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')
     canvas.bind_all("<MouseWheel>",mouse_wheel)

     main_frame1=Frame(canvas,bg='mediumturquoise')
     myscrollbar=Scrollbar(main_frame,orient="vertical",command=canvas.yview)
     canvas.configure(yscrollcommand=myscrollbar.set)

     myscrollbar.pack(side="right",fill="y")
     canvas.pack(side="left")
     canvas.create_window((0,0),window=main_frame1,anchor='nw')
     main_frame1.bind("<Configure>",myfunction)

     f4 = LabelFrame(main_frame1,bg='mediumturquoise', text="Saveti",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global img
     img=PhotoImage(file="slike\\korak6_8_1.png")
     im=Label(f4,image=img,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img3
     img3=PhotoImage(file="slike\\korak6_8_2.png")
     im3=Label(f4,image=img3,bd=10,bg='mediumturquoise')
     im3.grid(row=1, column=0,columnspan=2)

     global img4
     img4=PhotoImage(file="slike\\korak6_8_3.png")
     im4=Label(f4,image=img4,bd=10,bg='mediumturquoise')
     im4.grid(row=2, column=0,columnspan=2)

     global img5
     img5=PhotoImage(file="slike\\korak6_8_4.png")
     im5=Label(f4,image=img5,bd=10,bg='mediumturquoise')
     im5.grid(row=3, column=0,columnspan=2)

     global img6
     img6=PhotoImage(file="slike\\korak6_8_5.png")
     im6=Label(f4,image=img6,bd=10,bg='mediumturquoise')
     im6.grid(row=4, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img2,command=korak6_7,text = 'Nazad',compound=RIGHT,bg='teal',font=('Calibri',12,'bold'))
     b1.grid(row=5, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=pocetna, text = 'Početna',compound = LEFT, bg='teal',font=('Calibri',12,'bold'))
     b2.grid(row=5, column=1)


def korak7_1():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Razgovor za posao (Intervju)",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak7_1.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=pocetna,text='Početna',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak7_2,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak7_2():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="20 najčešće postavljanih pitanja na intervjuu",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak7_2.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak7_1,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak7_3,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak7_3():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Šta potencijalni poslodavci očekuju da saznaju tokom intervjua?",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak7_3.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak7_2,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak7_4,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak7_4():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Ponašanje kandidata tokom razgovora za posao",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak7_4.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak7_3,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak7_5,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak7_5():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Savremene metode selekcije kandidata",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak7_5.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak7_4,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=pocetna,text = 'Početna', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak8_1():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Postavljanje i dostizanje karijernog cilja",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak8_1.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=pocetna,text='Početna',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak8_2,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak8_2():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Uloga organizacije u razvoju karijere zaposlenih",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak8_2.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak8_1,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=korak8_3,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def korak8_3():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Aktivnosti organizacije na podršci i razvoju karijera zaposlenih",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\korak8_3.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=korak8_2,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=pocetna,text = 'Početna', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

#**********************************************************************************************
#***  POMOC ***
#**********************************************************************************************

def info():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="Informacije",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\informacije.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=pocetna,text='Početna',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=autori,text = 'Dalje', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

def autori():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     f4 = LabelFrame(main_frame,bg='mediumturquoise', text="O autorima",font=('Arial', 16, 'italic'))
     f4.pack(padx=5, pady=5)

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')
     
     global img
     img=PhotoImage(file="slike\\autori.png")
     im=Label(f4,image=img,bd=10,bg='mediumturquoise')
     im.grid(row=0, column=0,columnspan=2)

     global img2
     img2 = PhotoImage(file = "slike\\levo.png")
     img2 = img2.subsample(2, 2) #Velicina slike u dugmetu
     b1=DMMButton(f4,fg='white',activebackground='mediumaquamarine', image=img2,command=info,text='Nazad',compound=LEFT,bg='teal',font=('Calibri',12,'bold'))

     b1.grid(row=1, column=0)

     global img1
     img1 = PhotoImage(file = "slike\\desno.png")
     img1 = img1.subsample(2, 2) #Velicina slike u dugmetu
     b2=DMMButton(f4,fg='white',activebackground='mediumaquamarine',image = img1,command=pocetna,text = 'Početna', compound = RIGHT, bg='teal',font=('Calibri',12,'bold'))

     b2.grid(row=1, column=1)

     canvas.bind_all("<MouseWheel>",ignore)

#**********************************************************************************************
#***  POCETNA STRANA ***
#**********************************************************************************************
def pocetna():
     global main_frame
     main_frame.destroy() # Unistava prethodni frame

     main_frame = Frame(root,bg='mediumturquoise')
     main_frame.pack()

     global canvas
     canvas=Canvas(main_frame,bg = 'mediumturquoise')

     global img
     img=PhotoImage(file="slike\\pocetna.png")
     im=Label(main_frame,image=img,  bd=10, bg='mediumturquoise')
     im.grid(row=0, column=0,padx=5, pady=5)

     canvas.bind_all("<MouseWheel>",ignore)

def quit1():
     exit()

# === Korisnicke funkcije kraj

#**********************************************************************************************
#***  GLAVNI DEO PROGRAMA ***
#**********************************************************************************************

root = Tk()                             # Kreira glavni prozor sa nazivom root
root.title("Aplikacija Razvoj Karijere")# Naslov glavnog prozora
root.geometry('747x527+200+10')         # Dimenzija glavnog prozora
root.configure(background='mediumturquoise') # Boja pozadine

menubar = Menu(root)


filemenu0 = Menu(menubar, tearoff = 0, font=('Arial',11,'bold'), bg='mediumturquoise')
filemenu0.add_command(label = "Opšte o karijeri",command=korak0_1)
filemenu0.add_command(label = "Koraci u razvoju karijere",command=korak0_2)
filemenu0.add_separator()# Linija u meniju
filemenu0.add_command(label = "Izlaz", command = quit1) 
menubar.add_cascade(label = "Uvod", menu = filemenu0)



# === Korak 1
filemenu1 = Menu(menubar, tearoff = 0, font=('Arial',11,'bold'), bg='mediumturquoise')
filemenu1.add_command(label = "Pojam karijere",command = korak1_1)
filemenu1.add_command(label = "Karijera nekad i sad", command = korak1_2)
filemenu1.add_command(label = "Teorije razvoja karijere", command = korak1_3)
filemenu1.add_command(label = "Holland-ov heksagonalni model izbora karijere", command = korak1_4)
filemenu1.add_command(label = "Karakteristike etapa razvoja karijere", command = korak1_5)
filemenu1.add_separator()# Linija u meniju
filemenu1.add_command(label = "Izlaz", command = quit1) 
menubar.add_cascade(label = "Definisanje pojma karijere", menu = filemenu1)

# === Korak 2
filemenu2 = Menu(menubar, tearoff = 0,font=('Arial',11,'bold'), bg='mediumturquoise')
filemenu2.add_command(label="Planiranje karijere",command = korak2_1)
filemenu2.add_command(label = "SWOT analiza", command = korak2_2)
filemenu2.add_command(label = "Saznajte više o sebi",command = korak2_3 )
filemenu2.add_command(label = "Veštine,znanja,kompetencije",command = korak2_4)
filemenu2.add_command(label = "Poželjne veštine",command = korak2_5)
filemenu2.add_separator()# Linija u meniju
filemenu2.add_command(label = "Izlaz", command = quit1) 
menubar.add_cascade(label = "Planiranje karijere", menu = filemenu2)

# === Korak 3
filemenu3 = Menu(menubar, tearoff = 0, font=('Arial',11,'bold'), bg='mediumturquoise')
filemenu3.add_command(label="Zapošljivost",command = korak3_1)
filemenu3.add_command(label = "Osnovni pomovi",command = korak3_2)
filemenu3.add_command(label = "Ključna znanja,veštine,kompetencije",command = korak3_3)
filemenu3.add_command(label = "Ključna znanja,veštine,kompetencije",command = korak3_4)
filemenu3.add_command(label = "Prioritetne oblasti",command = korak3_5)
filemenu3.add_command(label = "Najtraženija zanimanja narednih decenija",command = korak3_6)
filemenu3.add_separator()# Linija u meniju
filemenu3.add_command(label = "Izlaz", command = quit1) 
menubar.add_cascade(label = "Koncept i teorija zapošljivosti", menu = filemenu3)

# === Korak 4
filemenu4 = Menu(menubar, tearoff = 0, font=('Arial',11,'bold'), bg='mediumturquoise')
filemenu4.add_command(label="Tržište rada",command = korak4_1)
filemenu4.add_command(label = "Karijerno vođenje", command = korak4_2)
filemenu4.add_command(label = "Tipovi ličnosti", command = korak4_3)
filemenu4.add_command(label = "Tehnički fakultet u Boru", command = korak4_4)
filemenu4.add_command(label = "Rudarsko inženjerstvo", command = korak4_5)
filemenu4.add_command(label = "Metaluršsko inženjerstvo", command = korak4_6)
filemenu4.add_command(label = "Tehnološko inženjerstvo", command = korak4_7)
filemenu4.add_command(label = "Inženjerski menadzment", command = korak4_8)
filemenu4.add_separator()# Linija u meniju
filemenu4.add_command(label = "Izlaz", command = quit1) 
menubar.add_cascade(label = "Istraživanje tržišta rada", menu = filemenu4)

# === Korak 5
filemenu5 = Menu(menubar, tearoff = 0, font=('Arial',11,'bold'), bg='mediumturquoise')
filemenu5.add_command(label="Važni koraci u nalaženju prvog posla", command = korak5_1)
filemenu5.add_command(label = "Istraživanje pre prijave", command = korak5_2)
filemenu5.add_command(label = "Mobilne aplikacije za pomoć", command = korak5_3)
filemenu5.add_separator()# Linija u meniju
filemenu5.add_command(label = "Izlaz", command = quit1) 
menubar.add_cascade(label = "Traženje posla", menu = filemenu5)

# === Korak 6
filemenu6 = Menu(menubar, tearoff = 0, font=('Arial',11,'bold'), bg='mediumturquoise')
filemenu6.add_command(label="CV", command = korak6_1)
filemenu6.add_command(label = "Lični podaci", command = korak6_2)
filemenu6.add_command(label = "Formalno obrazovanje", command = korak6_3)
filemenu6.add_command(label = "Radno iskustvo", command = korak6_4)
filemenu6.add_command(label = "Poznavanje stranih jezika", command = korak6_5)
filemenu6.add_command(label = "Lične osobine", command = korak6_6)
filemenu6.add_command(label = "Ostalo", command = korak6_7)
filemenu6.add_command(label = "Saveti", command = korak6_8)
filemenu6.add_separator()# Linija u meniju
filemenu6.add_command(label = "Izlaz", command = quit1) 
menubar.add_cascade(label = "Veštine pisanja CV", menu = filemenu6)

# === Korak 7
filemenu7 = Menu(menubar, tearoff = 0, font=('Arial',11,'bold'), bg='mediumturquoise')
filemenu7.add_command(label="Intervju", command = korak7_1)
filemenu7.add_command(label = "20 najčešće postavljanih pitanja", command = korak7_2)
filemenu7.add_command(label = "Šta potencijalni poslodavci očekuju da saznaju", command = korak7_3)
filemenu7.add_command(label = "Ponašanja kandidata", command = korak7_4)
filemenu7.add_command(label = "Savremene metode selekcije kandidata", command = korak7_5)
filemenu7.add_separator()# Linija u meniju
filemenu7.add_command(label = "Izlaz", command = quit1) 
menubar.add_cascade(label = "Priprema za intervju", menu = filemenu7)

# === Korak 8
filemenu8 = Menu(menubar, tearoff = 0, font=('Arial',11,'bold'), bg='mediumturquoise')
filemenu8.add_command(label="Postavljanje i dostizanje karijernog cilja", command = korak8_1)
filemenu8.add_command(label = "Uloga organizacije u razvoju karijere", command = korak8_2)
filemenu8.add_command(label = "Aktivnosti organizacije na podršci i razvoju karijera zaposlenih", command = korak8_3)
filemenu8.add_separator()# Linija u meniju
filemenu8.add_command(label = "Izlaz", command = quit1) 
menubar.add_cascade(label = "Podrška razvoju karijere", menu = filemenu8)

# === Help menu
helpmenu = Menu(menubar, tearoff=0, font=('Arial',11,'bold'), bg='mediumturquoise')
helpmenu.add_command(label = "Informacije", command = info)
helpmenu.add_command(label = "O Autorima...", command = autori)
menubar.add_cascade(label = "Pomoć", menu = helpmenu)

# Glavni prozor
root.config(menu = menubar)
root.resizable(0,0)

main_frame = Frame(root,bg='mediumturquoise')
main_frame.pack()

img=PhotoImage(file="slike\\pocetna.png")
im=Label(main_frame,image=img,  bd=10, bg='mediumturquoise')
im.grid(row=0, column=0,padx=5, pady=5)

# === Pokretanje GUI prozora
root.mainloop()
