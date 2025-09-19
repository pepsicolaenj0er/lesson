orders = [1200, 550, 2300, 1200, 750, 3000, 550, 1000, 2300, 400]
sumOrders = sum(orders)
print("общая выручка равна =", sumOrders )
avgCheck = sumOrders / len(orders)
print("средний чек равен = ", avgCheck)
orderCounts = {}
for zxc in orders:
    if zxc in orderCounts: 
        orderCounts[zxc]+=1 
    else:
        orderCounts[zxc]=1

sortedOrders = sorted(orderCounts.items(), key=lambda x: x[1],reverse=True)
top_1 = sortedOrders[0]
print(top_1)
