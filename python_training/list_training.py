countries = ["japan","israel","spain","italy"]

for country in countries:
    print (country)

countries = ["japan","israel","spain","italy","brazil"]

for country in countries:
    l = len(country)
    print (f"the length of {country} is {l}")

countries = ["japan","israel","spain","italy","brazil"]

list_length = len(countries)
slicing_list = countries [:2]
specific_place = countries [3]
slicing_to_end = countries [3:]
countries.append("mexico")
countries.insert(4,"cyprus")
if "israel" in countries:
    print ("israel found")
if "germany" in countries:
    print ("germany found")


