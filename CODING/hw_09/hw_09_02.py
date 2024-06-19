DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    # достаем из словаря скидку если есть, если нет - то дефолтную
    return price * (1 - customer.get("discount", DEFAULT_DISCOUNT))
