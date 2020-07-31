class Array:
    #The methods in this class are intended for use with the IPython console.
    #IDE Used: Spyder (part of the Anaconda distribution) is recommended to run it, but any Python IDE can be used
    
    def FindMaxValue(array,pos1,pos2):
        r = max(array[pos1:pos2]) #Find max value between given bounds
        x = [k for k, n in enumerate(array) if n == r] #Find indices at which max(es) are located
        return print('Max Value: ' + str(r) + ', Frequency: ' + str(len(x))) #Return nice display

    def FindMinPosition(array, pos1, pos2):
        r = min(array[pos1:pos2]) #Find min value between given bounds
        x = [k for k, n in enumerate(array) if n == r] #Find indices at which min(s) are located
        return print('Min Value: ' + str(r) + ', Indices: ' + str(x)) #Return nice display
    
    def Swap(array, pos1, pos2):
        array[pos1], array[pos2]=array[pos2], array[pos1]
        return print(array)
    
    def ShiftLeftByOne(array, pos1, pos2):
        #array.insert(pos1-1,[]) #Will add an extra space into array left-adjacent to pos1
        for k in list(range(pos1,pos2)):
            array.insert(k,array.pop(k+1))
        return print(array)
    
    def CreateRandomArray(size, minValue, maxValue):
        import random
        array = [] #Initialize array
        for k in list(range(size)): #Cycle thru each "entry" of array
            array.append(random.randint(minValue,maxValue)) #Fill in each "entry" of a row with a random number between given bounds
        return print(array)
    
    def CreateRandomMatrix(rows, cols, minVal, maxVal):
        import random
        matrix = [] #Initialize matrix
        for r in list(range(rows)):
            aRow = [] #Initialize a row of the matrix
            for c in list(range(cols)): #Cycle thru each column for each row
                aRow.append(random.randint(minVal, maxVal)) #Fill in each column of a row with a random number between given bounds
            matrix.append(aRow) #Add the row to the matrix
        return print(matrix) #Each returned list is a row of the matrix
    
    def CopyArray(array):
        return print(array[:])
    
    def FindInSortedArray(array, number):
        #Binary Search Algorithm (thanks for the hint!)
        L = 0
        R = len(array) - 1
        while L < R:
            m = (L + R) // 2
            if array[m] < number:
                L = m + 1
            elif array[m] > number:
                R = m - 1
            else:
                return print(m)
        return print('-1')
    
#Test all the methods
Array.FindMaxValue([1,2,7,3,4,5,6,7],0,8)
Array.FindMinPosition([1,2,3,4,1,5,6],0,5)
Array.Swap([1,2,3,4,5,6,7],4,6)
Array.ShiftLeftByOne([1,2,3,4,5,6,7],2,5)
Array.CreateRandomArray(7,1,9)
Array.CreateRandomMatrix(3,3,1,9)
Array.CopyArray([1,2,3,4,5,6,7])
Array.CopyArray([[1,2,3,4],[5,6,7]])
Array.FindInSortedArray([1,2,3,4,5,6,7],2)
Array.FindInSortedArray([1,2,3,4,5,6,7],6)
Array.FindInSortedArray([1,2,3,4,5,6,7],10)
