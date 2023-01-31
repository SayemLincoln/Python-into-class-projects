#proj11 by Sayem Lincoln

import itertools

class Matrix(object):
    #Adjacency matrix class
    
    def __init__(self):
        #Create and initialize your class attributes
        self._matrix = []
        self._rooms = 0
        
    def read_file(self, fp):  #fp is a file pointer
        #Build an adjacency matrix that you read from a file fp
        self._rooms = int(fp.readline())
        self._matrix = [set() for i in range(self._rooms)]
        for room in fp: #loop for room in file pointer
            room = [int(i) for i in room.split()]
            self._matrix[room[0]-1].update([room[1]])
            self._matrix[room[1]-1].update([room[0]])

    def __str__(self):
        #Return the matrix as a string
        s = ''
        for i in range(self._rooms):
            s += "{}: {}\n".format(i+1, ' '.join([str(j) for j in self.adjacent(i+1)]))
        return s  #__str__ always returns a string

    def __repr__(self):  # no modification need of this method
        #Call __str__() to return a string for displaying in the shell
        return self.__str__()  
        
    def adjacent(self,index):
        #Return the set of connecting rooms to room specified by index
        return self._matrix[index-1]

    def rooms(self):
        #Return the number of rooms
        return self._rooms

    
def greedy_TA(matrix):
    #Returns number of TA's required for serving rooms and their placement
    rooms = matrix.rooms()
    rooms_set = set(range(1, rooms+1))
    TA_num = 1
    while TA_num != rooms:  #loops for TA number and rooms with updating TA matrix
        for comb in itertools.combinations(rooms_set, TA_num):
            connected = set()
            for TA in comb:
                connected.update(matrix.adjacent(TA))
                connected.update([TA])
            if connected == rooms_set:
                return TA_num, comb
        TA_num += 1
    else:
        return TA_num, rooms_set

        
def open_file():
    #Asks user for file name until it can be opened and returns file object.
    while True:
        file_name = input("Enter a file name: ") 
        try: 
            return open(file_name, 'r')
        except Exception:
            print("File not found.")

            
def main():
    #Main cycle of program: asks for file with rooms representation and founds required TAs.
    file = open_file()
    M = Matrix()
    M.read_file(file)
    TA_num, TA_rooms = greedy_TA(M)
    print("TAs needed: {}".format(TA_num))
    print("TAs assigned to rooms: {}".format(','.join([str(tr) for tr in TA_rooms])))
    print('\nAdjacency Matrix')
    print(M)

if __name__ == "__main__":
    main()
    
# Questions
# Q1: 6
# Q2: 2
# Q3: 3
# Q4: 6
# Q5: 7