from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import cx_Oracle

# Add your own database name and password here to reflect in the code


con = cx_Oracle.connect('dbmslab/vitpune@localhost')
cur = con.cursor()

# Enter Table Names here
bookTable = "books" 
    
def View(): 
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    Label(labelFrame, text=" Book ID ", bg='white', fg='black', font=('Arial', 10)).place(relx=0.03, rely=0.1,
                                                                                          relwidth=0.11)
    Label(labelFrame, text=" Title ", bg='white', fg='black', font=('Arial', 10)).place(relx=0.15, rely=0.1,
                                                                                        relwidth=0.3)
    Label(labelFrame, text=" Author ", bg='white', fg='black', font=('Arial', 10)).place(relx=0.46, rely=0.1,
                                                                                         relwidth=0.3)
    Label(labelFrame, text=" Status ", bg='white', fg='black', font=('Arial', 10)).place(relx=0.77, rely=0.1,
                                                                                         relwidth=0.2)

    getBooks = "select * from " + bookTable
    y = 0.2
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%s" % i[0], bg='white', fg='black', font=('Arial', 10)).place(relx=0.03, rely=y,
                                                                                                  relwidth=0.11)
            Label(labelFrame, text="%s" % i[1], bg='white', fg='black', font=('Arial', 10)).place(relx=0.15, rely=y,
                                                                                                  relwidth=0.3)
            Label(labelFrame, text="%s" % i[2], bg='white', fg='black', font=('Arial', 10)).place(relx=0.46, rely=y,
                                                                                                  relwidth=0.3)
            Label(labelFrame, text="%s" % i[3], bg='white', fg='black', font=('Arial', 10)).place(relx=0.77, rely=y,
                                                                                                  relwidth=0.2)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()