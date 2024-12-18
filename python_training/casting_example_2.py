age = "23"
age_as_int = int(age)
if age_as_int<30 :
    print ("match found")

age_updated = "1234567"
index = age_updated.index("3")
print (f"test end index is {index}")

age_updated = 12345678
age_updated_as_str = str(age_updated)
index = age_updated_as_str.index ("3")
print (f"test end index is {index}")

price = "28$"
price.replace("$", "")
price = price.replace("$", "ILS")
print (price)

