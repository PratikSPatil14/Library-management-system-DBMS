from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import cx_Oracle


con = cx_Oracle.connect('dbmslab/vitpune@localhost')
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" #Issue Table
bookTable = "books" #Book Table


#allBid = [] #List To store all Book IDs

def returnn():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status,check
    
    bid = bookInfo1.get()

    extractBid = "select book_id from "+issueTable
    cur.execute(extractBid)
    con.commit()
    check = ""
        # for i in cur:
        #     allBid.append(i[0])
        
        #if bid in allBid:
    checkAvail = "select status from "+bookTable+" where book_id = '"+bid+"'"
    cur.execute(checkAvail)
    con.commit()

    check = ""

    for i in cur:
        check = i[0]

    if check == 'issued':
        status = True
    elif check == 'avail':
        status = False
        print("Book Available")
        messagebox.showinfo("Error", "Book is not Issued")
    else:
        messagebox.showinfo("Error", "Book ID not present")

        # else:
        #     messagebox.showinfo("Error","Book ID not present")
    # except:
    #     messagebox.showinfo("Error","Can't fetch Book IDs")
    
    
    issueSql = "delete from "+issueTable+" where book_id = '"+bid+"'"
  
    #print(bid in allBid)
    #print(status)
    updateStatus = "update "+bookTable+" set status = 'avail' where book_id = "+bid
    try:
        if status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Returned Successfully")
        else:
            #allBid.clear()
            messagebox.showinfo('Message',"Please check the book ID")
            root.destroy()
            #return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    #allBid.clear()
    root.destroy()
    
def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()