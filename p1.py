from tkinter import *
from PIL import Image,ImageTk
import time
import variables as v 
from variables import *
root=Tk()
root.title("Cyber Genesis Crew")
root.state("zoomed")
root.configure(background='#4B6495')
bimg="E:/project_gui/background.png"
bimg2="D:\hackathon-batch-1\cut2.png"
bimg3="D:\hackathon-batch-1\pin.png"
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

WIN=Label(root,image=photo)
WIN.place(x=-10,y=-40)


def values(shell_1,shell_2,og_value):

    outputvol= int(volatage_input.get())
    if(outputvol>og_value):
        s1_val.configure(text=str(shell_1))
        s2_val.configure(text=str(shell_2-(og_value-outputvol)))
        shell_2=shell_2-outputvol
    else:
        s1_val.configure(text=str(shell_1-(og_value-outputvol)/2))
        s2_val.configure(text=str(shell_2+(og_value-outputvol)/2))
        shell_1=shell_1-(og_value-outputvol)/2
        shell_2=shell_2-(og_value-outputvol)/2

    og_value=outputvol    

def set():
    
    try:
        if(0<=int(volatage_input.get())<=500):
            POutput.configure(text="Power Output : "+str(int(volatage_input.get()))+" W")
            PD_val.configure(text=volatage_input.get())
            values(shell_1,shell_2,og_value)
        else:
            POutput.configure(text="Power Output : Out of range ")    
    except:
        POutput.configure(text="Power Output : Invalid Input !! ")
    # if(volatage_input.get()==int):
    #     POutput.configure(text="Power Output : "+volatage_input.get()+" W")
    # else:
    #     POutput.configure(text="Power Output : error ")
# img=PhotoImage(file=bimg2)

def cancel():   
    pass

s1=Label(root,text="Shell-1 :",font=(('helvetica',17)),bg='#4B6495')
s1.place(x=1040,y=20)

s2=Label(root,text="Shell-2 :",font=(('helvetica',17)),bg='#4B6495')
s2.place(x=1040,y=135)

PD=Label(root,text="Potential Difference :",font=(('helvetica',17)),bg='#4B6495')
PD.place(x=1040,y=250)

s1_val=Label(root,text="22000",font=(('helvetica',17)),fg="white",bg='#4472C4',width=17,height=2,borderwidth=1,relief="solid")
s1_val.place(x=1040,y=57)

s2_val=Label(root,text="21780",font=(('helvetica',17)),fg="white",bg='#4472C4',width=17,height=2,borderwidth=1,relief="solid")
s2_val.place(x=1040,y=172)

PD_val=Label(root,text=int(s1_val.cget("text"))-int(s2_val.cget("text")),font=(('helvetica',17)),fg="white",bg='#4472C4',width=17,height=2,borderwidth=1,relief="solid")
PD_val.place(x=1040,y=287)

Label(root,text="Set Output To :",font=(('helvetica',17)),bg='#4B6495').place(x=1040,y=380)

# Label(root,text="null",font=((50)),padx=80,pady=20).place(x=1040,y=417)
volatage_input=Entry(root,font=(('helvetica',17)),width=15,justify=CENTER)

volatage_input.place(x=1040,y=430)

Button(root,text="SET",font=(('helvetica',15)),fg="white",bg='#4472C4',padx=24,pady=1,command=set).place(x=1040,y=490)
Button(root,text="CANCEL",font=(('helvetica',15)),fg="white",bg='#4472C4',padx=0,pady=1,command=cancel).place(x=1145,y=490)

#bottom
Battery=Label(root,text="Battery Status : "+str(batper)+ "%",bg="#4B6495",font=(('helvetica',17)))
Battery.place(x=50,y=600)

Timer=Label(root,text="Run-Out Time : 3 hr 2 min",bg="#4B6495",font=(('helvetica',17)))
Timer.place(x=380,y=600)

POutput=Label(root,text="Power Output : 220 W",bg="#4B6495",font=(('helvetica',17)))
POutput.place(x=750,y=600)


root.mainloop()

