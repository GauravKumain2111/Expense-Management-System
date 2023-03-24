from tkinter import *
from PIL import Image, ImageTk

root=Tk()

root.minsize(1600,850)
root.maxsize(1600,850)


f1=Frame(root, height=250, width=1600, bg="#F0FFFF")
f1.place(x=0, y=650)

img=Image.open("addreal.png")
resized=img.resize((100,100))
ph=ImageTk.PhotoImage(resized)

b1=Button(f1, bg="#F0FFFF", image=ph, borderwidth=0,command=ns)
b1.place(x=110, y=30)

l1=Label(f1, text="ADD RECORD", font=("Microsoft JhengHei UI", 12, "bold"), bg="#F0FFFF")
l1.place(x=105, y=130)

img2=Image.open("view.png")
resized2=img2.resize((100,100))
ph2=ImageTk.PhotoImage(resized2)
b2=Button(f1, bg="#F0FFFF", image=ph2, borderwidth=0 ,command=vp)
b2.place(x=430, y=30)
l2=Label(f1, text="VIEW RECORD", font=("Microsoft JhengHei UI", 12, "bold"), bg="#F0FFFF")
l2.place(x=425, y=130)

img3=Image.open("exit (2).png")
resized3=img3.resize((130,140))
ph3=ImageTk.PhotoImage(resized3)
b3=Button(f1, bg="#F0FFFF", image=ph3, borderwidth=0, command=quit )
b3.place(x=1340, y=10)
l3=Label(f1, text="EXIT", font=("Microsoft JhengHei UI", 14, "bold"), bg="#F0FFFF")
l3.place(x=1380, y=135)

img4=Image.open("feedback.png")
resized4=img4.resize((100,100))
ph4=ImageTk.PhotoImage(resized4)
b4=Button(f1, bg="#F0FFFF", image=ph4, borderwidth=0,command=feedback )
b4.place(x=1080, y=25)
l4=Label(f1, text="FEEDBACK", font=("Microsoft JhengHei UI", 14, "bold"), bg="#F0FFFF")
l4.place(x=1085, y=135)



img11=Image.open("analysis.png")
resized11=img11.resize((100,100))
ph11=ImageTk.PhotoImage(resized11)
b4=Button(f1, bg="#F0FFFF", image=ph11, borderwidth=0,command=analysis )
b4.place(x=750, y=25)
l11=Label(f1, text="ANANLYSIS", font=("Microsoft JhengHei UI", 14, "bold"), bg="#F0FFFF")
l11.place(x=745, y=135)

f2=Frame(root, height=5, width=1600, bg="darkblue" )
f2.place(x=0, y=650)

f3=Frame(root, width=1600, height=650, bg="pink")
f3.place(x=0, y=0)



img5=Image.open("bg11.jpg")
resized5=img5.resize((1600,650))
ph5=ImageTk.PhotoImage(resized5)
l5=Label(f3, image=ph5)
l5.place(x=0, y=0)

img6=Image.open("welcome10.jpg")
resized6=img6.resize((350,300))
ph6=ImageTk.PhotoImage(resized6)
l6=Label(f3, image=ph6, borderwidth=0,bg="#e4e9ef")
l6.place(x=620,y=0)

l7=Label(f3, text="TO \n\n Expense tracker", borderwidth=0,bg="#e4e9ef",font="Algerian 60 bold").place(x=400,y=300)

f4=Frame(f3, width=8, height=650, bg="darkblue")
f4.place(x=352, y=0)

f5=Frame(root, height=5, width=1600, bg="darkblue" )
f5.place(x=0, y=0)

f6=Frame(f3, width=8, height=650, bg="darkblue")
f6.place(x=1200, y=0)

img8=Image.open("namaste-removebg-preview.png")
resized8=img8.resize((350,500))
ph8=ImageTk.PhotoImage(resized8)
l10=Label(f3, image=ph8, borderwidth=0,bg="#e4e9ef")
l10.place(x=1215,y=10)

img9=Image.open("namaste-removebg-preview.png")
resized9=img9.resize((350,650))
ph9=ImageTk.PhotoImage(resized9)
l11=Label(f3, image=ph8, borderwidth=0,bg="#e4e9ef")
l11.place(x=0,y=10)

root.mainloop()