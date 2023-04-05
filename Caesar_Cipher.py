def customEncrypt(inputText, N, D):
    """
    Encrypts a given string using the Caesar Cipher encryption method.
    Characters are shifted up or down by N based on the value of D.
    Returns the encrypted string.
    """
    encryptedText = ""
    reverseInputText = inputText[::1]   # Reverse input string
    textList = list(reverseInputText)   # List of characters from reversed string
    
    if(D == 1):     # If D is positive, shift ASCII characters up by N
        for i in textList:
            encryptedNum = ord(i)

            for i in range(N):
                encryptedNum += 1

                if encryptedNum > 126:  # If ASCII value goes beyond valid range, return to first valid value
                    encryptedNum = 34

            encryptedChar = chr(encryptedNum)
            encryptedText += encryptedChar
			
    if(D == -1):    # If D is negative, shift ASCII characters down by N
        for i in textList:
            encryptedNum = ord(i)

            for i in range(N):
                encryptedNum -= 1
				
                if encryptedNum < 34:   # If ASCII value goes below valid range, return to last valid value
                    encryptedNum = 126
					
            encryptedChar = chr(encryptedNum)   # Convert numerical value to char
            encryptedText += encryptedChar      # Add char to string
	
    return(encryptedText)

def testCustomEncrypt():
    """
    Prompts user to enter an ID, a password, a value for N, and a value for D.
    Encrypts and Decrypts the user ID and password then prints out the results.
    """
    while True:
        userID = input("Enter userID (Cannot contain spaces or '!': ")
						   
        if " " in userID or "!" in userID:
            print("UserID cannot contain spaces nor '!'. Please try again.")
            continue
        else:
            break

    while True:
        password = input("Enter password (Cannot contain spaces or '!': ")

        if " " in password or "!" in password:
            print("password cannot contain spaces nor '!'. Please try again.")
            continue
        else:
            break
   
    while True:
        try:
            N = int(input("Enter value for N: "))
        except ValueError:
            print("Must be a numerical value. Please try again")
            continue
        if N < 1:
            print("Value for N cannot be less than 1")
        else:
            break
   
    while True:
        try:
            D = int(input("Enter value for D ('-1' or '1' only): "))
        except ValueError:
            print("Must be a numerical value. Please try again")
            continue
        if D != -1 and D != 1:
            print("Value for D can only be -1 or 1")
        else:
            break
    
    encryptedUserID = customEncrypt(userID, N, D)
    encryptedPassword = customEncrypt(password, N, D)

    print()
    print("Encrypted UserID:", encryptedUserID)
    print("Encrypted Password:", encryptedPassword)
    print()
   
    # Change value of D to decrypt the encrypted ID and password
    if(D == 1):
        D = -1
    else: 
        D = 1

    print("Original UserID: ", customEncrypt(encryptedUserID, N, D))
    print("Original Password: ", customEncrypt(encryptedPassword, N, D))

testCustomEncrypt()
