from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk
root=Tk()

root.minsize(1600,850)
root.maxsize(1600,850)


def ns():
 root1 = Toplevel(root)
 root1.minsize(500, 500)
 root1.maxsize(500, 500)
 l = Label(root1, text="Date Of Payment\n  (MM\DD\YY)", font="Algerin 15 italic").place(x=10, y=10)
 l = Label(root1, text="Method of Payment", font="Algerin 15 italic").place(x=10, y=80)
 l = Label(root1, text="Paid For", font="Algerin 15 italic").place(x=10, y=150)
 l = Label(root1, text="Description", font="Algerin 15 italic").place(x=10, y=220)
 l = Label(root1, text="Amount Paid", font="Algerin 15 italic").place(x=10, y=290)
 l = Label(root1, text="ID", font="Algerin 15 italic").place(x=10, y=360)
 global date

 date = StringVar()
 mp = StringVar()
 pf = StringVar()
 des1 = StringVar()
 ap1 = StringVar()
 id = StringVar()

 def c_c():
  global dop
  global mop
  global pt
  global des
  global ap
  global id1

  dop = date.get()
  mop = mp.get()
  pt = pf.get()
  des = des1.get()
  ap = ap1.get()

  ID = id.get()

  con = sqlite3.connect("hack1.db")

  c = con.cursor()

  try:
   if pt == "" or des == "" or ap == "":
    messagebox.showinfo("Alert", "One or more entry fields cannot be empty")




   else:
    c.execute("INSERT INTO expense VALUES(:dop,:mop,:pt,:des,:ap,:ID)",
              {'dop': dop, 'mop': mop,
               'pt': pt, 'des': des,
               'ap': int(ap), 'ID': (ID)})
    con.commit()
    messagebox.showinfo("Great!", "Record added to database")
    root1.destroy()
  except(ValueError):
   messagebox.showwarning("WARNING!", "Amount Paid must be integer number\nPlease Check Again")

 DateEntry(root1, textvariable=date, font="Algerin 15 italic").place(x=230, y=25)
 options = ["Cash", "UPI", "Cheque", "Credit Card", "Debit Card", "Net Banking", "GPay", "Paytm"]

 mp.set(options[0])
 OptionMenu(root1, mp, *options).place(x=240, y=80)
 Entry(root1, textvariable=pf, font="Algerin 15 italic").place(x=200, y=150)
 Entry(root1, textvariable=des1, font="Algerin 15 italic").place(x=200, y=220)
 Entry(root1, textvariable=ap1, font="Algerin 15 italic").place(x=200, y=293)
 Entry(root1, textvariable=id, font="Algerin 15 italic").place(x=200, y=360)

 Button(root1, text="ADD RECORD → ", font="Algerin 15 italic", command=c_c, bg="green", fg="white", relief=RIDGE).place(
  x=130, y=430)
 f2 = Frame(root1, width=5, height=555, bg="darkblue")
 f2.place(x=0, y=0)

 f3 = Frame(root1, width=5, height=505, bg="darkblue")
 f3.place(x=495, y=0)

 f4 = Frame(root1, width=500, height=5, bg="darkblue")
 f4.place(x=0, y=0)

 f5 = Frame(root1, width=500, height=5, bg="darkblue")
 f5.place(x=0, y=495)

 root1.mainloop()


def vp():
 global r
 r = Toplevel(root)
 r.minsize(1300, 870)
 r.maxsize(1300, 870)

 conn = sqlite3.connect("hack1.db")
 c = conn.cursor()
 c.execute("""Create Table if not exists expense(
                    dop text,
                    mop text,
                    pt text,
                    des text,
                    ap real,
                    ID text)""")
 conn.commit()
 conn.close()

 style = ttk.Style()
 style.theme_use("clam")
 style.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")
 style.map('Treeview', background=[('selected', 'green')])

 tree_scroll = Scrollbar(r)
 tree_scroll.pack(side=RIGHT, fill=Y)

 global my_tree
 my_tree = ttk.Treeview(r, yscrollcommand=tree_scroll.set)

 tree_scroll.config(command=my_tree.yview)

 my_tree.tag_configure("oddrow", background="white")
 my_tree.tag_configure("evenrow", background="skyblue")
 my_tree['columns'] = ('Date Of Payment', 'Method Of Payment', 'Paid To', 'Description', 'Amount Paid(In Rupees)', 'ID')
 my_tree.column("#0", width=0, minwidth=0, stretch=NO)
 my_tree.column("Date Of Payment", width=150, minwidth=25)
 my_tree.column("Method Of Payment", width=150, minwidth=25)
 my_tree.column("Paid To", width=150, minwidth=25)
 my_tree.column("Description", width=150, minwidth=50)
 my_tree.column("Amount Paid(In Rupees)", width=150, minwidth=25)
 my_tree.column("ID", width=150, minwidth=25)

 my_tree.heading("#0", text="Label", anchor=W)
 my_tree.heading("Date Of Payment", text="Date Of Payment (MM/DD/YY)", anchor=W)
 my_tree.heading("Method Of Payment", text="Method Of Payment", anchor=W)
 my_tree.heading("Paid To", text="Paid To", anchor=W)
 my_tree.heading("Description", text="Description", anchor=W)
 my_tree.heading("Amount Paid(In Rupees)", text="Amount Paid(In Rupees)", anchor=W)
 my_tree.heading("ID", text="ID", anchor=W)

 con = sqlite3.connect("hack1.db")

 c = con.cursor()

 c.execute("SELECT * FROM expense ")

 records = c.fetchall()

 global count
 count = 0

 for record in records:
  if count % 2 == 0:
   my_tree.insert(parent='', index='end', iid=count, text='',
                  values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('evenrow',))
  else:
   my_tree.insert(parent='', index='end', iid=count, text='',
                  values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('oddrow',))

  count += 1

 my_tree.pack(side=TOP)


 date = StringVar()
 mp = StringVar()

 ap1 = StringVar()
 id = StringVar()
 pf = StringVar()
 des1 = StringVar()


 DateEntry(r, textvariable=date, font="Algerin 15 italic").place(x=80, y=390)
 options = ["Cash", "UPI", "Cheque", "Credit Card", "Debit Card", "Net Banking", "GPay", "Paytm"]

 mp.set(options[0])
 OptionMenu(r, mp, *options).place(x=390, y=390)
 Entry(r, textvariable=ap1, font="Algerin 15 italic").place(x=610, y=390)
 Entry(r, textvariable=pf, font="Algerin 15 italic").place(x=930, y=390)

 a=StringVar()
 b=StringVar()
 c22=StringVar()
 d=StringVar()
 e=StringVar()
 f=StringVar()




 DateEntry(r,  font="Algerin 15 italic",textvariable=a).place(x=50, y=540)
 options = ["Cash", "UPI", "Cheque", "Credit Card", "Debit Card", "Net Banking", "GPay", "Paytm"]

 b.set(options[0])
 OptionMenu(r, b, *options).place(x=245, y=540)







 Entry(r,  font="Algerin 12 italic",textvariable=c22).place(x=350, y=540)
 Entry(r, font="Algerin 12 italic",textvariable=d).place(x=580, y=540)
 Entry(r, font="Algerin 12 italic",textvariable=e).place(x=800, y=540)
 Entry(r, font="Algerin 12 italic", textvariable=f).place(x=1040, y=540)

 def sr():

  a1=a.get()
  b1=b.get()
  c1=c22.get()
  d1=d.get()
  e1=e.get()
  f1=f.get()
  # Grab the record number
  selected = my_tree.focus()
  # Update record
  x = my_tree.selection()
  ids = []
  for record in x:
   ids.append(my_tree.item(record, 'values')[5])
  my_tree.item(selected, text="", values=(
  a1, b1, c1, d1, e1,f1,))


  # Update the database
  # Create a database or connect to one that exists





  conn = sqlite3.connect('hack1.db')

  # Create a cursor instance
  c = conn.cursor()

  try:
   if c1 == "" or d1 == "" or e1 == ""or f1=="":
    messagebox.showinfo("Alert", "One or more entry fields cannot be empty")




   else:
    c.executemany("DELETE FROM expense WHERE ID=?", [(a,) for a in ids])

    c.execute("INSERT INTO expense VALUES(:dop,:mop,:pt,:des,:ap,:ID)",
              {'dop': a1, 'mop': b1,
               'pt': c1, 'des': d1,
               'ap': int(e1), 'ID': (f1)})
    conn.commit()

    messagebox.showinfo("Great!", "Record Updated")

  except(ValueError):
   messagebox.showwarning("WARNING!", "Amount Paid must be integer number\nPlease Check Again")

  conn.commit()



 Button(r, text="UPDATE RECORD", bg="black", font=("BOLD", 16),command=sr,fg="white").place(x=550,y=605)

 def tvdel():

  for record1 in my_tree.get_children():
   my_tree.delete(record1)

 def date1():
  dop = date.get()
  tvdel()

  con = sqlite3.connect("hack1.db")

  c = con.cursor()

  c.execute("SELECT * FROM expense WHERE dop=?", (dop,))
  records = c.fetchall()

  global count
  count = 0

  for record in records:
   if count % 2 == 0:
    my_tree.insert(parent='', index='end', iid=count, text='',
                   values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                   tags=('evenrow',))
   else:
    my_tree.insert(parent='', index='end', iid=count, text='',
                   values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                   tags=('oddrow',))

   count += 1

 def payment():
  mop = mp.get()
  tvdel()

  con = sqlite3.connect("hack1.db")

  c = con.cursor()

  c.execute("SELECT * FROM expense WHERE mop=?", (mop,))
  records = c.fetchall()

  global count
  count = 0

  for record in records:
   if count % 2 == 0:
    my_tree.insert(parent='', index='end', iid=count, text='',
                   values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                   tags=('evenrow',))
   else:
    my_tree.insert(parent='', index='end', iid=count, text='',
                   values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                   tags=('oddrow',))

   count += 1

 def amount():
  ap = ap1.get()
  tvdel()

  con = sqlite3.connect("hack1.db")

  c = con.cursor()

  c.execute("SELECT * FROM expense WHERE ap=?", (ap,))
  records = c.fetchall()

  global count
  count = 0

  for record in records:
   if count % 2 == 0:
    my_tree.insert(parent='', index='end', iid=count, text='',
                   values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                   tags=('evenrow',))
   else:
    my_tree.insert(parent='', index='end', iid=count, text='',
                   values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                   tags=('oddrow',))

   count += 1

 def id4():
  pt = pf.get()
  tvdel()

  con = sqlite3.connect("hack1.db")

  c = con.cursor()

  c.execute("SELECT * FROM expense WHERE pt=?", (pt,))
  records = c.fetchall()

  global count
  count = 0

  for record in records:
   if count % 2 == 0:
    my_tree.insert(parent='', index='end', iid=count, text='',
                   values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                   tags=('evenrow',))
   else:
    my_tree.insert(parent='', index='end', iid=count, text='',
                   values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                   tags=('oddrow',))

   count += 1

 Button(r, text="Filter by date", font="Algerian 13 bold", command=date1,bg="black",fg="white").place(x=75, y=437)
 Button(r, text="Filter by transaction", font="Algerian 13 bold", command=payment,bg="black",fg="white").place(x=300, y=437)
 Button(r, text="Filter by amount paid", font="Algerian 13 bold", command=amount,bg="black",fg="white").place(x=605, y=437)
 Button(r, text="Filter by Paid to", font="Algerian 13 bold", command=id4,bg="black",fg="white").place(x=970, y=437)

 def delete():

  x = my_tree.selection()
  ids = []
  for record in x:
   ids.append(my_tree.item(record, 'values')[5])
  print(ids)
  for record in x:
   my_tree.delete(record)

  con = sqlite3.connect("hack1.db")

  c = con.cursor()

  c.executemany("DELETE FROM expense WHERE ID=?", [(a,) for a in ids])
  con.commit()
  con.close()

 def deleteall():
  x1 = my_tree.selection()
  ids1 = []
  for record in x1:
   ids1.append(my_tree.item(record))
  print(ids1)

  for record in my_tree.get_children():
   my_tree.delete(record)

  con = sqlite3.connect("hack1.db")

  c = con.cursor()

  c.execute("DELETE FROM expense")
  con.commit()
  con.close()

 Button(r, text="Delete the selected record ", font="Algerian 20 bold", fg="white",bg="darkblue", command=delete).place(x=400, y=720)
 Button(r, text="Delete all ", font="Algerian 20 bold", fg="white",bg="darkblue", command=deleteall).place(x=520, y=800)

 r.mainloop()




def analysis():
 t=Toplevel(root)
 t.minsize(1300,700)
 t.maxsize(1300,700)
 f1=Frame(t,bg="blue",width=350,height=450).place(x=10,y=120)
 f2=Frame(t,bg="grey",width=350,height=450).place(x=440,y=120)
 l=Label(t,text="Total Spent ",font="algerian 30 bold",fg="black",bg="grey").place(x=480,y=180)
 f3=Frame(t,bg="blue",width=350,height=450).place(x=880,y=120)
 t.mainloop()

def feedback():
 v = Toplevel(root)

 v.minsize(850, 400)
 v.maxsize(850, 400)

 f1 = Frame(v, bg="lightgrey", borderwidth=5, relief=RIDGE, height=70)
 f1.pack(side=TOP, fill="x")
 l = Label(f1, text="Feedback", fg="black", borderwidth=7, bg="lightgrey", font="Algerian 30 bold")
 l.place(x=310, y=0)
 f2 = Frame(v, bg="white", borderwidth=5, relief=RIDGE, height=300)
 f2.pack(fill="x")
 l = Label(f2, text="How would you rate us ?", fg="black", bg="white", font="Algerian 20 bold")
 l.place(x=4, y=2)
 radio = Radiobutton(f2, bg="white", font="Algerian 18 italic", text="Excellent", value=1).place(x=0, y=50)
 radio = Radiobutton(f2, bg="white", font="Algerian 18 italic", text="Good", value=2).place(x=180, y=50)
 radio = Radiobutton(f2, bg="white", font="Algerian 18 italic", text="Medium", value=3).place(x=290, y=50)
 radio = Radiobutton(f2, bg="white", font="Algerian 18 italic", text="Bad", value=4).place(x=430, y=50)
 radio = Radiobutton(f2, bg="white", font="Algerian 18 italic", text="Worse", value=5).place(x=530, y=50)

 entry = Entry(v, borderwidth=2, width=25, font="comicsansms 35 italic")
 entry.place(x=30, y=200)

 button = Button(v, width=20, height=0, text="Submit", bg="darkblue", border=5, font=("Impact", 18), fg="black")
 button.place(x=280, y=300)

 v.mainloop()


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