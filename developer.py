from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #title of the page
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("Times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=30,width=1530,height=75)

        img_bottom=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\attend.jpg")
        img_bottom=img_bottom.resize((1530,720),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        img_bottom=Label(self.root,image=self.photoimg_bottom)
        img_bottom.place(x=0,y=100,width=1530,height=730)

        #frame
        main_frame=Frame(img_bottom,bd=2,bg="grey")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\i.jpg")
        img=img.resize((200,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(main_frame,image=self.photoimg)
        f_lbl.place(x=300,y=0,width=200,height=200)

        #developer info
        dev=Label(main_frame,text="Hello I am Deeksha",font=("times new roman",20,"bold"),bg="white")
        dev.place(x=0,y=5)

        dev=Label(main_frame,text="With a passion for technology and a keen eye for detail,\nI have successfully crafted a cutting-edge solution using face recognition technology.\nIn commitment to efficiency and accuracy shines\n through in the seamless integration of facial recognition,\n ensuring a hassle-free and secure attendance tracking experience. ",font=("times new roman",20,"bold"),bg="white")
        dev.place(x=0,y=30)

        


if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()