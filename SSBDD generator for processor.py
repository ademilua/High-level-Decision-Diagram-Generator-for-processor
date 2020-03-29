import numpy as np
import time
class matrix(object):
    def __init__(self, size, pattern):
        start_time = time.time()
        self.size = size + 1  # Create the size of the array
        self.slots = np.arange(self.size * self.size).reshape(self.size, self.size)
        weights = []  # creates an empty list for weights
        for i in pattern:  # adds unique elements from pattern in weights
            if (i not in weights):
                weights.append(i)
        weights.sort()  # sorts the list
        count = 0  # Set a count variable that will be incremented for each cell that are not diagonal
        numbering = 0
        self.row = (np.array([0] * self.size))  # Create an array of 0 values with the array size
        self.col = (np.array([0] * self.size))
        row = (len(self.row))
        col = (len(self.col))
        for row_position in range(1, row):
            for col_position in range(1, col):
                self.map = np.concatenate(
                    [[row_position], [col_position]])  # Concatenate the index from row and col together to get indices
                if row_position == col_position:
                    self.slots[row_position][col_position] = 0
                else:
                    numbering += 1
                    print(f'{numbering} : For indices {self.map} ->')
                    self.slots[row_position][col_position] = pattern[count]
                    w = weights.index(pattern[count]) + 1
                    count += 1
                    print(f'Pattern is: {self.slots[row_position][col_position]}', end='|')
                    print('Weight is : {0}.'.format(w))
                    print("_" * 30)
        print('----------------Matrix Table-----------')
        print('Note Row 0 and column 0 are not used')
        print(self.slots)
        print('-----------------------------------------')
        self.lis_patt = []  # creates list to get pattern matrix with respect to weights
        for m in range(1, self.size):
            l = []
            for i in range(1, self.size):
                for j in range(1, self.size):
                    if (i != j):
                        if (i == m or j == m):  # if true append the index of that slot but not the slot pattern
                            l.append(self.slots[i][j])
            self.lis_patt.append(l)
        print('--------------Corresponding Patterns ----------------')
        c = 1
        for i in self.lis_patt:  # prints weights(indexes) of all patterns resides in the slots
            print(f'{c} -> {i}')
            c += 1
        print('Note each row in the patterns list hold values from row and column based on relationship')
        self.lis = []  # creates list to get pattern matrix with respect to weights
        for m in range(1, self.size):
            l = []
            for i in range(1, self.size):
                for j in range(1, self.size):
                    if (i != j):
                        if (i == m or j == m):  # if true append the index of that slot to a list
                            l.append(weights.index(self.slots[i][j]) + 1)
            self.lis.append(l)
        print('--------------Weights from the Corresponding patterns----------------')
        c = 1
        for i in self.lis:  # prints weights(indexes) of all patterns resides in the slots
            print(f'{c} -> {i}')
            c += 1
        print('Note each row in the weights list hold values from row and column based on relationship')
        self.sumlis = []  # creates list to get sum for all weights
        for i in self.lis:
            s = 0
            for k in i:
                s += k
            self.sumlis.append(s)
        print('---------------Sum of Weights for {0} functions---------------- '.format(self.size - 1)) #str.format()
        c = 1
        for i in self.sumlis:  # calculates total sum
            print('{0} -> {1}'.format(c, i))
            c += 1
        self.totalsum = sum(self.sumlis)
        print(f'-----------Total sum of weights for {self.size - 1} functions = : {self.totalsum}')#string interpolation format
        print('Main Sum List :', self.sumlis)
        print('\n\nGraph\n')
        a = []
        for i in range(1, len(self.sumlis) + 1):  # stores indexes of sumlis in list for graph plotting
            a.append(i)
        self.graph(a)
        print("--- %s seconds ---" % (time.time() - start_time))
    def graph(self, tindex):  # shows graph
        total = 0
        vals = []  # stores sum values of indexes
        for i in tindex:
            total += self.sumlis[i - 1]
            vals.append(self.sumlis[i - 1])
        half = total // 2  # calculates half
        s = 0  # stores total sum
        firsthalf = []
        sechalf = []  # saves rest of values
        #firsthalf_vals = []
        #sechalf_vals =[]
        for i in range(len(vals)):
            if s + vals[i] <= half:  # saves values that can be stored together and have sum less or equal to half
                s += vals[i]
                firsthalf.append(tindex[i])
                #firsthalf_vals.append(vals[i])
            else:  # saves rest of values
                sechalf.append(tindex[i])
                #sechalf_vals.append(vals[i])
        #print(vals, '->', firsthalf_vals, 'and', sechalf_vals)
        print(tindex, '->', firsthalf, ' and ', sechalf)
        if (len(firsthalf) >= 2):  # runs for first half
            self.graph(firsthalf)
        if (len(sechalf) >= 2):  # runs of second half
            self.graph(sechalf)

a = matrix(20,
           [0, 3, 3, 7, 7, 8, 11, 11, 11, 12, 13, 15, 17, 17, 17, 17, 17, 17, 17, 0, 3, 3, 7, 7, 8, 11, 11, 11, 12, 13,
            15, 17, 17, 17, 17, 17, 17, 17, 3, 3, 3, 5, 5, 7, 9, 9, 9, 10, 10, 11, 12, 12, 12, 12, 12, 12, 12, 3, 3, 3,
            5, 5, 7, 9, 9, 9, 10, 10, 11, 12, 12, 12, 12, 12, 12, 12, 2, 2, 4, 4, 5, 5, 7, 7, 7, 8, 9, 10, 11, 11, 11,
            11, 11, 11, 12, 6, 6, 9, 9, 9, 9, 9, 9, 9, 11, 12, 15, 18, 18, 18, 18, 18, 18, 18, 3, 3, 5, 5, 6, 6, 8, 8,
            8, 9, 10, 12, 14, 14, 14, 14, 14, 14, 14, 2, 2, 3, 3, 5, 5, 5, 5, 5, 6, 7, 9, 10, 10, 10, 10, 10, 10, 10, 2,
            2, 3, 3, 5, 5, 6, 8, 8, 9, 9, 11, 12, 12, 12, 12, 12, 12, 12, 2, 2, 3, 3, 5, 5, 6, 8, 8, 8, 8, 10, 11, 11,
            11, 11, 11, 11, 11, 3, 3, 4, 4, 7, 7, 8, 11, 11, 11, 11, 13, 14, 14, 14, 14, 14, 14, 14, 3, 3, 5, 5, 7, 7,
            8, 11, 11, 11, 11, 13, 14, 14, 14, 14, 14, 14, 14, 2, 2, 3, 3, 5, 5, 6, 8, 8, 8, 8, 8, 11, 11, 11, 11, 11,
            11, 11, 2, 2, 4, 4, 7, 7, 7, 8, 8, 8, 9, 9, 12, 13, 13, 13, 13, 13, 13, 2, 2, 4, 4, 6, 6, 6, 8, 8, 9, 9, 9,
            13, 13, 13, 13, 13, 13, 13, 2, 2, 3, 3, 5, 5, 5, 6, 6, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 1, 1, 2, 2, 4, 4,
            4, 5, 5, 5, 6, 6, 7, 8, 8, 8, 8, 8, 8, 3, 3, 5, 5, 5, 6, 6, 7, 7, 7, 9, 10, 12, 13, 13, 13, 13, 13, 13, 3,
            3, 5, 5, 5, 6, 6, 7, 7, 7, 9, 10, 12, 13, 13, 13, 13, 13, 13, 3, 3, 5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 11, 12,
            12, 12, 12, 12, 12])

