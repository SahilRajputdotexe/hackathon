from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("Cyber Genesis Crew")
root.state("zoomed")
root.configure(background='#4B6495')
bimg="E:/project_gui/background.png"
bimg2="C:/Users/HIMANSHU SINGH/Pictures/Screenshots/cut2.png"
bimg3="C:/Users/HIMANSHU SINGH/Pictures/project/pin.png"
# bimg3="C:/Users/HIMANSHU SINGH/Pictures/project/.png"

img=Image.open(bimg2)
resize_img=img.resize((1020,600))

img2=Image.open(bimg3)
resize_img2=img2.resize((200,200))

# img3=Image.open(bimg4)
# resize_img3=img3.resize((200,200))


resize_img.paste(resize_img2, (305, 213), resize_img2)
# Convert the Image object into a TkPhoto object


tkimage = ImageTk.PhotoImage(resize_img)

photo=ImageTk.PhotoImage(resize_img)

l1=Label(root,image=photo)
l1.place(x=-10,y=-40)
def set():
    try:
        l7.configure(text="Power Output : "+str(int(e1.get()))+" W")
    except:
        l7.configure(text="Power Output : Invalid Input !! ")
    # if(e1.get()==int):
    #     l7.configure(text="Power Output : "+e1.get()+" W")
    # else:
    #     l7.configure(text="Power Output : error ")
# img=PhotoImage(file=bimg2)

l2=Label(root,text="Shell-1 :",font=(('helvetica',17)),bg='#4B6495')
l2.place(x=1040,y=20)

l3=Label(root,text="Shell-2 :",font=(('helvetica',17)),bg='#4B6495')
l3.place(x=1040,y=135)

l4=Label(root,text="Potential Difference :",font=(('helvetica',17)),bg='#4B6495')
l4.place(x=1040,y=250)

l21=Label(root,text="20220",font=(('helvetica',17)),fg="white",bg='#4472C4',width=17,height=2,borderwidth=1,relief="solid")
l21.place(x=1040,y=57)

l31=Label(root,text="20000",font=(('helvetica',17)),fg="white",bg='#4472C4',width=17,height=2,borderwidth=1,relief="solid")
l31.place(x=1040,y=172)

l41=Label(root,text=int(l21.cget("text"))-int(l31.cget("text")),font=(('helvetica',17)),fg="white",bg='#4472C4',width=17,height=2,borderwidth=1,relief="solid")
l41.place(x=1040,y=287)

Label(root,text="Set Output To :",font=(('helvetica',17)),bg='#4B6495').place(x=1040,y=380)

# Label(root,text="null",font=((50)),padx=80,pady=20).place(x=1040,y=417)
e1=Entry(root,font=(('helvetica',17)),width=15,justify=CENTER)

e1.place(x=1040,y=430)

Button(root,text="SET",font=(('helvetica',15)),fg="white",bg='#4472C4',padx=24,pady=1,command=set).place(x=1040,y=490)
Button(root,text="CANCEL",font=(('helvetica',15)),fg="white",bg='#4472C4',padx=0,pady=1).place(x=1145,y=490)

#bottom
l5=Label(root,text="Battery Status : 95%",bg="#4B6495",font=(('helvetica',17)))
l5.place(x=50,y=600)

l6=Label(root,text="Run-Out Time : 3 hr 2 min",bg="#4B6495",font=(('helvetica',17)))
l6.place(x=380,y=600)

l7=Label(root,text="Power Output : 220 W",bg="#4B6495",font=(('helvetica',17)))
l7.place(x=750,y=600)


root.mainloop()