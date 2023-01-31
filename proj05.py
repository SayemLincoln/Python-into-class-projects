#proj05 by Sayem Lincoln
#get_char function
def get_char(ch, shift): #get_char function
    if (ord(ch) >= 65 and ord(ch) <= 90): #ascii alogrithm and condition
        num = (ord(ch) - 65 + shift) % 26
        shift = chr(num + 65) #finds shift
        return shift
    else:
        return ch

def get_shift(s, ignore): #get_shift function 
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count_num = []  

    for char in chars: #finding char loop in ciphered text
        count = s.count(char)
        count_num.append(count)

    for lt in ignore:#repeated character and shift finding loop
        count_num[chars.index(lt)] = 0
    most_num = max(count_num)
    position = count_num.index(most_num)
    ch_max = chars[position]
    E_postion = 4
    shift = E_postion - position
    return(shift,ch_max)

def output_plaintext(s, shift):#output_plaintext function
    plain = ""
    for char in s: #loop for char in s
        plain= plain+(get_char(char, shift))
    return plain

def main():
    ans = ""
    ignore =""
   
    #print and input statements
    print("Cracking a Caesar cypher.")
    ct = input("Enter text to cipher: ")
    print()
    ct = ct.upper()
   
    #while loop for yes response
    while ans != "yes":
        #print and input statements
        shift, CH_max = get_shift(ct, ignore) 
        ignore += CH_max
        print(output_plaintext(ct, shift))
        print()
        ans = input("Is this correct?(yes/no): ")

if __name__ == "__main__":
    main()
# Questions
# Q1: 7
# Q2: 3
# Q3: 3
# Q4: 6
# Q5: 1

