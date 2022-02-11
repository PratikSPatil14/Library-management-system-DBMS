from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import cx_Oracle


con = cx_Oracle.connect('dbmslab/vitpune@localhost')
cur = con.cursor()
 
bookTable = "books" #Book Table


def deleteBook():

    global status,bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root,check 
    
    bid = bookInfo1.get()

    checkAvail = "select status from "+bookTable+" where book_id = '"+bid+"'"
    cur.execute(checkAvail)
    con.commit()
#        print(allBid)
    check = ""
    for i in cur:
        check = i[0]
       
    if check == 'avail':
        status = True
        print("Book Available")
    elif check == 'issued':
        status = False
        print("Book not Available")
        messagebox.showinfo("Error","Book is Issued, Can't Delete")
    else:
        messagebox.showinfo("Error","Book ID not present")
    
    
    deleteSql = "delete from "+bookTable+" where book_id = '"+bid+"'"
    
    try:
        if status == True:
            cur.execute(deleteSql)
            con.commit()
            messagebox.showinfo('Success',"Book Deleted Successfully")
            root.destroy()
        elif status == False:
            messagebox.showinfo("Error","Can not Delete Issued Book")
        else:
            messagebox.showinfo("Error","Check the book id")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    root.destroy()
    
def delete(): 
    
    global status,bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root,check
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()