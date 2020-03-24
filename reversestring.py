def reversestring():
    userstring = "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"
    newstring = ''
    userstring = userstring.split(",",2)
    i = 0
    while i < len(userstring):
        newstring += "\t" * i + userstring[i]
        i += 1
    print(newstring)
    
reversestring()
