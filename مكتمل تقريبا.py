from tkinter import *


subjects = ["معاملات المواد","التقويم المستمر","اعمال تطبيقية","معدل الفروض","الاختبار"]

# البيانات
data = [
    ["مواد"] + subjects,
    ["اللغة العربية",  "", "", "", "", ""],
    ["الرياضيات",  "", "", "", "", ""],
    ["الفيزياء",  "", "", "", "", ""],
    ["العلوم",  "", "", "", "", ""],
    ["الاسلامية", "", "", "",  "", ""],
    ["تاريخ وجغرافيا", "", "",  "", "", ""],
    ["فرنسية", "", "", "", "",  ""],
    ["انجليزية", "", "", "", "", ""],
    ["معلوماتية", "", "", "",  "", ""],
    ["تكنولوجيا", "", "", "",  "", ""],
    ["رسم", "", "", "", "",  ""],
    ["رياضة", "", "", "", "",  ""],
    ["لغة امازيغية", "", "", "",  "", ""],
    ["تثمين المطالعة", "", "",  "", "", ""],
    ["تثمين مشاريع", "", "", "",  "", ""],
]
data2 = [
    ["مواد"] + subjects,
    ["اللغة العربية",  "", "", "", "", ""],
    ["الرياضيات",  "", "", "", "", ""],
    ["الفيزياء",  "", "", "", "", ""],
    ["العلوم",  "", "", "", "", ""],
    ["الاسلامية", "", "", "",  "", ""],
    ["تاريخ وجغرافيا", "", "",  "", "", ""],
    ["فرنسية", "", "", "", "",  ""],
    ["انجليزية", "", "", "", "", ""],
    ["هندسة كهرباءية", "", "", "",  "", ""],
    ["الاقتصاد", "", "", "",  "", ""],
    ["رسم", "", "", "", "",  ""],
    ["رياضة", "", "", "", "",  ""],
    ["لغة امازيغية", "", "", "",  "", ""],
    ["تثمين المطالعة", "", "",  "", "", ""],
    ["تثمين مشاريع", "", "", "",  "", ""],
    ["قانون", "", "", "",  "", ""],
    ["تسيير محاسبي", "", "", "",  "", ""],
]
data3 = [
    ["مواد"] + subjects,
    ["اللغة العربية",  "", "", "", "", ""],
    ["الرياضيات",  "", "", "", "", ""],
    ["الفيزياء",  "", "", "", "", ""],
    ["العلوم",  "", "", "", "", ""],
    ["الاسلامية", "", "", "",  "", ""],
    ["تاريخ وجغرافيا", "", "",  "", "", ""],
    ["فرنسية", "", "", "", "",  ""],
    ["انجليزية", "", "", "", "", ""],
    ["لغة اجنبية ثالثة", "", "", "",  "", ""],
    ["فلسفة", "", "", "",  "", ""],
    ["رسم", "", "", "", "",  ""],
    ["رياضة", "", "", "", "",  ""],
    ["لغة امازيغية", "", "", "",  "", ""],
    ["تثمين المطالعة", "", "",  "", "", ""],
    ["تثمين مشاريع", "", "", "",  "", ""],
]
subjects2 = ["معدل المادة","المعامل"]

data4 = [
    ["مواد"] + subjects2,
    ["اللغة العربية",  "", ""],
    ["الرياضيات",  "", ""],
    ["الفيزياء",  "", ""],
    ["العلوم",  "", ""],
    ["الاسلامية", "", ""],
    ["تاريخ وجغرافيا", "",""],
    ["فرنسية", "", ""],
    ["انجليزية", "", ""],
    ["لغة اجنبية ثالثة", "", ""],
    ["فلسفة", "", ""],
    ["رسم", "", ""],
    ["رياضة", "", ""],
    ["لغة امازيغية", "", ""],
]
def open_page1():
  page1 = Toplevel(window)
  window.title('حساب المعدل العام')
  page1.geometry(window.geometry())
  def open_page1_1():
    page1_1 = Toplevel(page1)
    page1_1.title("سنة اولى")

    def delete_entry(event):
        event.widget.delete(0, END)
 
    def create_table():
        # إزالة الجدول السابق إذا وجد
        for widget in page1_1.winfo_children():
            widget.destroy()

        # إنشاء الجدول باستخدام خلايا الإدخال (Entry)
        for i in range(len(data)):
            for j in range(len(data[i])):
                if i == 0 or j == 0:
                    # استخدم Label لخانات العمود الأول والصف الأول
                    label = Label(page1_1, text=data[i][j], relief=RIDGE, width=10)
                    label.grid(row=i, column=j)
                else:
                    # استخدم Entry لباقي الخلايا
                    entry = Entry(page1_1, width=10, validate='key')
                    entry.insert(END, data[i][j])
                    entry.grid(row=i, column=j)

                    # تحديد القيمة القصوى إلى 20
                    vcmd = (entry.register(lambda text: text.isdigit() and int(text) <= 20), '%P')
                    entry['validatecommand'] = vcmd
                    entry['invalidcommand'] = (entry.register(lambda: entry.delete(0, END)))
                    entry.bind('<Delete>', delete_entry)
                    entry.bind('<BackSpace>', delete_entry)

    create_table()
  def open_page1_2():
    page1_2 = Toplevel(page1)
    page1_2.title("حساب المعدل")
    def delete_entry(event):
        event.widget.delete(0, END)
 
    def create_table2():
        # إزالة الجدول السابق إذا وجد
        for widget in page1_2.winfo_children():
            widget.destroy()

        # إنشاء الجدول باستخدام خلايا الإدخال (Entry)
        for i in range(len(data2)):
            for j in range(len(data2[i])):
                if i == 0 or j == 0:
                    # استخدم Label لخانات العمود الأول والصف الأول
                    label = Label(page1_2, text=data2[i][j], relief=RIDGE, width=10)
                    label.grid(row=i, column=j)
                else:
                    # استخدم Entry لباقي الخلايا
                    entry = Entry(page1_2, width=10, validate='key')
                    entry.insert(END, data2[i][j])
                    entry.grid(row=i, column=j)

                    # تحديد القيمة القصوى إلى 20
                    vcmd = (entry.register(lambda text: text.isdigit() and int(text) <= 20), '%P')
                    entry['validatecommand'] = vcmd
                    entry['invalidcommand'] = (entry.register(lambda: entry.delete(0, END)))
                    entry.bind('<Delete>', delete_entry)
                    entry.bind('<BackSpace>', delete_entry)

    create_table2()
  def open_page1_3():
    page1_3 = Toplevel(page1)
    page1_3.title( "حساب المعدل")

    def delete_entry(event):
        event.widget.delete(0, END)
 
    def create_table():
        # إزالة الجدول السابق إذا وجد
        for widget in page1_3.winfo_children():
            widget.destroy()

        # إنشاء الجدول باستخدام خلايا الإدخال (Entry)
        for i in range(len(data3)):
            for j in range(len(data3[i])):
                if i == 0 or j == 0:
                    # استخدم Label لخانات العمود الأول والصف الأول
                    label = Label(page1_3, text=data[i][j], relief=RIDGE, width=10)
                    label.grid(row=i, column=j)
                else:
                    # استخدم Entry لباقي الخلايا
                    entry = Entry(page1_3, width=10, validate='key')
                    entry.insert(END, data[i][j])
                    entry.grid(row=i, column=j)

                    # تحديد القيمة القصوى إلى 20
                    vcmd = (entry.register(lambda text: text.isdigit() and int(text) <= 20), '%P')
                    entry['validatecommand'] = vcmd
                    entry['invalidcommand'] = (entry.register(lambda: entry.delete(0, END)))
                    entry.bind('<Delete>', delete_entry)
                    entry.bind('<BackSpace>', delete_entry)

    create_table()

  bt1 = Button(page1, text="سنة اولى ثانوي علوم", fg='black', bg='white', width=15, height=1, command=open_page1_1)
  bt1.place(x=340, y=15)
  bt1=Button(page1,text="سنة اولى ثانوي اداب",fg='black',bg='white',width=15,height=1,command=open_page1_1)
  bt1.place(x=340,y=60)
  bt2=Button(page1,text="سنة ثانية رياضيات",fg='black',bg='white',width=15,height=1,command=open_page1_2)
  bt2.place(x=160,y=15)
  bt2=Button(page1,text="سنة ثانية علوم",fg='black',bg='white',width=15,height=1,command=open_page1_2)
  bt2.place(x=160,y=60)
  bt2=Button(page1,text="سنة ثانية فلسفة",fg='black',bg='white',width=15,height=1,command=open_page1_3)
  bt2.place(x=160,y=105)
  bt2=Button(page1,text="سنة ثانية تسيير ",fg='black',bg='white',width=15,height=1,command=open_page1_2)
  bt2.place(x=160,y=150)
  bt2=Button(page1,text="سنة ثانية لغات",fg='black',bg='white',width=15,height=1,command=open_page1_3)
  bt2.place(x=160,y=195)
  bt2=Button(page1,text="سنة ثانية كهرباء",fg='black',bg='white',width=15,height=1,command=open_page1_2)
  bt2.place(x=160,y=240)
  bt2=Button(page1,text="سنة ثالثة رياضيات",fg='black',bg='white',width=15,height=1,command=open_page1_2)
  bt2.place(x=5,y=15)
  bt2=Button(page1,text="سنة ثالثة علوم",fg='black',bg='white',width=15,height=1,command=open_page1_2)
  bt2.place(x=5,y=60)
  bt2=Button(page1,text="سنة ثالثة فلسفة",fg='black',bg='white',width=15,height=1,command=open_page1_3)
  bt2.place(x=5,y=105)
  bt2=Button(page1,text="سنة ثالثة تسيير ",fg='black',bg='white',width=15,height=1,command=open_page1_2)
  bt2.place(x=5,y=150)
  bt2=Button(page1,text="سنة ثالثة لغات",fg='black',bg='white',width=15,height=1,command=open_page1_3)
  bt2.place(x=5,y=195)
  bt2=Button(page1,text="سنة ثالثة كهرباء",fg='black',bg='white',width=15,height=1,command=open_page1_2)
  bt2.place(x=5,y=240)
  back_button = Button(page1, text="عودة", fg='black', bg='white', width=15, height=1, command=page1.destroy)
  back_button.place(x=340, y=105)
def open_page2():
  page2 = Toplevel(window)
  window.title('سنة ثالثة')
  def open_page2_2():
    page2_2 = Toplevel(page2)
    page2_2.title( "حساب المعدل")

    def delete_entry(event):
        event.widget.delete(0, END)
 
    def create_table3():
        # إزالة الجدول السابق إذا وجد
        for widget in page2_2.winfo_children():
            widget.destroy()

        # إنشاء الجدول باستخدام خلايا الإدخال (Entry)
        for i in range(len(data4)):
            for j in range(len(data4[i])):
                if i == 0 or j == 0:
                    # استخدم Label لخانات العمود الأول والصف الأول
                    label = Label(page2_2, text=data4[i][j], relief=RIDGE, width=20)
                    label.grid(row=i, column=j)
                else:
                    # استخدم Entry لباقي الخلايا
                    entry = Entry(page2_2, width=20, validate='key')
                    entry.insert(END, data4[i][j])
                    entry.grid(row=i, column=j)

                    # تحديد القيمة القصوى إلى 20
                    vcmd = (entry.register(lambda text: text.isdigit() and int(text) <= 20), '%P')
                    entry['validatecommand'] = vcmd
                    entry['invalidcommand'] = (entry.register(lambda: entry.delete(0, END)))
                    entry.bind('<Delete>', delete_entry)
                    entry.bind('<BackSpace>', delete_entry)
    create_table3()
  
  page2.geometry(window.geometry())
  bt1=Button(page2,text="شعبة رياضيات",fg='black',bg='white',width=30,height=1,command=open_page2_2)
  bt1.place(x=120,y=35)
  bt2=Button(page2,text="شعبة علوم",fg='black',bg='white',cursor='heart',width=30,height=1,command=open_page2_2)
  bt2.place(x=120,y=80)
  bt3=Button(page2,text="شعبة اداب وفلسفة",fg='black',bg='white',width=30,height=1,command=open_page2_2)
  bt3.place(x=120,y=125)
  bt4=Button(page2,text= "تسيير واقتصاد" ,fg='black',bg='white',width=30,height=1,command=open_page2_2)
  bt4.place(x=120,y=170)
  bt5=Button(page2,text="هندسة كهرباءية",fg='black',bg='white',width=30,height=1,command=open_page2_2)
  bt5.place(x=120,y=215)
  bt6=Button(page2,text="شعبة لغات اجنبية",fg='black',bg='white',width=30,height=1,command=open_page2_2)
  bt6.place(x=120,y=260)
  back_button = Button(page2, text="عودة", fg='black', bg='white', width=30, height=1, command=page2.destroy)
  back_button.place(x=120, y=305)
def open_page3():
    page3 = Toplevel(window)
    page3.title("حساب المعدل السنوي")
    page3.geometry(window.geometry())
    # يمكنك هنا إضافة عناصر ومحتوى الصفحة الثانية
    def calculate_annual_average():
        total_grade = 0
        total_weight = 3  # عدد الفصول الدراسية
        for i in range(len(entries)):
            grade = float(entries[i].get())
            if grade > 20:
                grade = 20  # قم بتحديد القيمة القصوى للدرجة
            total_grade += grade
        gpa = total_grade / total_weight
        result_label.config(text="المعدل السنوي: {:.2f}".format(gpa))
    
    annual_average_button = Button(page3, text="حساب", fg='black', bg='white', width=30, height=1, command=calculate_annual_average)
    annual_average_button.place(x=120,y=200)

    back_button = Button(page3, text="عودة", fg='black', bg='white', width=30, height=1, command=page3.destroy)
    #back_button.place(x=120, y=200)

    subjects = ["الفصل الأول", "الفصل الثاني", "الفصل الثالث"]
    entries = []
    for i in range(len(subjects)):
        label = Label(page3, text="{}:".format(subjects[i]), font=('Arial', 12), anchor='e')
        label.place(x=50, y=50 + (i * 30))
        entry = Entry(page3, font=('Arial', 12))
        entry.place(x=150, y=50 + (i * 30))
        entries.append(entry)

    result_label = Label(page3, text="المعدل السنوي: ", font=('Arial', 12))
    result_label.place(x=50, y=170)

    back_button = Button(page3, text="عودة", fg='black', bg='white', width=30, height=1, command=page3.destroy)
    back_button.place(x=120,y=250)
#خاصة بحساب معدل الباكالوريا
def open_page4():
  page4 = Toplevel(window)
  page4.title("كيفية استخدام التطبيق")
  page4.geometry(window.geometry())
  back_button = Button(page4, text="عودة", fg='black', bg='white', width=30, height=1, command=page4.destroy)
  back_button.place(x=120, y=160)
window = Tk()
window.lift()
window.geometry('500x500+500+100')
window.title('تطبيق حساب المعدلات')
window.config(background='white')
window.minsize(499,499)
window.maxsize(501, 501)

bt1 = Button(text="حساب المعدل العام", fg='black', bg='white', width=30, height=1, command=open_page1)
bt1.place(x=120, y=80)

bt2 = Button(text="حساب معدل الشهادات", fg='black', bg='white', cursor='heart', width=30, height=1,command=open_page2)
bt2.place(x=120, y=125)

bt3 = Button(text="المعدل السنوي", fg='black', bg='white', width=30, height=1, command=open_page3)
bt3.place(x=120, y=170)

bt4 = Button(text="كيفية استعمال التطبيق", fg='black', bg='white', width=30, height=1, command=open_page4)
bt4.place(x=120, y=215)
str1=Label(text='بسم الله الرحمان الرحيم',fg='black',bg='white',font=10)
str1.place(x=120,y=40)
window.mainloop()