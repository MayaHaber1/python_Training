city = ("ramat gan")

index = city.index(" ")

begin = city[:index]
end = city[index:]


price = 'the price is 28$ as expected'
end_index =price.index('$')
start_index =price.index('is ')

price_last = price[start_index+3:end_index]
price.count(" ")
price_cap = price.capitalize()

price_last_updated = price_last.replace('is ',"")



print (f"test end")