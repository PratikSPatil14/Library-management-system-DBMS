from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import cx_Oracle


con = cx_Oracle.connect('dbmslab/vitpune@localhost')
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" 
bookTable = "books"
    


def issue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    bid = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    
    extractBid = "select book_id from "+bookTable
    cur.execute(extractBid)
    con.commit()
#    print(allBid)
    # for i in cur:
    #     allBid.append(i[0])
        
#    if bid in allBid:
    checkAvail = "select status from "+bookTable+" where book_id = '"+bid+"'"
    cur.execute(checkAvail)
    con.commit()
    check=''
#        print(allBid)
    for i in cur:
        check = i[0]
            
    if check == 'avail':
        status = True
        print("Book Available")
        print(type(check))
    elif check == 'issued':
        status = False
        print("Book not Available")
        messagebox.showinfo("Error", "Book alredy issued")
        print(type(check))
    else:
        print("Book not Available")
        print(type(check))
        messagebox.showinfo("Error", "Book ID not present")
    # else:
    #     messagebox.showinfo("Error","Book ID not present")
    
    
    issueSql = "insert into "+issueTable+"(BOOK_ID, ISSUETO) values ('"+bid+"','"+issueto+"')"
    show = "select * from "+issueTable
    
    updateStatus = "update "+bookTable+" set status = 'issued' where book_id = '"+bid+"'"
    try:
        if status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            root.destroy()
        else:
            #allBid.clear()
            # messagebox.showinfo('Message',"Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(bid)
    print(issueto)
    
    #allBid.clear()
    
    
    
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()



