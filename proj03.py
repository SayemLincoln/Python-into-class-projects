# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 14:37:47 2017

@author: srlin
"""
#Project 03
# by Syaem Lincoln
#dis measns dispended
#x is the total change in store
#z is the total change needed to give back
#y is the input of dollars

nickels=10
dimes=10
quarters=10
pennies=10
x=410
print("\nWelcome to change-making program.")
in_str = input("Enter the purchase price (xx.xx) or `q' to quit: ")
while in_str.lower() != 'q':
    dollar_str, cents_str = in_str.split(".")
  #dis measns dispended 
    dis_nickels=0
    dis_dimes=0
    dis_quarters=0
    dis_pennies=0
    
    y = int(input("Input dollars paid: "))
    if (float(in_str) <= 0) :
        print("Error: Purchase Price must be non-negative")
        in_str = input("Enter the purchase price (xx.xx) or `q' to quit: ")
    elif (y< float(in_str)):
          print("Error: Insufficient Payment.")
    else:
         y= y*100
         n=int(dollar_str + cents_str)
         z = y-n
         print("Change need to give back: ",z,)
         if x<z:
             print("Error: Insufficient funds.")
             break
         
         else:   
             x=x-z 
             while z>=25: 
                 dis_quarters+=1
                 z-=25
                 if quarters>0:
                    quarters-=1
                 else:    
                    quarters==0
             while z>=10:
                  dis_dimes+=1
                  z-=10
                  if dimes>0:
                     dimes-=1
                  else:    
                     dimes==0
             while z>=5:
                  dis_nickels+=1
                  z-=5
                  if nickels>0:
                     nickels-=1
                  else:    
                     nickels==0
             while z>=1:
                   dis_pennies+=1
                   z-=1
                   if pennies>0:
                      pennies-=1
                   else:    
                      pennies==0
                      
         z==0          
         print ("Collect payment below: ")
         print ("Quarters: ", dis_quarters,)
         print ("Dimes: ", dis_dimes,)
         print ("Nickels: ", dis_nickels,)
         print ("Pennies: ", dis_pennies,)
         print ("Stock: " , quarters, "quarters" , dimes, "dimes" , nickels, "nickels" , pennies, "pennies")
         print("Change left in Stock: ",x,)
         in_str = input("Enter the purchase price (xx.xx) or `q' to quit: ")

