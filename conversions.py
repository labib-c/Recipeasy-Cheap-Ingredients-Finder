def tablespoons_to_100ml(tbsp):
    return (tbsp*15) / 100


def cups_to_100ml(cups):
    return (cups*225) / 100

def ml_to_100ml(ml):
    return ml/100

# def pound_to_100g(pounds):
#     return (pounds*450) / 100


def ounce_to_100g(ounces):
    return (ounces*30) / 100

def grams_to_100g(grams):
    return grams/100

def get_loblaws_quantity(desired_quantity):
    if desired_quantity == "g" or desired_quantity == "ounce":
        return "100g"
    elif desired_quantity == "tbsp" or desired_quantity == "cups" or desired_quantity == "ml":
        return "100mL"
    else:
        return desired_quantity

def convert_quantities(price, number, quantity):
    if quantity == "cups":
        return cups_to_100ml(number) * price
    elif quantity == "tbsp":
        return tablespoons_to_100ml(number) * price
    elif quantity == "ml":
        return ml_to_100ml(number) * price
    elif quantity == "ounce":
        return ounce_to_100g(number) * price
    elif quantity == "g":
        return grams_to_100g(number) * price


