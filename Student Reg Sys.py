import pymysql
from tkinter import *
import tkinter.messagebox as tm

class AdminPanel(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label_head = Label(self, text="Administrator Panel")
        self.label_head.place(anchor="center")

        self.label_head_emp = Label(self, text="  ")
        self.label_head_emp.place(anchor="center")

        self.label_head.grid(row=0)
        self.label_head.config(font=("Courier", 12))
        self.label_head_emp.grid(row=1)

        self.ent_stu = Button(self, text="Enter Student", command=self._ent_btn_clicked)
        self.ent_stu.grid(columnspan=2)

        self.upd_stu = Button(self, text="Update Student", command=self._upd_btn_clicked)
        self.upd_stu.grid(columnspan=2)

        self.view_stu = Button(self, text="View Student", command=self._view_btn_clicked)
        self.view_stu.grid(columnspan=2)

        self.dele_stu = Button(self, text="Delete Student", command=self._dele_btn_clicked)
        self. dele_stu.grid(columnspan=2)

        self.pack()


    def _ent_btn_clicked(self):
        AdminPanel.destroy(self)

        enter_det = Tk()
        enter_det.title("Student Details")
        stu_det = StuDet(enter_det)

        enter_det.mainloop()

    def _upd_btn_clicked(self):
        AdminPanel.destroy(self)

        update_det = Tk()
        update_det.title("Update Details")
        stu_det = UpdateDet(update_det)

        update_det.mainloop()
            
            
    def _view_btn_clicked(self):
        AdminPanel.destroy(self)

        view_det = Tk()
        view_det.title("View Details")
        vi_det = ViewDet(view_det)

        view_det.mainloop()

            
    def _dele_btn_clicked(self):
        AdminPanel.destroy(self)

        dele_det = Tk()
        dele_det.title("Delete Details")
        de_det = DeleteDet(dele_det)

        dele_det.mainloop()

####################################    ENTER     ##############################################
      
class StuDet(Frame):
    def __init__(self, master):
        super().__init__(master)
    
        
        self.label_head = Label(self, text="Student Details")
        self.label_head.place(anchor="center")
        
        self.label_studentName = Label(self, text="Student Name")
        self.label_studentID = Label(self, text="Student ID")
        self.label_DOB = Label(self, text="Date Of Birth")
        self.label_Course = Label(self, text="Student Course")

        self.entry_studentName = Entry(self)
        self.entry_studentID = Entry(self)
        self.entry_DOB = Entry(self)
        self.entry_Course = Entry(self)

        self.label_head.grid(row=0)
        self.label_head.config(font=("Courier", 12))

        self.label_studentName.grid(row=1, sticky=E)
        self.label_studentName.config(font=("Courier", 10))
        self.label_studentID.grid(row=2, sticky=E)
        self.label_studentID.config(font=("Courier", 10))
        self.label_DOB.grid(row=3, sticky=E)
        self.label_DOB.config(font=("Courier", 10))
        self.label_Course.grid(row=4, sticky=E)
        self.label_Course.config(font=("Courier", 10))
        
        self.entry_studentName.grid(row=1, column=1)
        self.entry_studentID.grid(row=2, column=1)
        self.entry_DOB.grid(row=3, column=1)
        self.entry_Course.grid(row=4, column=1)

        #self.checkbox = Checkbutton(self, text="Keep me logged in")
        #self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Enter", command=self._enter_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()



    def _enter_btn_clicked(self):
        # print("Clicked")
        stuName = self.entry_studentName.get()
        stuID = self.entry_studentID.get()
        stuDOB = self.entry_DOB.get()
        stuCourse = self.entry_Course.get()

        if(len(stuName) == 0 or len(stuID) == 0 or len(stuDOB) == 0 or len(stuCourse) == 0):
            tm.showerror("Entry error", "Please complete the Entries")

        else:
            conn = pymysql.connect(
            host="localhost",
            user="root",
            db="db"
            )

            myCursor = conn.cursor()

            myCursor.execute("INSERT INTO student_db(studentID, studentName, studentDOB, studentCourse) VALUES(%s, %s, %s, %s)", (stuID, stuName, stuDOB, stuCourse))


            conn.commit()
            conn.close()
            
################################    UPDATE      ###############################################

class UpdateDet(Frame):
    def __init__(self, master):
        super().__init__(master)
    
        
        self.label_head = Label(self, text="Update Details")
        self.label_head.place(anchor="center")

        self.label_studentID = Label(self, text="Student ID")

        self.label_head_up = Label(self, text="Enter updated Details")
        self.label_head_up.place(anchor="center")
        
        self.label_studentName = Label(self, text="Student Name")
        self.label_DOB = Label(self, text="Date Of Birth")
        self.label_Course = Label(self, text="Student Course")

        self.entry_studentID = Entry(self)
        self.entry_studentName = Entry(self)
        self.entry_DOB = Entry(self)
        self.entry_Course = Entry(self)
        

        self.label_head.grid(row=0)
        self.label_head.config(font=("Courier", 12))
        
        self.label_studentID.grid(row=1, sticky=E)
        self.label_studentID.config(font=("Courier", 10))

        self.label_head_up.grid(row=2)
        self.label_head_up.config(font=("Courier", 12))

        self.label_studentName.grid(row=3, sticky=E)
        self.label_studentName.config(font=("Courier", 10))
        self.label_DOB.grid(row=4, sticky=E)
        self.label_DOB.config(font=("Courier", 10))
        self.label_Course.grid(row=5, sticky=E)
        self.label_Course.config(font=("Courier", 10))

        self.entry_studentID.grid(row=1, column=1)
        self.entry_studentName.grid(row=3, column=1)
        self.entry_DOB.grid(row=4, column=1)
        self.entry_Course.grid(row=5, column=1)

        #self.checkbox = Checkbutton(self, text="Keep me logged in")
        #self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Update", command=self._enter_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()



    def _enter_btn_clicked(self):
        # print("Clicked")
        stuID = self.entry_studentID.get()
        stuName = self.entry_studentName.get()
        stuDOB = self.entry_DOB.get()
        stuCourse = self.entry_Course.get()

        if(len(stuID) == 0):
            tm.showerror("Entry error", "Please enter student ID")

        else:
            conn = pymysql.connect(
            host="localhost",
            user="root",
            db="db"
            )

            myCursor = conn.cursor()

            myCursor.execute("UPDATE student_db SET studentName = %s, studentDOB = %s, studentCourse = %s WHERE StudentID = %s",(stuName, stuDOB, stuCourse, stuID))


            conn.commit()
            conn.close()


####################################    VIEW     ##############################################
      
class ViewDet(Frame):
    def __init__(self, master):
        super().__init__(master)
    
        
        self.label_head = Label(self, text="View Details")
        self.label_head.place(anchor="center")
        

        self.label_studentID = Label(self, text="Student ID")
        self.entry_studentID = Entry(self)

        self.label_head.grid(row=0)
        self.label_head.config(font=("Courier", 12))

        self.label_studentID.grid(row=2, sticky=E)
        self.label_studentID.config(font=("Courier", 10))
        
        self.entry_studentID.grid(row=2, column=1)

        self.viewbtn = Button(self, text="View", command=self._view_btn_clicked)
        self.viewbtn.grid(columnspan=2)

        self.viewallbtn = Button(self, text="View All Students", command=self._viewall_btn_clicked)
        self.viewallbtn.grid(column=0)

        self.pack()



    def _view_btn_clicked(self):
        # print("Clicked")
        stuID = self.entry_studentID.get()

        if(len(stuID) == 0):
            tm.showerror("Entry error", "Please Enter an ID")

        else:
            conn = pymysql.connect(
            host="localhost",
            user="root",
            db="db"
            )

            myCursor = conn.cursor()

            myCursor.execute("SELECT studentID FROM student_db WHERE studentID = %s", stuID)
            stu_id = myCursor.fetchall()

            myCursor.execute("SELECT studentName FROM student_db WHERE studentID = %s", stuID)
            stu_name = myCursor.fetchall()
            
            myCursor.execute("SELECT studentDOB FROM student_db WHERE studentID = %s", stuID)
            studentDOB = myCursor.fetchall()

            myCursor.execute("SELECT studentCourse FROM student_db WHERE studentID = %s", stuID)
            studentCourse = myCursor.fetchall()
    
            a = Tk()
            text = Text(a)
            text.insert(INSERT, "\n")
            text.insert(INSERT, "Student ID : ")
            text.insert(INSERT, stu_id)
            text.insert(INSERT, "\n")
            text.insert(INSERT, "Student Name : ")
            text.insert(INSERT, stu_name)
            text.insert(INSERT, "\n")
            text.insert(INSERT, "Date of Birth : ")
            text.insert(INSERT, studentDOB)
            text.insert(INSERT, "\n")
            text.insert(INSERT, "Course : ")
            text.insert(INSERT, studentCourse)
            text.pack()
            
            a.mainloop()
 
            conn.commit()
            conn.close()

    def _viewall_btn_clicked(self):
        # print("Clicked")
        stuID = self.entry_studentID.get()

        conn = pymysql.connect(
        host="localhost",
        user="root",
        db="db"
        )

        myCursor = conn.cursor()

        myCursor.execute("SELECT * FROM student_db")
        d = myCursor.fetchall()
    
        b = Tk()
        text = Text(b)

        text.insert(INSERT, "StudentID StudentName DOB Course")
        text.insert(INSERT, "\n")
        
        for r in d:
            text.insert(INSERT, "\n")
            
            text.insert(INSERT, r)

            text.pack()
            
        b.mainloop()
 
        conn.commit()
        conn.close()

####################################    DELETE     ##############################################
      
class DeleteDet(Frame):
    def __init__(self, master):
        super().__init__(master)
    
        
        self.label_head = Label(self, text="Delete Student")
        self.label_head.place(anchor="center")
        

        self.label_studentID = Label(self, text="Student ID")
        self.entry_studentID = Entry(self)

        self.label_head.grid(row=0)
        self.label_head.config(font=("Courier", 12))

        self.label_studentID.grid(row=2, sticky=E)
        self.label_studentID.config(font=("Courier", 10))
        
        self.entry_studentID.grid(row=2, column=1)

        self.viewbtn = Button(self, text="Delete", command=self._dele_btn_clicked)
        self.viewbtn.grid(columnspan=2)

        self.pack()



    def _dele_btn_clicked(self):
        stuID = self.entry_studentID.get()


        if(len(stuID) == 0):
            tm.showerror("Entry error", "Please provide an ID")

        else:
            conn = pymysql.connect(
            host="localhost",
            user="root",
            db="db"
            )

            myCursor = conn.cursor()

            myCursor.execute("DELETE FROM student_db WHERE studentID = %s",stuID)


            conn.commit()
            conn.close()

####################################    LOGIN     ################################################

    
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label_head = Label(self, text="Administrator Login")
        self.label_head.place(anchor="center")
        
        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_head.grid(row=0)
        self.label_head.config(font=("Courier", 12))

        self.label_username.grid(row=1, sticky=E)
        self.label_username.config(font=("Courier", 10))
        self.label_password.grid(row=2, sticky=E)
        self.label_password.config(font=("Courier", 10))
        
        self.entry_username.grid(row=1, column=1)
        self.entry_password.grid(row=2, column=1)

        #self.checkbox = Checkbutton(self, text="Keep me logged in")
        #self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Enter", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()


    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "a" and password == "a":
            
            #tm.showinfo("Login info", "Welcome John")
            root.destroy()

            admin_panel = Tk()
            admin_panel.title("Administrator Panel")
            adm = AdminPanel(admin_panel)

            admin_panel.mainloop()
            
            
        else:
            tm.showerror("Login error", "Incorrect username")


root = Tk()
root.title("Student Registration System")

lf = LoginFrame(root)
root.mainloop()
