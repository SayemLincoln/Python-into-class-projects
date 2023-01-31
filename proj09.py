#Proj08 by Sayem Lincoln

import string

def open_file():                                                #open file function
    while True:
        filename = input('Enter a file name: ')                 #file name input
        try:
            f = open(filename)                                  #opening dictionary file
            return f
        except:
            print ('Error -- Enter a file name: einstein.txt') 

def read_data(fp):                                              #Read file function 
    dic = {}
    number_of_line = 1
    for line in fp:                                             #for line in file loop
        for punct in string.punctuation:                        # for punctuation in line loop
            line = line.replace(punct,'')            
        line = line.lower().strip().split()
        for word in line:                                       #for word in line loop
            if word.isalpha() and len(word) > 1:                #boolean for alphabet and word
                if dic.get(word) == None:                       #boolean for finding word
                    dic[word] = set()                           #addition of word 
                dic[word].add(number_of_line)                   #giving out number of lines
        number_of_line += 1
    return dic

def find_cooccurance(D, inp_str):                               #occurance function
    if len(inp_str) != 0:                           
        for punct in string.punctuation:                        #loop for punctuation removal 
            inp_str = inp_str.replace(punct,'') 
        inp_str = inp_str.strip().split()
        line_set = set()                            
        for word in inp_str:                                    #for word in input string loop
            if D.get(word) != None:                             #boolean for word in file
                if len(line_set) == 0:
                    line_set = line_set.union(D[word])          #finding set union
                else:
                    line_set = line_set.intersection(D[word])   #finding set intersection

        line_list = list(line_set)                              #creating list of sets
        line_list.sort()                                        #sorting list 
        return line_list
    else:
        return 'None.'
    

def main():                                                     #main function
    f = open_file()                                             #function call back
    print ()
    D = read_data(f)                                            #function call back
    while True:
        inp_str = input('Enter space-separated words: ')        #input command line
        inp_str = inp_str.lower()
        if inp_str == 'q' or inp_str == 'Q':                    #input command line
            break
        result = find_cooccurance(D, inp_str)                   #function call back
        if len(inp_str) != 0:                                   
            inp_str = inp_str.strip().split()
            inp_str = ', '.join(inp_str)
            print ('The co-occurance for: ', inp_str)
            if result == []:                                    #empty output boolean
                result = 'None.'
            else:                                               #non-empty output boolean
                result = list(map(lambda x: str(x), result))
                result = ', '.join(result)
            print ('Lines: ', result)
            print()
        else:
            print ('The co-occurance for: ', inp_str)
            print ('Lines: ', result)
            print()
            
        
        
if __name__ == "__main__":
    main()        

# Questions
# Q1: 5
# Q2: 3
# Q3: 4
# Q4: 6
# Q5: 7            
        
