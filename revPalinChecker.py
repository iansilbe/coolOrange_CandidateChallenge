def revPalinChecker(word):
    charword = [char for char in word] #Split word into individual chars
    #Length of word doesn't matter (no need for modulo operator)
    end = int(len(charword)/2) + 1 #Long variable deserves its own line; see next comment
    tempVec = [] 
    for k in list(range(1,end)): #Need an iterable data type that matches first index with last index (0 != -1)
        tempVec.append(charword[k-1] == charword[-k]) #Perform operation & store result
    if tempVec.count(True) == end-1: #Ensure all checking operations came back affirmative
        print(word + ' is a palindrome.') #Display nice result
    else: #At least one checking operation came back negative
        print(word + ' is not a palindrome.') #Display nice result

#Test the method
revPalinChecker('noon')   
revPalinChecker('kayak')
revPalinChecker('canoe')
revPalinChecker('yacht')
revPalinChecker('123321')
revPalinChecker('racecar')
revPalinChecker('rats live on no evil star')
