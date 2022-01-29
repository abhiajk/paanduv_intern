from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk #to work with images
import tkinter.font as font #font module to change font size in widgets
from tkinter import messagebox
import solver as slv #backend code to solve equation with inputs received from user
root = Tk()
#root.geometry("950x1200")

#Tabs
mytab = ttk.Notebook(root)
mytab.grid()
tab1 = ttk.Frame(mytab)
tab2 = ttk.Frame(mytab)

mytab.add(tab1, text ='Home')
mytab.add(tab2, text ='Mach Calculator')

mytab.hide(1) #hide tab with index 1 i.e tab2

#tab1
####################################
####################################
#Tab1 - Home Tab
canvas = Canvas(tab2,width=600,height=300)
canvas.grid(columnspan=3, rowspan =3)
######
#Defining a common text font throughout the Home Tab with variable font size
sizeVar1=0
t1_font_bold = font.Font(family='Arial', size=sizeVar1,weight='bold')
t1_font_bolditalic = font.Font(family='Arial', size=sizeVar1,weight='bold',slant='italic')
######

#Description of App & Logo
#text
sizeVar=5
text1="This App is used to calculate the max inlet Mach corresponding to choked condition at throat for a Hyperloop pod in tube"
desc1 = Label(tab1, text=text1, font=t1_font_bolditalic, height=5)
desc1.grid(columnspan=3,column=0,row=1)
#text2 = ""
#desc2 = Label(tab1, text=text2, font=t1_font_bolditalic, height=5)
#desc2.grid(columnspan=3,column=0,row=1)
#logo using pillow module
logo=Image.open('hyperloop.jpg') #Image method opens the image as a pillow image;this needs to be converted to tkinter format
#logo=logo.resize((200,200))
logo = ImageTk.PhotoImage(logo) #converting pillow image into tkinter image
logo_label = Label(tab1,image=logo) #defining label as a container for image
#logo_label.image = logo_label
logo_label.grid(column=1,row=0)

#New Tab
def newTab():
    mytab.select(1)
    mytab.hide(0)

#button
sizeVar1=5
b = Button(tab1,text='Mach Calculator',command=lambda:newTab(),font=t1_font_bold,height=5, padx=20,bg = '#20bebe', fg='black', activebackground='green')
b.grid(column=1,row=2)
#rearranging canvas below Button
canvas = Canvas(tab1,width=600,height=100)
canvas.grid(columnspan=3)

#tab2
###############################
###############################
#tab2

canvas = Canvas(tab2,width=600,height=300)
canvas.grid(columnspan=3, rowspan =3)
######
#Defining a common text font throughout the Home Tab with variable font size
sizeVar2=0
t2_font_bold = font.Font(family='TimesNewRoman', size=sizeVar2,weight='bold')
t2_font_bolditalic = font.Font(family='Helvetica', size=sizeVar2,weight='bold',slant='italic')
######

def home():
    mytab.select(0)
    mytab.hide(1)

def maxmach():
    try:
        d1=float(e1.get())
        d2=float(e2.get())
        s = slv.solve(d1,d2)
        x = s.eqn_solver()
        #populate list and turn on listbox and scrollbar
        mylist.delete(0,5)
        for i in range(6):
            mylist.insert(END, x[i])
        mylist.grid(column=1,row=4,pady=10)
        scrollbar.grid(column=2,row=4)
    except:
        print('Invalid Input &/ Enter Numerical Values')
        messagebox.showwarning("Alert", "Invalid Input &/ Enter Numerical Values")

sizeVar2=2

#back_button
bck_button = Button(tab2,text='Go Back',font=t2_font_bold,padx=20,bg = 'green',fg='white',command=lambda:home())
bck_button.place(anchor=NW,height=20, width=80, y=10)

#entry
obj_dia = StringVar()
t_dia = StringVar()
l1 = Label(tab2, text="Enter Pod diameter (in metres)",font=t2_font_bold)
l1.grid(column=0,row=1)
e1 = Entry(tab2,bd=5,textvariable=obj_dia)
e1.grid(column=1,row=1)
l2 = Label(tab2, text="Enter tube diameter (in metres)",font=t2_font_bold)
l2.grid(column=0,row=2)
e2 = Entry(tab2,bd=5,textvariable=t_dia)
e2.grid(column=1,row=2)

calc_button = Button(tab2,text='CALCULATE',font=t2_font_bolditalic,padx=20,bg='red',fg='white',command=lambda:maxmach())
calc_button.grid(column=1,row=3)

#view results
scrollbar = Scrollbar(tab2)
mylist = Listbox(tab2, bd=5,height=3,yscrollcommand = scrollbar.set, font=t2_font_bolditalic)
scrollbar.config( command = mylist.yview )

#############################################
#############################################

root.mainloop()
