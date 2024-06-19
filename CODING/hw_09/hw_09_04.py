def discount_price(discount):
    def get_discount_price_customer(price):
        # достаем из словаря скидку если она есть, если нет - дефолтную
        return price * (1 - discount)
    return get_discount_price_customer
