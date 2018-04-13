# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 19:12:31 2017

@author: glenn

Student name: Glenn Solomon
Student number: 040908930

"""



"""
---------------------------THIS PROGRAM IS FOR PYTHON 3.x-------------------------------------

"""

import tkinter as tk
from tkinter.messagebox import *
 
class hello:
    def __init__(self, top):
        B1=tkinter.Button(top, text='English', command = self.english_hello).grid(row=1, column=0)
    
        B2=tkinter.Button(top, text='Spanish', command = self.spanish_hello).grid(row=2, column=1)
        
        B3=tkinter.Button(top, text='French', command= self.french_hello).grid(row=3, column=2)
        
    def english_hello(self):
        showinfo("English Hello", "Hello Glenn")
    
    def spanish_hello(self):
        showinfo("Spanish Hello", "Hola Glenn")
    
    def french_hello(self):
        showinfo("French Hello", "Bonjour Glenn")
    
    


#B1.pack()
#B2.pack()
#B3.pack()

def main_loop():
    top=tk.Tk()
    buttons=hello(top)
    top.mainloop()

if __name__=="__main__":main_loop()