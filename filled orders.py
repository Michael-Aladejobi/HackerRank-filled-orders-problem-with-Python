def filledOrders(order, k):

    total, count = 0, 0

    for order in sorted(order):

        pending_order = []

        if order <= k:

           pending_order.append(order)

           for pends in pending_order:

               if (total + pends) <= k:

                   count += 1

                   k -= pends

               elif k == 0 or order == []:

                   count = 0

    return count

print(filledOrders([2,10, 30] , 40))

