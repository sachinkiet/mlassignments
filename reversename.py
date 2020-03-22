def reversename():
    firstname = input("Pleae enter first name->")
    lastname = input("Pleae enter last name->")
    print( lastname[::-1] + ' ' + firstname[::-1])

reversename()