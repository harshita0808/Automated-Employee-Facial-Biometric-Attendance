from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #background image
        img=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\2401770.jpg")
        img=img.resize((1530,810),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=810)


        #title of the page
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("Times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=30,width=1530,height=75)
        
        #button
        b1=Button(self.root,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("Times new roman",15,"bold"),bg="green",fg="white")
        b1.place(x=515,y=730,width=500,height=55)

    #=============attendance===================
    def mark_attendance(self,i,n,r,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (r not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{d},{dtString},{d1},Present")


    #============face recognition=============
        
    def face_recog(self):           
        #draw boundary on image
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     #convert into gray scale
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)    #create rectangle on image
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))   #provide confidence acc to formula


                #take data from mysql
                conn = mysql.connector.connect(host="localhost", port=3306, user="root", password="Qwerty@123#4567", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Student_id, Name, RollNumber, Dept from student where Student_id=" + str(id))
                data = my_cursor.fetchone()

                if data and all(data):  # Check if data is not None and all values are not None
                    i,n, r, d = map(str, data)
                    

                    if confidence > 77:
                        cv2.putText(img,f"Student_id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"RollNumber:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Dept:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)  
                        self.mark_attendance(i,n,r,d)                  
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    coord=[x,y,w,y]
                else:
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while video_cap.isOpened():
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()