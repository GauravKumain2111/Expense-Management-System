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
    my_tree['columns'] = (
    'Date Of Payment', 'Method Of Payment', 'Paid To', 'Description', 'Amount Paid(In Rupees)', 'ID')
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

    a = StringVar()
    b = StringVar()
    c22 = StringVar()
    d = StringVar()
    e = StringVar()
    f = StringVar()

    DateEntry(r, font="Algerin 15 italic", textvariable=a).place(x=50, y=540)
    options = ["Cash", "UPI", "Cheque", "Credit Card", "Debit Card", "Net Banking", "GPay", "Paytm"]

    b.set(options[0])
    OptionMenu(r, b, *options).place(x=245, y=540)

    Entry(r, font="Algerin 12 italic", textvariable=c22).place(x=350, y=540)
    Entry(r, font="Algerin 12 italic", textvariable=d).place(x=580, y=540)
    Entry(r, font="Algerin 12 italic", textvariable=e).place(x=800, y=540)
    Entry(r, font="Algerin 12 italic", textvariable=f).place(x=1040, y=540)

    def sr():

        a1 = a.get()
        b1 = b.get()
        c1 = c22.get()
        d1 = d.get()
        e1 = e.get()
        f1 = f.get()

        selected = my_tree.focus()

        x = my_tree.selection()
        ids = []
        for record in x:
            ids.append(my_tree.item(record, 'values')[5])
        my_tree.item(selected, text="", values=(
            a1, b1, c1, d1, e1, f1,))

        conn = sqlite3.connect('hack1.db')

        c = conn.cursor()

        try:
            if c1 == "" or d1 == "" or e1 == "" or f1 == "":
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

    Button(r, text="UPDATE RECORD", bg="black", font=("BOLD", 16), command=sr, fg="white").place(x=550, y=605)
