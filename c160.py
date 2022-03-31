from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import os
import tkinter.messagebox as tkmb

root=Tk()
root.title("notepad")
root.minsize(650,650)
root.maxsize(650,650)


open_image=ImageTk.PhotoImage(Image.open("open.png"))
save_image=ImageTk.PhotoImage(Image.open("save.png"))
exit_image=ImageTk.PhotoImage(Image.open("exit.jpg"))

label1=Label(root,text="File name")
label1.place(relx=0.28,rely=0.03,anchor=CENTER)

input_name=Entry(root)
input_name.place(relx=0.46,rely=0.03,anchor=CENTER)

text_1=Text(root,height=35,width=80)
text_1.place(relx=0.5,rely=0.55,anchor=CENTER)

name=""

def openimage():
    global name
    text_1.delete(1.0,END)
    input_name.delete(0,END)
    text_file=filedialog.askopenfilename(title=" Open Text File", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    name=os.path.basename(text_file)
    formatedname=name.split('.')[0]
    input_name.insert(END,formatedname)
    root.title(formatedname)
    text_file=open(name,'r')
    paragraph=text_file.read()
    text_1.insert(END,paragraph)
    text_file.close()

def saveimage():
    input_file=input_name.get()
    file=open(input_file+".txt","w")
    data=text_1.get(1.0,END)
    print(data)
    file.write(data)
    input_name.delete(0,END)
    text_1.delete(1.0,END)
    tkmb.showinfo("update","success")
    
def closeimage():
    root.destroy()

btn_open=Button(root,image=open_image,command=openimage)
btn_open.place(relx=0.05,rely=0.03,anchor=CENTER)
btn_save=Button(root,image=save_image,command=saveimage)
btn_save.place(relx=0.11,rely=0.03,anchor=CENTER)
btn_close=Button(root,image=exit_image,command=closeimage)
btn_close.place(relx=0.17,rely=0.03,anchor=CENTER)


root.mainloop()

