from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from lib import *
from threading import *
import tkinter.font as tkFont
import json
from tkinter import simpledialog
from PIL import Image


class PhnxWindow:
    def __init__(self,window):
        self.trans = ""
        self.statement = ""
        self.winSetup(window)
        self.setup(window)
        self.accSetup()
        self.modalSetup(window)
        self.status_text = []
        
        #self.status = Label(text="")

    def setup(self,window):
        self.canvas = Canvas(
            window,
            bg = "#ffffff",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.grip = Label(bg="white", height = 1)
        self.grip.pack(side="top", fill="x")

        self.g1 = Grip(self.grip)

        self.background_img = PhotoImage(file = f"img/background.png")
        self.background = self.canvas.create_image(
            400.0, 300.0,
            image=self.background_img)
        
        #Generate
        self.img0 = PhotoImage(file = f"img/img0.png")
        self.b0 = Button(
            window,
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btnGenClicked,
            relief = "flat")

        self.b0.place(
            x = 339, y = 436,
            width = 121,
            height = 57)


        #transaction
        self.img1 = PhotoImage(file = f"img/img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btnTransClicked,
            relief = "flat")

        self.b1.place(
            x = 250, y = 291,
            width = 81,
            height = 38)
        self.txtTrans = Label(text = "")
        

        #close
        self.img2 = PhotoImage(file = f"img/img2.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = window.destroy,
            relief = "flat")

        self.b2.place(
            x = 762, y = 8,
            width = 30,
            height = 30)

        # #minimize
        # self.img3 = PhotoImage(file = f"img/img3.png")
        # self.b3 = Button(
        #     image = self.img3,
        #     borderwidth = 0,
        #     highlightthickness = 0,
        #     #command = btn_clicked,
        #     relief = "flat")

        # self.b3.place(
        #     x = 726, y = 8,
        #     width = 30,
        #     height = 30)

        #statement
        self.img4 = PhotoImage(file = f"img/img4.png")
        self.b4 = Button(
            image = self.img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btnStatementClicked,
            relief = "flat")

        self.b4.place(
            x = 250, y = 351,
            width = 81,
            height = 38)

        self.txtStatement = Label(text = "")
        

        
        #ir name
        self.entry0_img = PhotoImage(file = f"img/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            289.5, 163.5,
            image = self.entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#c0c0c0",
            highlightthickness = 0)

        self.entry0.place(
            x = 141, y = 151,
            width = 297,
            height = 23)
        #ir id
        self.entry1_img = PhotoImage(file = f"img/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            649.0, 160.5,
            image = self.entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#c0c0c0",
            highlightthickness = 0)

        self.entry1.place(
            x = 550, y = 148,
            width = 198,
            height = 23)
        #utr no
        self.entry2_img = PhotoImage(file = f"img/img_textBox2.png")
        self.entry2_bg = self.canvas.create_image(
            289.5, 204.5,
            image = self.entry2_img)

        self.entry2 = Entry(
            bd = 0,
            bg = "#c0c0c0",
            highlightthickness = 0)

        self.entry2.place(
            x = 141, y = 192,
            width = 297,
            height = 23)

        #amount
        self.entry3_img = PhotoImage(file = f"img/img_textBox3.png")
        self.entry3_bg = self.canvas.create_image(
            649.0, 201.5,
        image = self.entry3_img)

        self.entry3 = Entry(
            bd = 0,
            bg = "#c0c0c0",
            highlightthickness = 0)

        self.entry3.place(
            x = 550, y = 189,
            width = 198,
            height = 23)

        #bank name
        self.entry4_img = PhotoImage(file = f"img/img_textBox4.png")
        self.entry4_bg = self.canvas.create_image(
            289.5, 245.5,
            image = self.entry4_img)

        self.entry4 = Entry(
            bd = 0,
            bg = "#c0c0c0",
            highlightthickness = 0)

        self.entry4.place(
            x = 141, y = 233,
            width = 297,
            height = 23)

        #date
        self.entry5_img = PhotoImage(file = f"img/img_textBox5.png")
        self.entry5_bg = self.canvas.create_image(
            649.0, 242.5,
            image = self.entry5_img)

        self.entry5 = Entry(
            bd = 0,
            bg = "#c0c0c0",
            highlightthickness = 0)

        self.entry5.place(
            x = 550, y = 230,
            width = 198,
            height = 23)

    def winSetup(self,window):
        self.window_width = 800
        self.window_height = 600

        # get the screen dimension
        self.screen_width = window.winfo_screenwidth()
        self.screen_height = window.winfo_screenheight()

        # find the center point
        self.center_x = int(self.screen_width/2 - self.window_width / 2)
        self.center_y = int(self.screen_height/2 - self.window_height / 2)

        # set the position of the window to the center of the screen
        window.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')

        window.configure(bg = "#ffffff")
        window.overrideredirect(True)
        window.attributes('-topmost',True)

    def browse(self):
        filename = fd.askopenfilename()
        print(filename)
        return filename

    def btnGenClicked(self):
        self.c.place(x = 40, y = 65)
        t1=Thread(target=self.processData)
        t1.start()

    def btnTransClicked(self):
        self.trans = self.browse()
        self.txtTrans.config(text=self.trans)
        if(self.trans != ""):
            self.txtTrans.place(
                x = 350, y = 299,
                height = 20)
        else:
            self.txtTrans.place_forget()

    def btnStatementClicked(self):
        self.statement = self.browse()
        self.txtStatement.config(text=self.statement)
        if(self.statement != ""):
            self.txtStatement.place(
                x = 350, y = 359,
                height = 20)
        else:
            self.txtStatement.place_forget()

    def processData(self):
        irName = self.entry0.get()
        irID = self.entry1.get()
        utrNo = self.entry2.get()
        amount = self.entry3.get()
        bankName = self.entry4.get()
        date = self.entry5.get()

        pd = PaymentDetails(utrNo,amount,bankName, date)
        fi = ICReqFormInput(irName,irID, pd)
        obj = PhnxICForm(fi)

        obj.processData() # -> ICRequestForm.pdf
        #self.status.config(text = "ICRequestForm.pdf generated !!")
        self.updateProc("ICRequestForm.pdf generated !!")

        if(not(self.trans.endswith('.pdf'))):
            obj.img2pdf(self.trans,"pdf/trans.pdf") # -> trans.pdf
            #self.status.config(text = "trans.pdf generated !!")
            self.updateProc("trans.pdf generated !!")
            self.trans = 'pdf/trans.pdf'

        if(not(self.statement.endswith('.pdf'))):
            obj.img2pdf(self.statement,"pdf/statement.pdf") # -> statement.pdf
            #self.status.config(text = "trans.pdf generated !!")
            self.updateProc("statement.pdf generated !!")
            self.statement = 'pdf/statement.pdf'


        #Mailing process
        p1 = Phnx_Mail(fi,self.statement, self.trans)
        p1.sendMail()

        messagebox.showinfo("Phoenix", "Mail sent !!")

        self.c.place_forget()
        for txt in self.status_text:
            self.c.delete(txt)
        

    def modalSetup(self,window):
        self.c = Canvas(
            bg = "#ffffff",
            height = 490,
            width = 715,
            bd = 0,
            highlightthickness = 1,
            relief = "flat")

        self.modal_bg_tl_img = PhotoImage(file = f"img/tl.png")
        self.modal_bg_tl = self.c.create_image(
            60.0, 130.0,
            image=self.modal_bg_tl_img)

        self.modal_bg_br_img = PhotoImage(file = f"img/br.png")
        self.modal_bg = self.c.create_image(
            620.0, 370.0,
            image=self.modal_bg_br_img)


        file=f"img/1fW0bkup.gif"
        info = Image.open(file)
        self.frames = info.n_frames
        print(self.frames)
        self.im = [PhotoImage(file=file,format=f"gif -index {i}") for i in range(self.frames)]
        self.count = 0
        print(self.im.count)

        

        self.gif_label = Label(self.c,image="")
        self.gif_label.place(x=250, y = 40)

        t1=Thread(target= lambda : self.animation(window,0))
        t1.start()

        self.c.create_text(363,275,text = "Processing..", fill = "#262626", font = ('Segoe UI Light', 18))
        self.c_y = 305
        #self.c.place(x = 40, y = 65)

    def updateProc(self, status):
        self.status_text.append(self.c.create_text(360, self.c_y, text= status, fill = "#262626", font = ('Segoe UI Light', 12) ))
        self.c_y = self.c_y + 20

    def accSetup(self):
        self.f = open("acc.json","r")
        self.jo = json.loads(self.f.read())
        print(self.jo)
        self.f.close()
        self.label = Label(text = self.jo["account"], bg="#FFFFFF", fg = "#1f8dba")
        self.label.place(
            x = 580, y = 60
        )
        self.label.bind("<Button-1>",self.updateAcc)
        # clone the font, set the underline attribute,
        # and assign it to our widget
        self.f = tkFont.Font(self.label, self.label.cget("font"))
        self.f.configure(underline = True)
        self.label.configure(font=self.f)

    def updateAcc(self,event):
        self.userIP = simpledialog.askstring(title="Change email ID",prompt="your mail ID ? :")
        print(self.userIP)
        if(self.userIP != None):
            with open("acc.json", "r") as jsonFile:
                data = json.load(jsonFile)

            data["account"] = self.userIP
            
            with open("acc.json", "w") as jsonFile:
                json.dump(data, jsonFile)

            self.label.config(text=self.userIP)

    def animation(self,window,count):
        im2 = self.im[count]

        self.gif_label.configure(image=im2,height =215, width = 235)
        self.count += 1
        if self.count == self.frames:
            self.count = 0
        anim = window.after(50,lambda :self.animation(window,self.count))