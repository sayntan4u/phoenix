import smtplib
from email.message import EmailMessage
# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from fpdf import FPDF
import json

#Class for mail
class Phnx_Mail:
    def __init__(self, icReqFormInput, statePath, transPath):
        self.msg = EmailMessage()
        self.msg['Subject'] = "iCOUPON REQUEST OF {0}".format(icReqFormInput.PaymentDetails.Amount)
        self.msg['From'] = "maxout.phoenix@gmail.com"
        with open("acc.json", "r") as jsonFile:
                data = json.load(jsonFile)
        self.msg['To'] = data["account"]
        self.msg.set_content('''
Hi Team,

PFA of
1. Screenshot of amount transfer of worth ({6})
2. Icoupon Request Form.

Below are the details:-

Name of Transferor - {0}
Ir Id of Transferor (if any)- {1}
Bank Name- {2}
Date of transaction- {3}
Amount - {4}
UTR no- {5}

Regards
Chandu
        '''.format(icReqFormInput.IRName,
        icReqFormInput.IRID, 
        icReqFormInput.PaymentDetails.BankName, 
        icReqFormInput.PaymentDetails.Date, 
        icReqFormInput.PaymentDetails.Amount, 
        icReqFormInput.PaymentDetails.UTRNo,
        icReqFormInput.PaymentDetails.Amount))

        self.files = {
             'pdf/ICRequestForm.pdf' : 'IC Request Form.pdf',             
             transPath : 'Transfer Screenshot.pdf',
             statePath : 'Statement.pdf'
             }

        for file in self.files:
            with open(file,'rb') as f:
                file_data = f.read()
                file_name = self.files[file]
            
            self.msg.add_attachment(file_data, maintype = 'application', subtype= 'octet-stream', filename = file_name)
            print("added {0}".format(file_name))

    def sendMail(self):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("maxout.phoenix@gmail.com","9474900677S")
            smtp.send_message(self.msg)
            print("sent")

#container class for ICREQFORM
class ICReqFormInput:
    def __init__(self, IRName, IRID, PaymentDetails):
        self.IRName = IRName
        self.IRID = IRID
        self.PaymentDetails = PaymentDetails

#container for BankDetails
class PaymentDetails:
    def __init__(self, UTRNo, Amount, BankName, Date):
        self.UTRNo = UTRNo
        self.Amount = Amount
        self.BankName = BankName
        self.Date = Date

#class for PDFGeneration
class PhnxICForm:
    def __init__(self, icreqformInput):
        self.IRName = icreqformInput.IRName
        self.IRID = icreqformInput.IRID
        self.UTRNo = icreqformInput.PaymentDetails.UTRNo
        self.Amount = icreqformInput.PaymentDetails.Amount
        self.BankName = icreqformInput.PaymentDetails.BankName
        self.Date = icreqformInput.PaymentDetails.Date

    def processData(self):
        img = Image.open('img/IC1.jpg')
        I1 = ImageDraw.Draw(img)
        myFont = ImageFont.truetype('font/ARIAL.TTF', 40)
        I1.text((370, 420), self.IRName, font=myFont, fill =(0, 0, 0))
        I1.text((1170, 420), self.IRID, font=myFont, fill =(0, 0, 0))
        I1.text((480, 830), self.Amount, font=myFont, fill =(0, 0, 0))
        myFont = ImageFont.truetype('font/ARIAL.TTF', 30)
        I1.text((470, 1180), self.UTRNo, font=myFont, fill =(0, 0, 0))
        I1.text((730, 1180), self.Amount, font=myFont, fill =(0, 0, 0))
        I1.text((975, 1180), self.BankName, font=myFont, fill =(0, 0, 0))
        I1.text((1350, 1180), self.Date, font=myFont, fill =(0, 0, 0))
        myFont = ImageFont.truetype('font/ARIAL.TTF', 28)
        listofDenom = self.denominationRequired(self.Amount)
        x=700
        for n in listofDenom: 
            I1.text((x,2100), str(n), font=myFont, fill =(0, 0, 0))
            x=x+160
        img.save("newIC.jpg")
        self.img2pdf("newIC.jpg","pdf/ICRequestForm.pdf")

    def denominationRequired(self,amt):
        retList=[]
        denomlist = [20000,5000,1000,500,100]
        amt = int(amt.replace(",",""))

        for n in denomlist:
            div = amt//n
            retList.append(div)
            if(amt!=0):
                amt = amt - div*n
        return retList

    def img2pdf(self,path,pdfName):
        pdf = FPDF()
        pdf.add_page()
        pdf.image(path, 0, 0, 210, 297) 
        pdf.output(pdfName, "F")
        print("pdf generated")
    
#class for Drag & drop borderless tkinter
class Grip:
    ''' Makes a window dragable. '''
    def __init__ (self, parent, disable=None, releasecmd=None) :
        self.parent = parent
        self.root = parent.winfo_toplevel()

        self.disable = disable
        if type(disable) == 'str':
            self.disable = disable.lower()

        self.releaseCMD = releasecmd

        self.parent.bind('<Button-1>', self.relative_position)
        self.parent.bind('<ButtonRelease-1>', self.drag_unbind)

    def relative_position (self, event) :
        cx, cy = self.parent.winfo_pointerxy()
        geo = self.root.geometry().split("+")
        self.oriX, self.oriY = int(geo[1]), int(geo[2])
        self.relX = cx - self.oriX
        self.relY = cy - self.oriY

        self.parent.bind('<Motion>', self.drag_wid)

    def drag_wid (self, event) :
        cx, cy = self.parent.winfo_pointerxy()
        d = self.disable
        x = cx - self.relX
        y = cy - self.relY
        if d == 'x' :
            x = self.oriX
        elif d == 'y' :
            y = self.oriY
        self.root.geometry('+%i+%i' % (x, y))

    def drag_unbind (self, event) :
        self.parent.unbind('<Motion>')
        if self.releaseCMD != None :
            self.releaseCMD()