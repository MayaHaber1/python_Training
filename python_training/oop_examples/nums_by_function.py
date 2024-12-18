from utils import utils

def nums_calculate (start_num , end_num):
    multiple = start_num * end_num
    print (f"the multiple value is {multiple}")
    for i in range (start_num,end_num):
        print (i)


#start running code

utils_from_other_file = utils ()


num1 = 3
num2 = 9
nums_calculate(num1,num2)

#end running code