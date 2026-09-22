#Function definition with default argument

def showinfo( name, city = "Hyderabad" ):
#This prints a passed info into this function
    print ("Name:", name)
    print ("City:", city)
    return
# Now call showinfo function
showinfo(name = "Aanshi", city = "chennai")
showinfo(name = "Saritha")