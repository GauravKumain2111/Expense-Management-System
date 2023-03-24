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


Button(r, text="Filter by date", font="Algerian 13 bold", command=date1, bg="black", fg="white").place(x=75, y=437)
Button(r, text="Filter by transaction", font="Algerian 13 bold", command=payment, bg="black", fg="white").place(x=300,
                                                                                                                y=437)
Button(r, text="Filter by amount paid", font="Algerian 13 bold", command=amount, bg="black", fg="white").place(x=605,
                                                                                                               y=437)
Button(r, text="Filter by Paid to", font="Algerian 13 bold", command=id4, bg="black", fg="white").place(x=970, y=437)


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


Button(r, text="Delete the selected record ", font="Algerian 20 bold", fg="white", bg="darkblue", command=delete).place(
    x=400, y=720)
Button(r, text="Delete all ", font="Algerian 20 bold", fg="white", bg="darkblue", command=deleteall).place(x=520, y=800)

r.mainloop()