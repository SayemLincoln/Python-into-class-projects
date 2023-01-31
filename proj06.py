# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:12:44 2017
@author: srlin
"""
#proj06 by Sayem Lincoln
#imports
from itertools import product
import time
import zipfile
import string

print("Cracking Zip files.") #print statements
print("Warning cracking password is illegal due to law U.S. Code §1030, and has a prison term of 5 years.") #password cracking law

def open_dict_file(): # opening dictionary file function
    while True:
        a=input("Enter dictionary file name: ") #dictionary file input
        try:
            dict_file=open(a,'r') #opening dictionary file
            break
            
        except:
            continue
    return dict_file #returning dictionary file
    
def open_zip_file(): # opening zip file function
    while True:
        filename=input("Enter a zip file name: ") #zip file input
        try:
            Zip_file = zipfile.ZipFile(filename) #opening zip file
            break        
        except:
            continue
    return Zip_file #returning zip file
   

def brute_force_attack(zip_file):
   # while True:
    extracted='' #preset extracted
    for i in range(9):
        for items in product(string.ascii_lowercase, repeat=i): #loop for product
            x=''.join(items)  #joing string for passwords

            try:
                zip_file.extractall(pwd=x.encode()) #trying password
                extracted='yes'
                print("Brute force password is ", x)
                break
            
            except:
                continue
        if extracted == 'yes': #condition for extraction return
            return True
            break

   
    
def dictionary_attack(zip_file, dict_file): # dictionary attcak function
    findout = False  #preset findout
    for line in dict_file: #loop for password
        password=line.strip() 
            
        try: #cracking zip file password
            zip_file.extractall(pwd=password.encode()) 
            findout=True
            if   findout == True:
                 print("Dictioanry attack password is ", password)
                 break
             
        except:
             continue
    dict_file.close() #closing file) 
    return findout  #returning findout     

q=False
while not q: #nested for inputs
    in_str=input("What type of cracking ('brute force','dictionary','both','q'): ")
    
    if in_str == 'q': #if q is input
        break
    
    elif in_str=="brute force": #if brute force is input
        print("This is brute force cracking")
        start = time.process_time() #start time
        Zipfile = open_zip_file()
        brute_force_attack(Zipfile)
        end = time.process_time() #end time
        Elapsed_time=end-start  #calculating time
        print("Brute force Elapsed time: " '{:6.4f}'.format(Elapsed_time))
        
    elif in_str=="dictionary": #if dictionary is input
        print("This is dictionary cracking")
        start = time.process_time() #start time
        dictfile= open_dict_file()
        Zipfile = open_zip_file()
        dictionary_attack(Zipfile, dictfile)
        end = time.process_time() #end time
        Elapsed_time=end-start #calculating time
        print("Dictionary Attack Elapsed time: " '{:6.4f}'.format(Elapsed_time))
        
    elif in_str=="both": #if both is input
         print("Both brute force and dictionary attack cracking")
         start = time.process_time() #start time
         dictfile= open_dict_file()
         Zipfile = open_zip_file()
         end = time.process_time() #end time
         Elapsed_time=end-start #calculating time
         print("Dictionary Attack Elapsed time: " '{:6.4f}'.format(Elapsed_time))
        
         if dictionary_attack(Zipfile, dictfile)==False: #if dictionary attack does not work
            print("No password found.") 
            start = time.process_time() #start time
            brute_force_attack(Zipfile) 
            end = time.process_time() #end time
            Elapsed_time=end-start #calculating time
            print("Brute force Elapsed time: " '{:6.4f}'.format(Elapsed_time))
#Questions
# Q1: 1
# Q2: 7
# Q3: 7
# Q4: 1
# Q5: 1