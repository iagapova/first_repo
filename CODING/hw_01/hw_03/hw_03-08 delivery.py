def cost_delivery(quantity, *items, discount=0):
    if quantity >= 1:
        if discount >0:
            return (5 + (quantity -1)*2) * discount
        else:
            return (5 + (quantity -1)*2)
    else:
        return 0