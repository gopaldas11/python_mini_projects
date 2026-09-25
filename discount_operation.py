def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"

    if price <= 0:
        return "The price should be greater than 0"
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    discount_price = price * (1 - discount / 100)
    return discount_price

apply_discount(100, 20)
apply_discount(200, 50)
apply_discount(50, 0)
apply_discount(5, 100)
apply_discount(74.5, 20.0)


