##for i in range (10):
#    print (i)

#for i in range (2,10):
#    print (i)

#for i in range (2,20,2):
 #   print (i)

#for i in range (1,20,5):
 #       print (i)

num = 3

for i in range (10):
    result = num * i
    print (result)

    if (result > 10):
      print ("the number is higher than 10")
      break

num = 3
for i in range (1,100):
    result = i % num
    if (result == 0):
        print (f"the number is {i}")



