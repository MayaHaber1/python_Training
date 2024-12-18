

def find_letter_in_name(name , letter_to_find):
    print (f"trying to find letter in name {name}")
    index = name.index("a")
    if (index>0):
        print ("index found but it is not 0")
    else:
        print ("index found at the start")
    #print (index)



name1= ("shira")
letter1 = "i"
name2 = "ran"
name3 = "avi"
letter2 = "a"
find_letter_in_name(name1 , letter1)
