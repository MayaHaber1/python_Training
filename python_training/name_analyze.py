city = "new_york"

index = city.index ("_")
before = city[:index]
after = city[index+1:]
len_before = len(before)
len_after = len(after)
if (len_after > len_before):
    print ("the second part of tested city is longer")
print ("test end")
