def palindromeChecker(word):
    chars = list(word) #Break up string into components
    revChars = list(reversed(chars)) #Reverse characters
    return print(chars == revChars) #Check to see if regular is the same as reverse
            
#Run a bunch of test cases       
palindromeChecker('123321') #Input parameter must be a string
palindromeChecker('noon') #Palindrome
palindromeChecker('racecar') #Palindrome
palindromeChecker('rats live on no evil star') #Palindrome
palindromeChecker('Ian Silberzweig') #Not palindrome