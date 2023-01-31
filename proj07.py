# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:02:48 2017

@author: srlin
"""
#Proj07 by Sayem Lincoln
# Uncomment the following lines when you run the run_file tests
# so the input shows up in the output file.
#
#import sys
#def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str
#

def open_file(): #open file function
    while True:
        
        o=input("Filename: ") #file name input
        try:
            fp=open(o,'r') #opening dictionary file
            break
        
        except:
            print("Error in filename.") #file name error print
            continue
        
    return fp
    
def read_file(fp): #file read function
    n = int(fp.readline()) 
    n = int(n)
    network = []
    for i in range(n):
        network.append([])

    a = 0 
    for i in network: #assigning index value to list within network list
        i.append(a)
        a = a + 1
        
    while True: 
       line = fp.readline() # read line
       line = line.split(" ") #split line
       
       try: #taking string to int value
         num1 = int(line[0]) 
         num2 = int(line[1])
       except:
           break
       
       for i in network:
            #joining number to lists
           if i[0] == num1: 
               i.append(num2) #append to i
           if i[0] == num2:
               i.append(num1) #append to i
               
    #taking index of lists away
    for i in network: 
        i.pop(0)
        
    return network , n
    
def num_in_common_between_lists(list1, list2):
    count = 0
    for m in list1: #finding common in list 1 
        for n in list2: #finding common in list 2
            if n == m:
                count = count +1
            
    return count


def init_matrix(n):
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
            
    return matrix
    
def calc_similarity_scores(network,n): 
    mtx = init_matrix(n)
    for m in range(n): #finding m in range of n
        
        for c in range(n): #finding c in range of n
            mtx[m][c] = num_in_common_between_lists(network[m],network[c]) #finding number common within lists
            
    return mtx 

def recommend(user_id,network,similarity_matrix):
    index= None
    y = similarity_matrix[user_id] #defining similarirty matrix
    y[y.index(max(y))] = 0 #max simmilarity(yourself) turned to zero
    while True:
        
      index = y.index(max(y)) #defining new max similarity already friend 
      frd = False
      
      for i in network[user_id]: #finding new max similarity
          if index == i:
              y[index] =0
              frd = True 
              
      if frd == True: #if already friend condition
          continue
      else:
          
          return index
          break


def main():
    ans=''
    print("Facebook friend recommendation.") 
    network, n= read_file(open_file()) #calling function 
    m=n-1
    integer=input("Enter an integer in the range 0 to " + str(m) + ": ") #value input
    while True:
        
        while not integer.isdigit(): #loop for verification of value input
            print("Error: input must be an int between 0 and 9") #error print statement
            integer=input("Enter an integer in the range 0 to " + str(m) + ": ") #value input
            
        integer=int(integer)
        if (integer>= 0) and (integer<=m):
                rec = recommend(integer,network,calc_similarity_scores(network,n)) 
                print("The suggested friend for" , integer,  "is" , rec)
                ans=input("Do you want to continue (yes/no)? ") #user yes/no input
                ans=ans.lower()
                
                while ans=='yes':
                    integer=input("Enter an integer in the range 0 to " + str(m) + ": ") #value input
                    integer=int(integer)
                    rec = recommend(integer,network,calc_similarity_scores(network,n))
                    print("The suggested friend for" , integer,  "is" , rec) 
                    ans=input("Do you want to continue (yes/no)? ") #user yes/no input
                    ans=ans.lower()
                    
                else:
                    break 
        else:
                print("Error: input must be an int between 0 and 9") #error print statement
        integer=input("Enter an integer in the range 0 to " + str(m) + ": ") #value input
        
if __name__ == "__main__":
    main()
    
# Questions
# Q1: 5
# Q2: 3
# Q3: 4
# Q4: 6
# Q5: 7