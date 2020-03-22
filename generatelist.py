def generatelist():
    userstring = input("Please enter the comma seprated string->")
    
    if(userstring != ''):
        userlist = userstring.split(',')
        print(userlist)
    else:
        print('String can\'t be blank')
        generatelist()
    
generatelist()