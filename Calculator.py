# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:00:20 2020

@author: Dewald
"""

import sys 

Reapeat = False
i = 0
a = 0
Alpha ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Repeat = True
total = 0
Nr1 = ""
enter = ""
def totals():
     Nr1 = input("Enter a number""\n")
     enter = input("Enter the 2nd number""\n")
     for a in range(len(str(Nr1))):
         for i in range(len(Alpha)):  
             if str(Nr1[a]) == Alpha[i]:
                 print("please enter a valid character")
                 sys.exit()
     for a in range(len(str(enter))):
         for i in range(len(Alpha)):  
             if str(enter[a]) == Alpha[i]:
                 print("please enter a valid character for the 2nd number")
                 sys.exit()  
        
     if Add.lower() == "y":
         total = float(Nr1.replace(',', '.')) + float(enter.replace(',', '.'))
         return print("total: " + str(total)) 
         
     if Sub.lower() == "y":    
          total = float(Nr1.replace(',', '.')) - float(enter.replace(',', '.'))
          return print("total: " + str(total))
        
     if Div.lower() == "y":
         total = float(Nr1.replace(',', '.')) / float(enter.replace(',', '.'))
         return print("total: " + str(total))
     
     if Mp.lower() == "y":     
          total = float(Nr1.replace(',', '.')) * float(enter.replace(',', '.'))
          return print("total: " + str(total))        
        
def repeater():
    Repeatstr = input("Do you want to continue using the calculator(Y/N)""\n") 
    if Repeatstr.lower() == "y":
          Repeat == True
    elif Repeatstr.lower() == "n":
            print("Thanks for using this calculator")
            Repeat == False
            sys.exit()
    else: 
        print("Enter a valid character")
        repeater()

while Repeat == True:
    
    Add = input("Do you want to Add a Number(Y/N)""\n")
    if Add.lower() == "y":
        totals()
        repeater()
        Add = "n"
    elif Add.lower() == "n":
        print("====================================")
    else:    
        print("Enter a valid character")
    
    Sub = input("Do you want to Subtract a Number(Y/N)""\n")
    if Sub.lower() == "y": 
        totals()
        repeater()
        Sub = "n"
    
    elif Sub.lower() == "n":
        print("====================================")
    else:    
        print("Enter a valid character")
    
    Div = input("Do you want to Divide a Number(Y/N)""\n")
    if Div.lower() == "y": 
        totals()
        repeater()
        Div = "n"
    elif Div.lower() == "n":
        print("====================================")
    else:    
        print("Enter a valid character")
    
    Mp = input("Do you want to Multiply a Number(Y/N)""\n")
    if Mp.lower() == "y": 
        totals()
        repeater()
        Mp = "n"
    elif Mp.lower() == "n":
        print("====================================")
    else:    
        print("Enter a valid character")
