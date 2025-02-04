from tkinter import *
import tkinter.messagebox as tmsg


def data():
    print("Submitting Form")
    print(f"Name :{namevalue.get()}")
    print(f"Email id :{emailvalue.get()}")
    print(f"Phone no. :{phonevalue.get()}")
    print(f"Date : {datevalue.get()}")
    print(f"Time : {timevalue.get()}")
    print(f"Suggestion :{suggestvalue.get()}")
    print(f"Rating :{reviewentry.get()}%")
    rating = reviewentry.get()
    if 0 < rating < 20:
        customer_review = "Bad"
    elif 20 < rating < 40 :
        customer_review = "Okay"
    elif 40 < rating < 60 :
        customer_review = "Neutral"
    elif 60 < rating < 80 :
        customer_review = "Good"
    elif 80 < rating < 100 :
        customer_review = "Best"
    else :
        customer_review = "Invalid"
        
    tmsg.showinfo("Success", "Form submitted successfully")
    
    with open("details.txt" , "a") as f:
        f.write(f"\nName :{namevalue.get()}\nEmail id :{emailvalue.get()}\nPhone no. :{phonevalue.get()}\nDate : {datevalue.get()}\nTime : {timevalue.get()}\nSuggestion :{suggestvalue.get()}\nReview :{customer_review}\n-----------------------------------------------")
    

root = Tk()
root.title("MyGUI")
root.geometry("800x600")

f1 = Frame(root, bg = "yellow" , borderwidth = 2 , )
f1.pack(side = TOP , fill = X )

f2 = Frame(root , borderwidth = 2 ,)
f2.pack(side = TOP , fill = X )

f3 = Frame(root)
f3.pack(fill = X)

f4 = Frame(root , borderwidth = 2 ,bg = "Black")
f4.pack(side = BOTTOM , fill = X )

Label(f1,text="Welcome to Our Restaurant",font=('Helvetica', 20 , "bold" ,"underline"),bg="yellow",).pack()
Label(f2,text="Feedback Form",font=('Times New Roman', 15 , "bold" ,"underline"),).pack()
Label(f4,text="Thank You for giving us your valuable Feedback. Please visit again",font=('Times New Roman', 15   ,), fg = "white" , bg = "black").pack()

name = Label(f3,text="Full Name :").grid(row=0,column=0)
email = Label(f3,text="Email id :").grid(row=1,column=0)
phone = Label(f3,text="Phone No. :").grid(row=2,column=0)
date = Label(f3,text="Date :").grid(row=3,column=0)
time = Label(f3,text="Time :").grid(row=4,column=0)
suggest = Label(f3,text="Any Suggestion :").grid(row=5,column=0)
review = Label(f3,text="Rate us :").grid(row=6,column=0)

namevalue = StringVar()
emailvalue = StringVar()
phonevalue = StringVar()
datevalue = StringVar()
timevalue = StringVar()
suggestvalue = StringVar()
# reviewvalue = IntVar()

nameentry = Entry(f3 , textvariable = namevalue).grid(row = 0 , column = 3)
emailentry = Entry(f3 , textvariable = emailvalue).grid(row = 1 , column = 3)
phoneentry = Entry(f3 , textvariable = phonevalue).grid(row = 2 , column = 3)
dateentry = Entry(f3 , textvariable = datevalue).grid(row = 3, column = 3)
timeentry = Entry(f3 , textvariable = timevalue).grid(row = 4 , column = 3)
suggestentry = Entry(f3 , textvariable = suggestvalue).grid(row = 5 , column = 3)
reviewentry = Scale(f3 , from_=0,to_=100,orient=HORIZONTAL)
reviewentry.grid(row = 6, column = 3)
btn = Button(root, text = "Submitt", command = data).pack()



root.mainloop()