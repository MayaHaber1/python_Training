##from python_training.if_examples import summery, multiple


def nums_calculator (first_num , second_num):
    summery = first_num+second_num
    diff = first_num-second_num
    multiple = first_num * second_num
    print (f"the summery of numbers is {summery}")
    print (f"the diffrance is {diff}")
    return multiple


num1 = 23
num2 = 34
num3 = 20
multiple_from_function_1 = nums_calculator(num1,num2)
nums_calculator(num2,num3)
multiple_from_function_2 = nums_calculator(num1,num3)

if (multiple_from_function_2>multiple_from_function_1):
    print ("the first number is higher")



