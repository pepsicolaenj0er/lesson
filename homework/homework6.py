orders = [1200, 550, 2300, 1200, 750, 3000, 550, 1000, 2300, 400]

sumOrders = sum(orders)  #  Good: используешь встроенную функцию sum()
print("общая выручка равна =", sumOrders )

avgCheck = sumOrders / len(orders)  #  верно
print("средний чек равен = ", avgCheck)  # МОЖЕШЬ УЛУЧШИТЬ, округлить через round(avgCheck, 2)

orderCounts = {}
for zxc in orders:
    if zxc in orderCounts:           # СЛИШКОМ ИЗБЫТОЧНО, IF для подобного не нужен, лучше упростить и укоротить за счет get метода встроенный в списки 
        orderCounts[zxc]+=1 
    else:
        orderCounts[zxc]=1

# Правильно
sortedOrders = sorted(orderCounts.items(), key=lambda x: x[1], reverse=True)

top_1 = sortedOrders[0]  # Отлично
print(top_1)  # Улучши вывод, сделай более понятный и симпатичный (работа с строками никогда не помешает, в будущем будет проще дебажить если будешь часто выводить красиво
