
import numpy as np
class matrix(object):  
    
    def __init__(self,size):
   
        self.size = size + 1 #Create the size of the array
        self.slots = np.arange(self.size*self.size).reshape(self.size,self.size)
        count = 0  # Set a count variable that will be incremented for each cell that are not diagonal
        numbering = 0
        self.row = (np.array([0] * self.size)) # Create an array of None values with the array size
        
        self.col = (np.array([0] * self.size))
        row = (len(self.row)) 
        col = (len(self.col)) 
        
        for row_position in range(1,row):
            for col_position in range(1, col):
                
                self.map = np.concatenate([[row_position],[col_position]])  #Concatenate indexes
               
                if row_position == col_position:
                
                    self.slots[row_position][col_position] = 0  
                else:
                    numbering += 1

                    print('{0} : For indices {1} ->'.format(numbering,self.map))
 
                    count +=1
                    
                    self.slots[row_position][col_position] = count

                    print('patterns is : {0}.'.format(self.slots[row_position][col_position]))
         


# In[6]:


m = matrix(8)







