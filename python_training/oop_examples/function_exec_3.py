from python_training.loop_examples import result


def numbers_more_100 (number):
    if (number > 100):
        print (f"{number} is more than 100")
        return number



numbers = [53,107,109,300,1004]
results=[]
for number in numbers:
    number = numbers_more_100(number)
    results.append(number)
    print (f"fron line 10 {number} is more than 100")
    print (f"{result}")