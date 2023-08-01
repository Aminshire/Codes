menu = ["Coffee","Tea","Cake","Sandwich"]
stock = {menu[0]:15,menu[1]:20,menu[2]:10,menu[3]:5}
price = {menu[0]:3, menu[1]:2, menu[2]:2.5, menu[3]:2}
m = 0
total_stock = 0
for i in stock.values():
    item_price = i * price.get(menu[m])
    total_stock += item_price
    m += 1
print(total_stock)