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
