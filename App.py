import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



try:
    connection = mysql.connector.connect(
        host='localhost',
        database='student system',
        user='admin',            
        password='123456'
    )
    if connection.is_connected():
        cursor = connection.cursor()
        print("Success Connect")
except Error as e:
    print(" Error Check:", e)
    exit()

connection.commit()

class Login:

        def __init__(self,master):

            self.master = master
            self.master.geometry('400x250')
            self.master.title('Login')
            self.master.configure(background=("lightblue"))
            self.master.resizable(False,False)
            self.success= False

            self.credentials = {
            "mohanad": "312002"
        }

            self.lbl_title = Label(self.master, text="Login System", font=("Arial", 18), bg="lightblue")
            self.lbl_title.pack(pady=10)

            self.lbl_user= Label (self.master, text="Username",font=("Arial",18),bg="lightblue")
            self.lbl_user.pack(pady=5)
            self.entry_username=Entry(self.master,font=("Arial",12)) 
            self.entry_username.pack(pady=5)

            self.lbl_password= Label (self.master, text="Password",font=("Arial",18),bg="lightblue")
            self.lbl_password.pack(pady=5)
            self.entry_password=Entry(self.master,font=("Arial",12),show="*") 
            self.entry_password.pack(pady=5)

            self.btn_login = Button(self.master, text="Login", font=("Arial", 12), command=self.check_login)
            self.btn_login.pack(pady=10)

            self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        def check_login(self):
            username = self.entry_username.get().strip()
            password = self.entry_password.get().strip()

            if username in self.credentials:
                if self.credentials[username] == password:
                    self.success = True
                    # messagebox.showinfo("Success", "Login Successful!")
                    self.master.destroy()
                else:
                    messagebox.showerror("Error", "Invalid password")
            else:
                messagebox.showerror("Error", "Invalid username")

        def on_closing(self):

            self.master.destroy()    

class Student :

        def __init__(self,root):
            self.root = root
            self.root.geometry('1350x690+1+1')
            self.root.title('Student Management System')
            self.root.configure(background=("silver"))
            self.root.resizable(False,False)
            title= Label(self.root,
            text="[Student-Registration-System]",
            bg="#749cf8",
            font= ('monospace',14,'bold'),
            fg="White")
            title.pack(fill=X)

            #  Varibles #
        
            self.id_var = StringVar()
            self.name_var = StringVar()
            self.email_var = StringVar()
            self.phone_var = StringVar()
            self.certi_var = StringVar()
            self.gender_var = StringVar()
            self.address_var =StringVar()
            self.del_var=StringVar()
            self.se_var = StringVar()  

            #-----------------------------------------#
            # manage app #
            manage_frame =Frame(self.root , bg ='white' )
            manage_frame.place(x=0,y=30,width=200,height=400)

            label_id = Label(manage_frame, text="ID-Number",bg="white")
            label_id.pack()
            id_entry = Entry(manage_frame,textvariable=self.id_var, bd='2',justify='center') 
            id_entry.pack()

            label_name = Label(manage_frame,text="Student-Name",bg="white")
            label_name.pack()
            name_entry = Entry(manage_frame,textvariable=self.name_var,bd="2",justify='center')
            name_entry.pack()

            label_email = Label(manage_frame,text="E-mail",bg="white")
            label_email.pack()
            email_entry = Entry(manage_frame,textvariable=self.email_var,bd="2",justify="center")
            email_entry.pack()

            label_phone = Label(manage_frame,text="Phone-Number",bg="white")
            label_phone.pack()
            phone_entry = Entry(manage_frame,textvariable=self.phone_var,bd="2",justify="center")
            phone_entry.pack()

            label_certi = Label(manage_frame,text="Qualifications",bg="white")
            label_certi.pack()
            certi_entry = Entry(manage_frame,textvariable=self.certi_var,bd="2",justify="center")
            certi_entry.pack()

            label_gender = Label(manage_frame,text="Select-Gender", bg="white")
            label_gender.pack()
            combo_gender = ttk.Combobox(manage_frame,textvariable=self.gender_var,justify='center')
            combo_gender['value']= ('Male','Female')
            combo_gender.pack()

            label_address = Label(manage_frame,text="Student-Address",bg="white")
            label_address.pack()
            address_entry = Entry(manage_frame,textvariable=self.address_var,bd="2",justify="center")
            address_entry.pack()

            label_del = Label(manage_frame,text="Delete-Student",fg="red",bg="white")
            label_del.pack()
            del_entry = Entry (manage_frame,textvariable=self.del_var,bd="2",justify="center")
            del_entry.pack()

            #-----------------------------------------------------------------------#
            # button #
            btn_frame = Frame(self.root,bg="white")
            btn_frame.place(x=0,y=435,width=200,height=310)
            title_1 = Label(btn_frame,text="Control panel", fg="white",font=('deco',14),bg='#5da1bf')
            title_1.pack(fill=X)

            add_btn = Button(btn_frame,text='Add Student',bg='#8b9391',fg='white',command=self.add_student)
            add_btn.place(x=35,y=35,width=150,height=30)

            update_btn = Button(btn_frame,text='Edit Student Data',bg='#8b9391',fg='white',command=self.update_student)
            update_btn.place(x=35,y=70,width=150,height=30)

            clear_btn = Button(btn_frame,text='Empty Fields',bg='#8b9391',fg='white',command=self.clear)
            clear_btn.place(x=35,y=105,width=150,height=30)

            delete_btn = Button(btn_frame,text='Delete Student',bg='#8b9391',fg='white',command=self.del_student)
            delete_btn.place(x=35,y=140,width=150,height=30)

            about_btn = Button(btn_frame,text='About Us',bg='#8b9391',fg='white',command=self.about)
            about_btn.place(x=35,y=175,width=150,height=30)

            exit_btn = Button(btn_frame,text='Close the program',bg='#8b9391',fg='white',command=root.quit)
            exit_btn.place(x=35,y=210,width=150,height=30)
            #-----------------------------------------------------------------------#
            # Search frame #

            search_frame = Frame(self.root,bg="white")
            search_frame.place(x=203,y=31,width=1142,height=50)

            lbl_search = Label(search_frame,text="Search For a Student",bg='white')
            lbl_search.place(x=35,y=12)

            self.combo_search = ttk.Combobox(search_frame,justify='left')
            self.combo_search['value']=('ID','Name','E-mail','Phone')
            self.combo_search.place(x=160,y=12)

            search_entry = Entry (search_frame,textvariable=self.se_var,justify='left',bd='2')
            search_entry.place(x=330,y=12)

            search_btn = Button(search_frame,text="Search",justify='center', bg='#549fa0',fg='white',command=self.search)
            search_btn.place(x=480,y=12)
            #-----------------------------------------------------------------------#
            # Details #

            detail_frame = Frame(self.root,bg='#e7eded')
            detail_frame.place(x=203,y=83,width=1142,height=605)

            scrol_x= Scrollbar(detail_frame,orient=HORIZONTAL)
            scrol_y =Scrollbar(detail_frame,orient=VERTICAL)

            #tree view #
            self.student_table = ttk.Treeview(detail_frame,
            columns=('ID','Name','E-mail','Phone','Qualifications','Gender','Address'),
            xscrollcommand=scrol_x.set,
            yscrollcommand=scrol_y.set)
            self.student_table.place(x=5,y=1,width=1120,height=585) 
            scrol_x.pack(side=BOTTOM , fill=X)
            scrol_y.pack(side=RIGHT , fill=Y)

            self.student_table ['show']='headings'
            self.student_table.heading('ID',text="ID-Number")
            self.student_table.heading('Name',text="Student-Name")
            self.student_table.heading('E-mail',text="E-mail") 
            self.student_table.heading('Phone',text="Phone-Number") 
            self.student_table.heading('Qualifications',text="Student-Qualifications")
            self.student_table.heading('Gender',text="Gender")
            self.student_table.heading('Address',text="Address")


            self.student_table.column('ID',width=20)
            self.student_table.column('Name',width=120)
            self.student_table.column('E-mail',width=100)
            self.student_table.column('Phone',width=65)
            self.student_table.column('Qualifications',width=70)
            self.student_table.column('Gender',width=50)
            self.student_table.column('Address',width=100)

            self.view_student()
            self.student_table.bind("<ButtonRelease-1>",self.get_cursor)

        def add_student(self):

            cursor.execute("insert into studentsinfo values (%s,%s,%s,%s,%s,%s,%s)",(
                                                                        self.id_var.get(),
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.phone_var.get(),
                                                                        self.certi_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.address_var.get()))
            self.view_student()
            connection.commit()
            self.clear()

        def view_student(self):
            
            cursor.execute("select * from studentsinfo")
            rows = cursor.fetchall()
            if len(rows) !=0 :
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("",END,values=row)

        def del_student(self):

            cursor.execute("delete from studentsinfo where id= %s",(self.del_var.get(),))
            connection.commit()
            self.view_student()

        def clear(self):
            
            self.id_var.set('')
            self.name_var.set('')
            self.email_var.set('')
            self.phone_var.set('')
            self.certi_var.set('')
            self.gender_var.set('')
            self.address_var.set('')
            self.del_var.set('')

        def get_cursor(self,ev):
            cursor_row = self.student_table.focus()

            if not cursor_row:
                return

            contents=self.student_table.item(cursor_row)
            row = contents['values']
            self.id_var.set(row[0])
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.phone_var.set(row[3])
            self.certi_var.set(row[4])
            self.gender_var.set(row[5])
            self.address_var.set(row[6])

        def update_student(self):
            
            cursor.execute("""
                    UPDATE studentsinfo 
                    SET name = %s, email = %s, phone = %s, Qualifications = %s, gender = %s, address = %s
                    WHERE id = %s
                    """, (
                            self.name_var.get(),
                            self.email_var.get(),
                            self.phone_var.get(),
                            self.certi_var.get(),
                            self.gender_var.get(),
                            self.address_var.get(),
                            self.id_var.get()
                        ))
            self.view_student()
            connection.commit()
            self.clear()

        def search(self):
            search_by = self.combo_search.get()  
            search_value = '%' + self.se_var.get() + '%'   

            query = f"SELECT * FROM studentsinfo WHERE {search_by} LIKE %s"
            cursor.execute(query, (search_value,))
            rows = cursor.fetchall()

            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)

        def about(self):
            
            messagebox.showinfo("Created By Engineer: Mohanad Ahmed","Welcome To Student Management System ")

if __name__ == "__main__":
    # أولاً، عرض نافذة تسجيل الدخول
    login_root = Tk()
    login_app = Login(login_root)
    login_root.mainloop()
    
    if login_app.success:
        main_root = Tk()
        app = Student(main_root)
        main_root.mainloop()
    else:
        print("Login was not successful. Exiting the program.")
