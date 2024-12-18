def city_analyzer(city,num_of_chars):
    index = city.index("-")
    city_start = city [:index]
    city_end = city [index+1:]
    length = len(city)

    print (f"city can split to 2 values {city_start} and {city_end}")
    print (f"he length of city is {length}")
    if (num_of_chars>3):
        print (f"num of chars is higher than 3")

        return length

city_1 = 'new-york'
city_2 = 'ramat-gan'
city_3 = 'tel-aviv'
city_analyzer(city_1,3)
city_analyzer(city_2,6)
length_from_function = city_analyzer(city_3,8)
print (f"length is {length_from_function}")
