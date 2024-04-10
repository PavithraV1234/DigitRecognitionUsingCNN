from keras.models import load_model
from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np
from num2words import num2words

model = load_model('mnist.h5')
a=0
b=0
print(type(model))
def predict_digit(img):
    #resize image to 28x28 pixels
    img = img.resize((28,28))
    #convert rgb to grayscale
    img = img.convert('L')
    
    img = np.array(img)

    #reshaping to support our model input and normalizing
    img = img.reshape(1,28,28,1)
    img = img/255.0
    #predicting the class
    res = model.predict([img])[0]
    return np.argmax(res), max(res)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.x = self.y = 0
        self.title("DigiRecog-Handwritten Digit Recognition System using Machine Learning")
        

        # Creating elements
        self.canvas = tk.Canvas(self, width=300, height=300, bg = "black", cursor="cross")
        self.label = tk.Label(self, text="Draw..", font=("Helvetica", 48))
        self.classify_btn = tk.Button(self, text = "Recognise", command = self.classify_handwriting) 
        self.button_clear = tk.Button(self, text = "Clear", command = self.clear_all)
        self.canvass = tk.Canvas(self, width=300, height=300, bg = "black", cursor="cross")
        self.labell = tk.Label(self, text="Draw..", font=("Helvetica", 48))
        self.classify_btnn = tk.Button(self, text = "Recognise", command = self.classify_handwritingg) 
        self.button_clearr = tk.Button(self, text = "Clear", command = self.clear_alll)
        self.labelll = tk.Label(self, text=str("["+str(10*a+b)+" ,"+num2words(10*a+b)+"]") , font=("Helvetica", 20))
        self.classifyy_btnn = tk.Button(self, text = "Recognise double digit", command = self.classifyy_handwritingg) 

        # Grid structure
        self.canvas.grid(row=0, column=0, pady=2, sticky=W, )
        self.label.grid(row=1, column=0,pady=2, padx=2)
        self.classify_btn.grid(row=2, column=0, pady=2, padx=2)
        self.button_clear.grid(row=3, column=0, pady=2)
        self.canvass.grid(row=0, column=1, pady=2, sticky=W, )
        self.labell.grid(row=1, column=1,pady=2, padx=2)
        self.classify_btnn.grid(row=2, column=1, pady=2, padx=2)
        self.button_clearr.grid(row=3, column=1, pady=2)
        self.labelll.grid(row=4, column=0, pady=2,padx=2)
        self.labelll.place(relx = 0.5, rely = 0.96, anchor = CENTER)
        self.classifyy_btnn.grid(row=4, column=1, pady=2, padx=2)
        self.classifyy_btnn.place(relx = 0.5, rely = 0.88, anchor = CENTER)
        

        
        self.canvas.bind("<B1-Motion>", self.draw_lines)
        self.canvass.bind("<B1-Motion>", self.draw_liness)

    def clear_all(self):
        self.canvas.delete("all")
    def clear_alll(self):
        self.canvass.delete("all")

     
    def classify_handwriting(self):
        if self.canvas.find_all()!=():
            HWND = self.canvas.winfo_id() # get the handle of the canvas
            rect = win32gui.GetWindowRect(HWND) # get the coordinate of the canvas
            im = ImageGrab.grab(rect)
            
            

            digit, acc = predict_digit(im)
            self.label.configure(text= str(digit)+', '+ str(int(acc*100))+'%')
            return digit
        
    def classify_handwritingg(self):
        if self.canvass.find_all()!=():
            HWNDD = self.canvass.winfo_id() # get the handle of the canvas
            rectt = win32gui.GetWindowRect(HWNDD) # get the coordinate of the canvas
            imm = ImageGrab.grab(rectt)
            
            

            digitt, accc = predict_digit(imm)
            self.labell.configure(text= str(digitt)+', '+ str(int(accc*100))+'%')
            return digitt
    def classifyy_handwritingg(self):
        a=App.classify_handwriting(self)
        b=App.classify_handwritingg(self)
        self.labelll.configure(text="["+str(str(10*a+b)+" ,"+num2words(10*a+b))+"]")

    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r=10
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill="white",outline="white")
    def draw_liness(self, event):
        self.x = event.x
        self.y = event.y
        r=8
        self.canvass.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill="white",outline="white")
app = App()
mainloop()