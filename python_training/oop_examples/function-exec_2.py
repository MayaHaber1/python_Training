def get_pattern_length (first_name):
    length_name = len(first_name)
    return length_name

first_name = "maya"
last_name = "haber"
first_len = get_pattern_length(first_name)
second_len = get_pattern_length(last_name)
if first_len>second_len :
    print(f"first name is longer")
    print (f"{first_name} {last_name}")
else:
    print (f"last name is longer")
    print(f"{last_name} {first_name}")
print ("test end")

